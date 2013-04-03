import json
from flask import Flask, request
from flask.ext.restful import Resource
from janubox.server.messages import *
from janubox.server.database import JanuBoxDB

class Authorize(Resource):
	def get(self, login, password):
		pass

class File(Resource):
	def get(self):
		pass

	def post(self):
		pass

	def put(self):
		pass

	def delete(self):
		pass

class BaseDirectory(Resource):
	def get(self):
		pass

	def post(self):
		pass

	def put(self):
		pass

	def delete(self):
		pass

class User(Resource):
	def get(self):
		pass

	def post(self):
		pass

	def put(self):
		pass

	def delete(self):
		pass


def add_resources(api):
	api.add_resource(Authorize, '/user/<string:login>/<string:password>/authorize')















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

