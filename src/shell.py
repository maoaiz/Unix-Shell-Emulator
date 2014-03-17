# -*- coding: utf8 -*-
COMMANDS_FILE_DIR = "data/commands.txt"
HELP_TEXT_SHELL = """
Type ls, cat, mkdir, cd, or any unix command to show its descrition
"""
HELP_TEXT_SHELL_ES = u"""
Estas órdenes del shell están definidas internamente.  Teclee 'help' para ver esta lista.
Teclee 'help nombre' para saber más sobre la función 'nombre'.

id_trabajo [&]                                                                      history [-c] [-d despl] [n] ó history -anrw [fichero] ó history -ps arg [arg..>
 (( expresión ))                                                                    if ÓRDENES; then ÓRDENES; [ elif ÓRDENES; then ÓRDENES; ]...[ else ÓRDENES;>
 . fichero [argumentos]                                                              jobs [-lnprs] [idtrabajo ...] o jobs -x orden [args]
 :                                                                                   kill [-s id_señal | -n num_señal | -id_señal] pid | idtrabajo ... ó kill -l >
 [ arg... ]                                                                          let arg [arg ...]
 [[ expresión ]]                                                                    local [opción] nombre[=valor] ...
 alias [-p] [nombre[=valor] ... ]                                                    logout [n]
 bg [id_trabajo ...]                                                                 mapfile [-n cuenta] [-O origen] [-s cuenta] [-t] [-u df] [-C llamada] [-c quantu>
 bind [-lpvsPVS] [-m comb_teclas] [-f fichero] [-q nombre] [-u nombre] [-r sectecl>  popd [-n] [+N | -N]
 break [n]                                                                           printf [-v var] formato [argumentos]
 builtin [orden-interna-shell [arg ...]]                                             pushd [-n] [+N | -N | dir
 caller [expresión]                                                                 pwd [-LP]
 case PALABRA in [PATRÓN [| PATRÓN]...) ÓRDENES ;;]... esac                       read [-ers] [-a matriz] [-d delim] [-i texto] [-n ncars] [-N ncars] [-p prompt] >
 cd [-L|[-P [-e]]] [dir]                                                             readarray [-n cuenta] [-O origen] [-s cuenta] [-t] [-u df] [-C llamada] [-c quan>
 command [-pVv] orden [arg ...]                                                      readonly [-aAf] [nombre[=valor] ...] o readonly -p
 compgen [-abcdefgjksuv] [-o opción]  [-A acción] [-G patglob] [-W listapalabras>  return [n]
 complete [-abcdefgjksuv] [-pr] [-DE] [-o opción] [-A acción] [-G patglob] [-W l>  select NOMBRE [in PALABRAS ... ;] do ÓRDENES; done
 compopt [-o|+o opción] [-DE] [nombre ...]                                          set [-abefhkmnptuvxBCHP] [-o option-name] [--] [arg ...]
 continue [n]                                                                        shift [n]
 coproc [NOMBRE] orden [redirecciones]                                               shopt [-pqsu] [-o] [nombre_opción...]
 declare [-aAfFgilrtux] [-p] [nombre[=valor] ...]                                    source fichero [argumentos]
 dirs [-clpv] [+N] [-N]                                                              suspend [-f]
 disown [-h] [-ar] [idtrabajo ...]                                                   test [expresión]
 echo [-neE] [arg ...]                                                               time [-p] tubería
 enable [-a] [-dnps] [-f fichero] [nombre ...]                                       times
 eval [arg ...]                                                                      trap [-lp] [[arg] id_señal ...]
 exec [-cl] [-a nombre] [orden [argumentos ...]] [redirección ...]                  true
 exit [n]                                                                            type [-afptP] nombre [nombre ...]
 export [-fn] [nombre[=valor] ...] ó export -p                                      typeset [-aAfFgilrtux] [-p] nombre[=valor] ...
 false                                                                               ulimit [-SHacdefilmnpqrstuvx] [límite]
 fc [-e nombre_e] [-lnr] [primero] [último] ó fc -s [pat=rep] [orden]              umask [-p] [-S] [modo]
 fg [id_trabajo]                                                                     unalias [-a] nombre [nombre ...]
 for NOMBRE [in PALABRAS ... ] ; do ÓRDENES; done                                   unset [-f] [-v] [nombre ...]
 for (( exp1; exp2; exp3 )); do ÓRDENES; done                                       until ÓRDENES; do ÓRDENES; done
 function nombre { ÓRDENES ; } ó nombre () { ÓRDENES ; }                          variables - Nombres y significados de algunas variables de shell
 getopts cadena_opciones nombre [arg]                                                wait [id]
 hash [-lr] [-p ruta] [-dt] [nombre ...]                                             while ÓRDENES; do ÓRDENES; done
 help [-dms] [patrón ...]                                                           { ÓRDENES ; }
"""


def get_command(c):
    """Buscar en el archivo"""
    command_info = u""
    get_info = False
    with open(COMMANDS_FILE_DIR, 'r+') as f:
        for line in f:
            l = line.strip('\n')
            if not get_info and l == c:
                command_info += l + "\n"
                get_info = True
            elif get_info:
                command_info += l.decode('utf8') + "\n"
                if l == "":
                    get_info = False
                    break
    if len(command_info) == 0:
        return "NO Existe el comando %s" % c
    return command_info

def init_shell(u):
    command = raw_input("{user}@shell-emulator:~$ ".format(user=u))
    if command == "exit":
        return command
    if command == "help":
    	print HELP_TEXT_SHELL_ES
    else:
        print get_command(command)
    init_shell(u)
