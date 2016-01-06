# MD5Tool
crackea tu hash md5

USO:

usage: md5tool.py [-h] -o OPCION [-c CRACK] [-l LISTA]<br>
optional arguments:
  -h, --help            show this help message and exit
  -o OPCION, --opcion OPCION
                        Ej: --opcion encode/decode]
  -c CRACK, --crack CRACK
                        Ej: --crack 21232f297a57a5a743894a0e4a801fc3
  -l LISTA, --lista LISTA
                        Ej: --lista lista_de_hash.txt


Ejemplos:

- Crackear solo un hash.
python md5tool.py -o decode -c 21232f297a57a5a743894a0e4a801fc3

- Crackear con una lista de hash.
python md5tool.py -o decode -l hash_lista.txt

- Crear hash md5.
python md5tool.py -o encode -c admin


