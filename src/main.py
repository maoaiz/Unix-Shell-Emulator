# -*- coding: utf8 -*-
from .login import login
from .shell import init_shell
HELP_TEXT = """You need login to use the ShellEmulator.

You need type your username and your password to login.

We have a guest user if you don't have anyone.

username: guest
password: guest"""


def main():
    print "Welcome to ShellEmulator by Mauricio Aizaga\n@MaoAiz"
    while True:
        init_shell("admin")
        user = login()
        if user:
            if user == "exit":
                print "The program has finished correctly, see you later.\n\nVisit us at http://mauricioaizaga.com\n"
                break
            elif user == "help":
                print HELP_TEXT
            else:
                print "...Welcome", user, "...\n"
                init_shell(user)
        else:
            print "Login incorrect."
    exit()


main()
