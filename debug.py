from QueryBuilder import QueryBuilder
import QueryConstants
import DataTypes

if __name__ == '__main__':
	builder = QueryBuilder()
	'''
	q = builder.setTableName('test')\
	.setAction(QueryConstants.ACTION_CREATE_TABLE)\
	.setKVMap({'1':DataTypes.MYSQL_TXT,'b':[DataTypes.MYSQL_FLOAT(1,4),'AUTO INCREMENT']})\
	.create()
	query = builder.setTableName('test')\
	   .setAction(QueryConstants.ACTION_DELETE)\
	   .setwhereArgs([('N',{'color':'red'},'A',('N',({'a':3},'O',{'b':4})),'A',{'GENDER':'M'})])\
	   .create()
	qq = builder.setTableName('test')\
		.setAction(QueryConstants.ACTION_UPDATE)\
		.setKVMap({'col1':1,'col2':2,'col3':3})\
		.setwhereArgs([{'col1':0},'O',{'col2':10}])\
		.create()

	insertQueryTest = builder.setTableName('Test')\
                .setKVMap({'col1':1, 'col2': 2, 'name':'Mike He'})\
                .setAction(QueryConstants.ACTION_INSERT)\
                .create()
	print(insertQueryTest)
	q1 = builder.setTableName('T')\
				.setAction(QueryConstants.ACTION_SELECT)\
				.setwhereArgs([{'col1':1},'A',{'col2':2},'O',{'name':'hdy'}])\
                .create()
    '''
	query = builder.setAction(QueryConstants.ACTION_CREATE_TABLE)\
        .setTableName('TableTest')\
        .setKVMap({'col1':DataTypes.MYSQL_TXT, 'col2':DataTypes.MYSQL_INT(1024),'UserName': DataTypes.MYSQL_STXT})\
        .create()
	print(query)
        
	qq = builder.setAction(QueryConstants.ACTION_DROP_TABLE)\
				.setTableName("Drop Test")\
				.create()
	print(qq)
	# print(qq)
	# print(DataTypes.MYSQL_FLOAT(1,3))

