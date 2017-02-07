# SqlQueryBuilder
A SQL query builder written in Python3

# Usage:
	from QueryBuilder import QueryBuilder
	import QueryConstants
	import DataTypes

## Action Param:
This parameter will tell the builder which type of query to build.
Current version support:

1. SELECT

2. INSERT

3. UPDATE

4. DELETE

## **SELECT** statment
QueryBuilder will accept SELECT statment. You just need to pass where statment(optional) to the builder instance and run **create()** method

### Example:

	builder = QueryBuilder()
	builder.setTableName('test')\
			.setAction(QueryConstants.ACTION_SELECT)\
			.setwhereArgs([{'FirstName':'Mike'},'and', {'Gender':'M'}])\
			.create()

Also, **SELECT** statment can set *Order rules* , *Limit rules* and *Dictinct rule* by using:
	builder.setSelectLimit(<int>)
	builder.setSelectDistinct(<bool>)
	builder.setSelectOrder(<colname>)

#### About WhereArgs
WhereArgs is a *list* and it need to be written in following format:
Provide that we use zero indexing, the value in even index need to be a dictionary, keys are column names and values are the value you want to pass to the where statment. And WhereArgs support using *BETWEEN* and *IN*. If you want to use *IN* keyword to specify the filter:

	builder.setwhereArgs([<colname>,'in',[value1,value2,...]])

And if you want to use *BETWEEN* keyword:

	builder.setwhereArgs([<colname>,'between',{lowerbound,upperbound}])

## **INSERT** statment
If you want to create an INSERT statment with this builder, values are required to be provided to the builder and the column names are optional. However, if you are considering to pass both column names and values, the length of two list is required to be exactly the same.

**Example:**

	builder = QueryBuilder()
	query = builder.setTableName('qqq')\
			.setAction(QueryConstants.ACTION_INSERT)\
			.setParams(['col1','col2','col3'])\
			.setValues([1,2,3])\
			.create()

Also, you can use dictionary to pass these values to the builder:
	query = builder.setTableName('qqq')\
			.setAction(QueryConstants.ACTION_INSERT)\
			.setKVMap({'col1':1,'col2':2,'col3':3})
			.create()