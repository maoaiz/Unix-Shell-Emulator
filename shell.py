# -*- coding: cp1252 -*-
import getpass

def get_user(u, p):
    """Buscar en el archivo"""
    return True

def get_command(c):
    """Buscar en el archivo"""
    return "este comando no hace nada"

def init_shell(u):
    command = raw_input("{user}@shell-emulator:~$ ".format(user=u))
    if command == "exit":
        return command
    info = get_command(command)
    print info
    init_shell(u)


def login():
    username = raw_input("\nLogin:$ ")
    if username == "exit":
        return username
    password = getpass.getpass("Password for {user}:~$ ".format(user=username))
    if get_user(username, password):
        return username
    else:
        return False

def main():
    print "Welcome to ShellEmulator by Mauricio Aizaga\n@MaoAiz"
    while True:
        user = login()
        if user:
            if user == "exit":
                print "The program has finished correctly, see you later.\n\nVisit us at http://mauricioaizaga.com\n"
                break      
            else:
                print "Welcome", user, "\n"
                init_shell(user)
        else:
            print "Invalid password for", user, "\n"
    exit()




main()
