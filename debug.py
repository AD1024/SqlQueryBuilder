from QueryBuilder import QueryBuilder
import QueryConstants
import DataTypes

if __name__ == '__main__':
	builder = QueryBuilder()
	q = builder.setTableName('test')\
	.setAction(QueryConstants.ACTION_CREATE_TABLE)\
	.setKVMap({'1':DataTypes.MYSQL_TXT,'b':[DataTypes.MYSQL_FLOAT(1,4),'AUTO INCREMENT']})\
	.create()
	print(q)
	# print(DataTypes.MYSQL_FLOAT(1,3))