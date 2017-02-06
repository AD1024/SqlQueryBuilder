# 开始浑浑噩噩的debug...由于我是cpp选手所以可能error无数..慢慢修

# 233 聊天解压...
# 实在抱歉，mac系统下弹幕姬比较辣鸡...没法点歌...OTZ
from queryBuilder import QueryBuilder
import QueryConstants

if __name__ == '__main__':
	builder = QueryBuilder()
	# 我不太清楚python的builder模式是不是这样子写...先试一试..
	builder.setTableName('test')
	builder.setAction('update')
	# [{},'and',{},'or']
	builder.setParams(['a','cc','vv'])
	builder.setValues([1,2,3])
	builder.setwhereArgs([{'a':1},'and',{'b':'2'},'or',{'c':3}])
	q = builder.create()
	print(q)