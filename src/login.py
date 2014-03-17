# -*- coding: utf8 -*-
import getpass
USERS_FILE_DIR = "data/users.txt"


def get_user(u, p):
    """Buscar en el archivo"""
    try:
        f = open(USERS_FILE_DIR)
        for line in f.readlines():
            l = line.strip('\n').split(" ")
            if l[0] == u and l[1] == p:
                f.close()
                return True
        f.close()
        return False
    except Exception, e:
        print "[Exception] ", e
        return False


def login():
    username = raw_input("\nLogin:$ ")
    if username == "exit":
        return username
    password = getpass.getpass("Password for {user}:~$ ".format(user=username))
    if get_user(username, password):
        return username
    else:
        return False
