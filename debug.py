from QueryBuilder import QueryBuilder
import QueryConstants
import DataTypes

if __name__ == '__main__':
	builder = QueryBuilder()
	q = builder.setTableName('test')\
	.setAction(QueryConstants.ACTION_CREATE_TABLE)\
	.setKVMap({'1':DataTypes.MYSQL_TXT,'b':[DataTypes.MYSQL_FLOAT(1,4),'AUTO INCREMENT']})\
	.create()
	query = builder.setTableName('qqq')\
			.setAction(QueryConstants.ACTION_INSERT)\
			.setKVMap({'col1':1,'col2':2,'col3':3})\
			.create()
	qq = builder.setTableName('t1')\
	.setAction('select')\
	.setSelectDistinct(True)\
	.setwhereArgs([{'a':1},'and','col','between',{1,10}])\
	.setSelectOrder('colnames')\
	.setSelectLimit(10)\
	.create()

	print(query)
	print(qq)
	# print(DataTypes.MYSQL_FLOAT(1,3))