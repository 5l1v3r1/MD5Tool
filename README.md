# MD5Tool
crackea tu hash md5

USO:

usage: md5tool.py [-h] -o OPCION [-c CRACK] [-l LISTA]<br>
optional arguments:<br>
  -h, --help            show this help message and exit<br>
  -o OPCION, --opcion OPCION<br>
                        Ej: --opcion encode/decode]<br>
  -c CRACK, --crack CRACK<br>
                        Ej: --crack 21232f297a57a5a743894a0e4a801fc3<br>
  -l LISTA, --lista LISTA<br>
                        Ej: --lista lista_de_hash.txt<br><br>


Ejemplos:

- Crackear solo un hash.<br>
<b>python md5tool.py -o decode -c 21232f297a57a5a743894a0e4a801fc3</b>

- Crackear con una lista de hash.<br>
<b>python md5tool.py -o decode -l hash_lista.txt</b>

- Crear hash md5.<br>
<b>python md5tool.py -o encode -c admin</b>


