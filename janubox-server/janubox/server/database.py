import psycopg2
from messages import *


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

DATABASE_URI = 'postgresql+psycopg2://user:password@host:port/dbname'
database = SQLAlchemy()

class File(database.Model):
	id = db.Column(db.Integer, primary_key=True)	
	base_directory_id = db.Column(db.Integer, db.ForeignKey('base_directory.id'))
	deleted = db.Column(db.Boolean)
	uri = db.Column(db.Text)

class BaseDirectory(database.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

class Revision(database.Model):
	id = db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))
	data = db.Column(db.Text)
	commit = db.Column(db.DateTime)

class Operation(database.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

class User(database.Model):
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.Text)
	hashcode = db.Column(db.Text)
	admin = db.Column(db.Boolean)

class JanuBoxDBError(Exception):
	pass







"""
class JanuBoxDB(object):
	def __init__(self, dbname, user=None, password=None):
		self._dbname = dbname
		self._user = user
		self._password = password
		self._connect()
		self._con.close()

	def _connect(self):
		try:
			self._con = psycopg2.connect(database=self._dbname,\
						user=self._user, password=self._password)
		except psycopg2.Error:
			raise JanuBoxDBError(DB_CONNECTION_ERROR % self._dbname)

	def executeSQL(self, sql, ret_type=None):
		self._connect()
		cur = self._con.cursor()
		ret = False

		try:
			cur.execute(sql)
		except psycopg2.Error:
			self._con.rollback()
			self._con.close()
			raise JanuBoxDBError(DB_SQL_SYNTAX_ERROR % sql)

		try:
			if ret_type == 'one':
				ret = cur.fetchone()
			elif ret_type == 'all':
				ret = cur.fetchall()
			elif ret_type == 'many':
				ret = cur.fetchmany()
			elif ret_type == 'last_id':
				ret = cur.lastrowid
			elif ret_type == None:
				ret = True
			else:
				raise JanuBoxDBError(UNSUPPORTED_RET_TYPE_ERROR % ret_type)
		except sqlite.Error:
			self._con.rollback()
			self._con.close()
			raise JanuBoxDBError(DB_RET_TYPE_ERROR % (ret_type, sql))

		self._con.close()
		return ret
"""