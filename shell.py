# -*- coding: cp1252 -*-
import getpass

def get_user(u, p):
    print "Logueando a", u, "..."
    return True

def get_command(c):
    return "este comando no hace nada"

def init_shell(u):
    command = raw_input("{user}@shell-emulator ~ $ ".format(user=u))
    info = get_command(command)
    if command == "exit":
        exit()
    else:
        print info
        init_shell(u)


def login():
    print "\nLogin:"
    username = raw_input("no-user@shell-emulator ~ $ ")
    password = getpass.getpass("password for {user} ~ $".format(user=username))

    if get_user(username, password):
        print "Bienvenido", username, "\n"
        init_shell(username)
    else:
        print "Invalid password for", username
        login()

def main():
    print "Bienvendo a ShellEmulator\n"
    login()



main()
raw_input()
