import psycopg2
from messages import *


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

DATABASE_URI = 'postgresql+psycopg2://user:password@host:port/dbname'
database = SQLAlchemy()

class File(database.Model):
	pass

class BaseDirectory(database.Model):
	pass

class Revision(database.Model):
	pass

class Operation(database.Model):
	pass

class User(database.Model):
	pass


class JanuBoxDBError(Exception):
	pass

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
