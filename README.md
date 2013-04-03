janubox
=======

An directory synchronizer.


janubox-server:
postgres
bsdiff4 - https://pypi.python.org/pypi/bsdiff4/1.0.1
base64 para transferir os dados
json para envio e recebimento de mensagens
argumentos da linha de comando: porta, intranet, internet ou local
								endereço servidor bd, usuário, senha ou url_db
abrir socket
lançar thread para cada operação
operações: add_file, remove_file, edit_file, change_base_directory_file,
			add_user, remove_user, edit_user.

janubox-client:
bsdiff4
argumentos linha de comando: base_directory no servidor, dest_dir (opcional), usuário e senha,
							endereço servidor, porta.

database:
directory: id, name
file: id, uri, directory
revision: id, file, user, data
log: id, user, operation
operation: id, name
user: id, login, password

json format:
{operation:'authorize', md5:'', base_directory:''}
{operation:'add_file', file_uri:'', base_directory:'', data:''}
{operation:'edit_file', file_uri:'', base_directory:'', data:''}
{operation:'remove_file', file_uri:'', base_directory:'', data:''}