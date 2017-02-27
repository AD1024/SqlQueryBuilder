AUTO_INC = 'AUTO INCREMENT'
PRIM_KEY = 'PRIMARY KEY'
# Begin Mysql data types
MYSQL_VARCHAR = 'VARCHAR(255)'
MYSQL_CHAR = 'CHAR(255)'
MYSQL_TXT = 'TEXT'
MYSQL_STXT = 'TINYTEXT'
MYSQL_BLOB = 'BLOB'
MYSQL_MTXT = 'MEDIUMTEXT'
MYSQL_MBLOB = 'MEDIUMBLOB'
MYSQL_LTXT = 'LONGTEXT'
MYSQL_LBLOB = 'LONGBLOB'

def MYSQL_ENUM(lis):
	Q += 'ENUM('
	for i in lis:
		if isinstance(i,str):
			Q += '\'' + i + '\''
		else:
			Q += str(i)
		Q += ','
	Q = Q[0:len(Q)-1] + ')'
	return Q

# MYSQL int
def MysqlcreateInt(typ,s):
	if typ == 'T':
		return 'TINYINT(' + str(s) + ')'
	elif typ == 'S':
		return 'SMALLINT(' + str(s) + ')'
	elif typ == 'M':
		return 'MEDIUMINT(' + str(s) + ')'
	elif typ == 'I':
		return 'INT(' + str(s) + ')'
	elif typ =='B':
		return 'BIGINT(' + str(s) + ')'
def MYSQL_TINT(s):
	return MysqlcreateInt('T',s)
def MYSQL_SINT(s):
	return MysqlcreateInt('S',s)
def MYSQL_MINT(s):
	return MysqlcreateInt('M',s)
def MYSQL_INT(s):
	return MysqlcreateInt('I',s)
def MYSQL_BIGINT(s):
	return MysqlcreateInt('B',s)

# Mysql float
def MysqlcreateFloat(typ, s, d):
	if typ == 'F':
		return 'FLOAT(' + str(s) + ',' + str(d) + ')'
	elif typ == 'D':
		return 'DOUBLE(' + str(s) + ',' + str(d) + ')'
	elif typ == 'DE':
		return 'DECIMAL(' + str(s) + ',' + str(d) + ')'
def MYSQL_FLOAT(s, d=6):
	return MysqlcreateFloat('F',s,d)
def MYSQL_DOUBLE(s,d=6):
	return MysqlcreateFloat('D',s,d)
def MYSQL_DEC(s,d=6):
	return MysqlcreateFloat('DE',s,d)

# Mysql DateTime
MYSQL_DATE = 'DATE()'
MYSQL_TIME = 'TIME()'
MYSQL_STAMP = 'TIMESTAMP()'
MYSQL_YEAR = 'YEAR()'
# End Of Mysql Data types

# Begin SQL Server Datatypes

# SQL SERVER Chars
SQSERV_TEXT = 'text'
SQSERV_NTEXT = 'ntext'

def SqlServCreateChar(typ, u, s):
	if u:
		if typ == 'C':
			return 'char(' + str(s) + ')'
		elif typ == 'vc':
			return 'varchar(' + str(s) + ')'
	else:
		if typ == 'C':
			return 'nchar(' + str(s) + ')'
		elif typ == 'vc':
			return 'nvarchar(' + str(s) +')'
def SQSERV_CHAR(s):
	return SqlServCreateChar('C',True,s)
def SQSERV_VARCHAR(s):
	return SqlServCreateChar('vc',True,s)
def SQSERV_NCHAR(s):
	return SqlServCreateChar('C',False,s)
def SQSERV_NVARCHAR(s):
	return SqlServCreateChar('vc',False,s)

# SQLSERVER Binary
SQSERV_BIT = 'bit'
SQSERV_IMG = 'image'
def SqlServerCreateBin(typ, s):
	if typ == 'B':
		return 'binary(' + str(s) + ')'
	elif typ == 'VB':
		return 'varbinary(' + str(s) + ')'

def SQLSERV_BIN(s):
	return SqlServerCreateBin('B',s)
def SQLSERV_VARBIN(s):
	return SqlServerCreateBin('VB',s)

# SQLSERVER int and float
SQSERV_TINT = 'tinyint'
SQLSERV_SINT = 'smallint'
SQLSERV_INT = 'int'
SQSERV_BINT = 'bigint'
SQSERV_SMONEY = 'smallmoney'
SQSERV_MONEY = 'money'
SQSERV_REAL = 'real'
def SQSERV_DEC(p,s):
	return 'decimal(' + str(p) + ',' + str(s) + ')'
def SQSERV_NUM(p,s):
	return 'numeric(' + str(p) + ',' + str(s) + ')'

def SQSERV_FLOAT(d):
	return 'float(' + str(d) + ')'

# SQlServer DateTime
SQSERV_DATETIME = 'datetime'
SQSERV_DATETIME2 = 'datetime2'
SQSERV_SDATETIME = 'smalldatetime'
SQSERV_DATE = 'date'
SQSERV_TIME = 'time'
SQSERV_DATETIMEOFF = 'datetimeoffset'
SQSERV_STAMP = 'timestamp'
#end of SQl server data types
