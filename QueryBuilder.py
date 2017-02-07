'''
	Exceptions
'''
import QueryConstants
import DataTypes

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
		self.pvMap = {} # values and column names
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

	def setKVMap(self, dic):
		self.pvMap = dic
		return self

	def setwhereArgs(self, where):
		self.whereArgs = where
		return self

	def setTableName(self, name):
		self.tableName = name
		return self

	'''
	@return data type of var
	Note: this method is not used for determining database type
	'''
	def getType(self, var):
		if isinstance(var, str):
			return 'str'
		elif isinstance(var, int):
			return 'int'
		elif isinstance(var, float):
			return 'float'
		elif isinstance(var, list):
			return 'list'
		elif isinstance(var, dict):
			return 'dict'
		elif isinstance(var, set):
			return 'set'

	'''
	@param dict where statment dictionary
	@return where statment
	'''
	def parseWhereStatment(self, dic):
		if len(dic) == 0:
			return ''
		s = 'where '
		for i in self.whereArgs:
			if self.getType(i) == 'dict':
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
				if i == 'and' or i == 'AND' or i =='a' or i =='A':
					s += 'AND'
				elif i == 'or' or i == 'OR' or i == 'o' or i == 'O':
					s += 'OR'
				elif i == 'not' or i == 'NOT' or i == 'n' or i == 'N':
					s += 'NOT'
			s += ' '
		return s


	'''
	 Check avability of column names and values
	'''
	def checkParam(self):
	# If the number of columns and values mismatched then raise exception
		if len(self.pvMap) != 0:
			return True
		if len(self.params) != len(self.values) \
						or (len(self.values) == 0 and len(self.params) == 0):
			return False
		else:
			return True

	'''
		Parse dictionary to lists
	'''
	def parseParams(self):
		self.values = []
		self.params = []
		for i in self.pvMap:
			self.params.append(i)
			self.values.append(self.pvMap[i])

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
			if len(self.pvMap) != 0:
				self.parseParams()

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
					# Parse column names
					query += str(i) + ','
				query = query[0:len(query)-1]
				query += ') '
				query += 'VALUES('
				for i in self.values: # Parse values
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

			if len(self.pvMap) != 0: 
				# If the value dictionary is set, use dictionary except raw data
				self.parseParams()

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
			# DELETE action
			query += 'DELETE FROM ' + self.tableName + ' '
			query += self.parseWhereStatment(self.whereArgs)
			return query
		elif self.action == 'select' or self.action == QueryConstants.ACTION_SELECT:
			# SELECT action
			query += 'SELECT * FROM ' + self.tableName + ' '
			query += self.parseWhereStatment(self.whereArgs)
			return query
		elif self.action == 'create table' \
				or self.action == QueryConstants.ACTION_CREATE_TABLE:
			query += QueryConstants.ACTION_CREATE_TABLE + ' ' + self.tableName + '\n(\n'
			if len(self.pvMap) != 0:
				self.parseParams()
			if not self.checkParam():
				raise ParamValueNotMatchException()
				return ''
			for i in range(0,len(self.params)):
				k = self.params[i]
				v = self.values[i]
				query += k + ' '
				if self.getType(v) == 'list':
					for j in v:
						query += j + ' '
					query = query[0:len(query)-1]
				else:
					query += v
				query += ',\n'
			query += ')'
			return query

		