from QueryBuilder import QueryBuilder
import QueryConstants

if __name__ == '__main__':
	builder = QueryBuilder()
	builder.setTableName('test')
	builder.setAction('update')
	# [{},'and',{},'or']
	builder.setParams(['a','cc','vv'])
	builder.setValues([1,2,3])
	builder.setwhereArgs([{'a':1},'and',{'b':'2'},'or',{'c':3}])
	q = builder.create()
	print(q)