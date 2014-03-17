# -*- coding: utf8 -*-
from .login import login
from .shell import init_shell


def main():
    print "Welcome to ShellEmulator by Mauricio Aizaga\n@MaoAiz"
    while True:
        user = login()
        if user:
            if user == "exit":
                print "The program has finished correctly, see you later.\n\nVisit us at http://mauricioaizaga.com\n"
                break      
            else:
                print "...Welcome", user, "...\n"
                init_shell(user)
        else:
            print "Login incorrect."
    exit()


main()
