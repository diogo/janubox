janubox
=======

An directory synchronizer.


janubox-server:
postgres
bsdiff4 - https://pypi.python.org/pypi/bsdiff4/1.0.1

janubox-client:
bsdiff4


database:
directory: id, name
file: id, name, directory
revision: id, file, user, data
log: id, user, operation
operation: id, name
user: id, login, password

