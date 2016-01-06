#!/usr/bin/env python
import argparse
import os
import urllib2

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])
cls()

RED1 = '\033[31m'
AMARILLO = '\033[33m'
BLUE = '\033[94m'
GREEN = '\033[32m'
OTRO = '\033[36m'
BOLD = '\033[1m'
ENDC = '\033[0m'

logo = BLUE + """
    #     # ######  ####### #######                      
    ##   ## #     # #          #     ####   ####  #      
    # # # # #     # #          #    #    # #    # #      
    #  #  # #     # ######     #    #    # #    # #      
    #     # #     #       #    #    #    # #    # #      
    #     # #     # #     #    #    #    # #    # #      
    #     # ######   #####     #     ####   ####  ######  
          Blog   : dth-security.blogspot.com
          Twitter: @s1kr10s
""" + ENDC

print logo
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--opcion", required=True,
                help="Ej: --opcion encode/decode]")
ap.add_argument("-c", "--crack", required=False,
                help="Ej: --crack 21232f297a57a5a743894a0e4a801fc3")
ap.add_argument("-l", "--lista", required=False,
                help="Ej: --lista lista_de_hash.txt")
args = vars(ap.parse_args())

opcion = args["opcion"]
phrasehash = args["crack"]
lista = args["lista"]
apikey = "pLH3vFY1E9eXMlex";

#conexion get data
def getdatos(tipo, apikey, phrasehash):
    req = urllib2.Request("http://api.md5crack.com/" + tipo + "/" + apikey + "/" + phrasehash)
    contents = urllib2.urlopen(req)
    html = contents.read()
    return html

#encode string
if opcion == 'encode':
    tipos = "hash";
    if phrasehash <> None and lista == None:
        data = getdatos(tipos, apikey, phrasehash)
         
        html = data.split('","')
        code = html[3].split('":')
        code = code[1].split('}')

        if code[0] == '5':
            phrase = html[0].split('":"')
            print BOLD + "      STRING : " + ENDC + GREEN + str(phrasehash) + ENDC
            print BOLD + "      HASH   : " + ENDC + GREEN + str(phrase[1]) + ENDC + '\n'
              
#cracking hash
elif opcion == 'decode':
    tipos = "crack";
    if phrasehash <> None and lista == None:
        if(len(phrasehash) == 32):
            data = getdatos(tipos, apikey, phrasehash)

            html = data.split('","')
            code = html[3].split('":')
            code = code[1].split('}')
            if code[0] == '6':
                phrase = html[0].split('":"')
                print BOLD + "      HASH  : " + ENDC + GREEN + str(phrasehash) + ENDC
                print BOLD + "      CRACK : " + ENDC + GREEN + str(phrase[1]) + ENDC + '\n'
            else:
                print BOLD + "      HASH  : " + ENDC + RED1 + str(phrasehash) + ENDC
                print BOLD + "      CRACK : " + ENDC + RED1 + "No Encontrado" + ENDC + '\n'
        else:
            print AMARILLO + "      El HASH " + BOLD + phrasehash + ENDC + AMARILLO + " no es de tipo MD5." + ENDC + '\n'
    elif lista <> None:
        if os.path.isfile(lista) and os.access(lista, os.R_OK):
            listahash = file(lista, "r")
            for hashlista in listahash:
                hashlista = hashlista.rstrip()
                data = getdatos(tipos, apikey, hashlista)

                html = data.split('","')
                code = html[3].split('":')
                code = code[1].split('}')
                if code[0] == '6':
                    phrase = html[0].split('":"')
                    print BOLD + "      HASH  : " + ENDC + GREEN + str(hashlista) + ENDC
                    print BOLD + "      CRACK : " + ENDC + GREEN + str(phrase[1]) + ENDC + '\n'
                else:
                    print BOLD + "      HASH  : " + ENDC + RED1 + str(hashlista) + ENDC
                    print BOLD + "      CRACK : " + ENDC + RED1 + "No Encontrado" + ENDC + '\n'
        else:
            print AMARILLO + "      El Archivo " + BOLD + lista + ENDC + AMARILLO + " no pudo ser encontrado." + ENDC + '\n'
