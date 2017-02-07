'''
	Exceptions
'''
import QueryConstants

class ParamValueNotMatchException(Exception):
	def __init__(self, err = 'Param Values mismatch'):
		Exception.__init__(self, err)
class TableNotSetExcetion(Exception):
	def __init__(self, err = 'Table name is not set'):
		Exception.__init__(self, err)

# Major Implementation
class QueryBuilder():
	def __init__(self):
		self.action = '' # action of the query
		self.params = [] # col names
		self.values = [] # values to change
		self.whereArgs = [] # where statments: K: str, V: str or other data types
		self.tableName = None # table to alter

	def setAction(self, action):
		self.action = action
		return self

	def setParams(self, param):
		self.params = param
		return self

	def setValues(self, values):
		self.values = values
		return self

	def setwhereArgs(self, where):
		self.whereArgs = where
		return self

	def setTableName(self, name):
		self.tableName = name
		return self

	'''
	@return data type of var
	'''
	def getType(self, var):
		if isinstance(var, str):
			return 'str'
		elif isinstance(var, int):
			return 'int'
		elif isinstance(var, float):
			return 'float'

	'''
	@param dict where statment dictionary
	@return where statment
	'''
	def parseWhereStatment(self, dic):
		if len(dic) == 0:
			return ''
		s = 'where '
		for i in self.whereArgs:
			if isinstance(i, dict):
				# current item is condition dictionary
				for j in i:
					s += str(j) + '='
					v = i[j]
					if self.getType(v) == 'str':
						s += '\'' + v + '\''
					elif self.getType(v) == 'int':
						s += str(v)
					else:
						s += str(v)
			else:
				# current item is logic expression
				if i == 'and' or i == 'AND':
					s += 'AND'
				else:
					s += 'OR'
			s += ' '
		return s

	def checkParam(self):
	# If the number of columns and values mismatched then raise exception
		if len(self.params) != len(self.values) \
						or (len(self.values) == 0 and len(self.params) == 0):
			return False
		else:
			return True

	def create(self):
		query = ''
		# If there isn't a table name in the query then raise exception
		if not self.tableName or self.tableName is None:
			raise TableNotSetExcetion()
			return ''

		if self.action == 'insert' or self.action == QueryConstants.ACTION_INSERT:
			# Action Insert
			if not self.checkParam():
				raise ParamValueNotMatchException()
				return ''
			query += 'INSERT INTO ' + self.tableName + ' '
			if len(self.params) == 0:
				# There can be no column names in an insert query
				query += 'VALUES('
				for i in iter(self.values):
					query += str(i) + ','
				query = query[0:len(query)-1]
				query += ')'
				return query
			else:
				query += '('
				for i in iter(self.params):
					query += str(i) + ','
				query = query[0:len(query)-1]
				query += ') '
				query += 'VALUES('
				for i in self.values:
					if self.getType(i) == 'str':
						query += '\'' + i + '\''
					else:
						query += str(i)
					query += ','
				query = query[0:len(query)-1] + ')'
				return query
		elif self.action == 'update' or self.action == QueryConstants.ACTION_UPDATE:
			# Action update
			if not self.checkParam():
				raise ParamValueNotMatchException()
				return ''
			query += 'UPDATE ' + self.tableName + ' SET '
			for i in range(0, len(self.params)): # the length of params and values is the same
				k = self.params[i]
				v = self.values[i]
				query += str(k) + '=' + str(v) + ','
			query = query[0:len(query)-1]
			query += ' '
			if len(self.whereArgs) == 0: # if there isn't and where statment
				return query
			else:
				query += self.parseWhereStatment(self.whereArgs)		
				return query
		elif self.action == 'delete' or self.action == QueryConstants.ACTION_DELETE:
			query += 'DELETE FROM ' + self.tableName + ' '
			query += self.parseWhereStatment(self.whereArgs)
			return query
		elif self.action == 'select' or self.action == QueryConstants.ACTION_SELECT:
			query += 'select * from ' + self.tableName + ' '
			query += self.parseWhereStatment(self.whereArgs)
			return query
			

