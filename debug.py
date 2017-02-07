from QueryBuilder import QueryBuilder
import QueryConstants

if __name__ == '__main__':
	builder = QueryBuilder()
	q = builder.setTableName('test')\
	.setAction('update')\
	.setValues([1,2,3])\
	.setParams(['a','b','c'])\
	.setwhereArgs([{'a':1},'and',{'b':'2'},'or',{'c':3}])\
	.create()
	print(q)