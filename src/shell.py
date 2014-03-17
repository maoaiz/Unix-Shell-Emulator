# -*- coding: utf8 -*-
COMMANDS_FILE_DIR = "data/commands.txt"


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
