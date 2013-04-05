import json
from flask import Flask, request
from flask.ext.restful import Resource, reqparse
from janubox.server.messages import *
from janubox.server.database import *

parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

def read_auth(key, id, is_file=True):
	pass

def write_auth(key, id, is_file=True):
	pass

def admin_auth(key, bdir_id=False):
	pass

def super_auth(key):
	pass

def auth(key, bdir_id, flag):
	if flag == 'read':
		 = User.query.filter(User.key == 'key',
							Permission.user_id == User.id,
							Permission.bdir_id == 'bdir_id').first()

class Files(Resource):
	def post(self):
		args = parser.parse_args()
		if write_auth(args['key'], args['bdir_id'], False):
			pass

	def get(self):
		args = parser.parse_args()
		if read_auth(args['key'], args['bdir_id'], False):
			pass

class File(Resource):
	def get(self, file_id):
		args = parser.parse_args()
		if read_auth(args['key'], file_id):
			pass

	def put(self, file_id):
		args = parser.parse_args()
		if write_auth(args['key'], file_id):
			pass

	def delete(self, file_id):
		args = parser.parse_args()
		if write_auth(args['key'], file_id):
			pass

class BaseDirectories(Resource):
	def post(self):
		args = parser.parse_args()
		if super_auth(args['key']):
			pass

	def get(self):
		args = parser.parse_args()
		if super_auth(args['key']):
			pass

class BaseDirectory(Resource):
	def get(self, bdir_id):
		args = parser.parse_args()
		if read_auth(args['key'], bdir_id, False):
			pass

	def put(self, bdir_id):
		args = parser.parse_args()
		if admin_auth(args['key'], bdir_id):
			pass

	def delete(self, bdir_id):
		args = parser.parse_args()
		if admin_auth(args['key'], bdir_id):
			pass

class Users(Resource):
	def post(self):
		args = parser.parse_args()
		if super_auth(args['key']):
			pass

	def get(self):
		args = parser.parse_args()
		if super_auth(args['key']):
			pass
		elif read_auth(args['key']):
			pass

class User(Resource):
	def get(self, user_id):
		pass

	def put(self, user_id):
		pass

	def delete(self, user_id):
		pass


def add_resources(api):
	api.add_resource(Files, '/files')
	api.add_resource(File, '/files/<string:file_id>')
	api.add_resource(BaseDirectories, '/base_dirs')
	api.add_resource(BaseDirectory, '/base_dirs/<string:bdir_id>')















"""
class JanuBoxClient(object):
	def __init__(self, addr=None, ip=None, user=None):
		self.addr = addr
		self.ip = ip
		self.user = user

	def __eq__(self, other):
		return (self.addr == other.addr and self.ip == other.ip and self.user == other.user)

class JanuBoxServer(SocketServer.BaseRequestHandler):

	clients = []

	def treat_response(self, operation, ):

    def handle(self):
    	data = self.request.recv(1024)
        try:
        	data = json.loads(data)
        	response = eval("self._%s(data)" % data['operation'])
	    except TypeError, ValueError, KeyError:
        	response = INVALID_REQUEST_ERROR
        except AttributeError:
        	response = INVALID_OPERATION_ERROR
        finally:
	    	self.request.sendall(response)

	def _authorize(self, data=None):
		client = JanuBoxClient()
	    client.addr, client.ip = self.request.getpeername()
		try:
	    	JBSRequestHandler.clients.index(client)
	    	return ALREADY_AUTHORIZED_WARNING
	    except ValueError:
	    	if data is None:
	    		return False
	    	else:
	    		try:
	    			user = JanuBoxDB.get_authorization(data['data'])
	    			if user:
	    				client.user = user
	    				JanuBoxServer.clients.append(client)
	    				return AUTHORIZATION_SUCESS_WARNING
	    			else:
	    				return False
	    		except:
	    			return False

	def _add_file(self, data):
		if self._authorize():
			if JanuBoxDB.add_file(data['file_uri'], data['base_directory'], data['data']):
				self._send_broadcast(data)
			else:
"""
