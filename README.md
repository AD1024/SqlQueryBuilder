# SqlQueryBuilder
A SQL query builder written in Python3

# Usage:
```python
from QueryBuilder import QueryBuilder
import QueryConstants
import DataTypes
```

## Action Param:
This parameter will tell the builder which type of query to build.
Current version support:

1. SELECT (QueryConstants.ACTION_SELECT)
2. INSERT (QueryConstants.ACTION_INSERT)
3. UPDATE (QueryConstants.ACTION_UPDATE)
4. DELETE (QueryConstants.ACTION_DELETE)
5. CREATE TABLE (QueryConstants.ACTION_CREATE_TABLE)



## WHERE statment

WHERE statment is presented in *WhereArgs* is a *list* and it need to be written in following format:
Provide that we use zero indexing, the value in even indices need to be a dictionary whose keys are column names and values are the value that you want to pass to the where statment. And odd indices are logic keywords(AND OR NOT), they can be written either in upper case or in lower case. Additionally, you can just use the first letter of those words to represent them. 

**Example:**

```python
builder.setwhereArgs([{'color':'red'},'A',{'type':'C'},'O',{'year':1999}])
```

WhereArgs support using *BETWEEN* and *IN*. If you want to use *IN* keyword to specify the filter:

```python
builder.setwhereArgs([<colname>,'in',[value1,value2,...]])
```

And if you want to use *BETWEEN* keyword:

```python
builder.setwhereArgs([<colname>,'between',{lowerbound,upperbound}])
```

However, this statment does not follows the rule presented above.

If you want to include *IN* or *BETWEEN* keyword:

```python
builder.setwhereArgs([{'color':'red'},'O','color','in',['green','blue','yellow'],'A','level','between',{10,50}])
```

If you want to add parenthesis in *WHERE* statment, you can simply put them in a Tuple, and they can be nesting.

**Example:**

```python
builder.setwhereArgs([('N',{'color':'red'},'A',('N',({'a':3},'O',{'b':4})),'A',{'GENDER':'M'})])
```

## **SELECT** statment

QueryBuilder will accept SELECT statment. You just need to pass where statment(optional) to the builder instance and run **create()** method

### Example:

```python
builder = QueryBuilder()
builder.setTableName('test')\
		.setAction(QueryConstants.ACTION_SELECT)\
		.setwhereArgs([{'FirstName':'Mike'},'and', {'Gender':'M'}])\
		.create()
```

Also, **SELECT** statment can set *Order rules* , *Limit rules* and *Dictinct rule* by using:
```python
builder.setSelectLimit(<int>)
builder.setSelectDistinct(<bool>)
builder.setSelectOrder(<colname>)
```




## **INSERT** statment
If you want to create an INSERT statment with this builder, values are required to be provided to the builder and the column names are optional. However, if you are considering to pass both column names and values, the length of two list is required to be exactly the same.

**Example:**

```python
builder = QueryBuilder()
query = builder.setTableName('qqq')\
		.setAction(QueryConstants.ACTION_INSERT)\
		.setParams(['col1','col2','col3'])\
		.setValues([1,2,3])\
		.create()
```

Also, you can use dictionary to pass these values to the builder:

```python
query = builder.setTableName('qqq')\
		.setAction(QueryConstants.ACTION_INSERT)\
		.setKVMap({'col1':1,'col2':2,'col3':3})\
		.create()
```

*KVMap* is a dictionary, whose keys are column names and values are values of those columns

## UPDATE Statement

Update statment is similar to *INSERT* statment. The only difference is that **setParams()** will tell the builder which columns are needed to be changed and **setValues()** will tell the builder what value you want them to maintain.

**Example:**

```python
builder.setTableName('test')\
	   .setAction(QueryConstants.ACTION_UPDATE)\
	   .setParams(['col1','col2','col3'])\
	   .setValues([1,2,3])\
	   .setwhereArgs([{'col1':0},'O',{'col2':10}])\  # WHERE statment is optional
	   .create()
```

Similarly, **UPDATE** statment support using dictionary to pass your parameters:

```python
builder.setTableName('test')\
	   .setAction(QueryConstants.ACTION_UPDATE)\
	   .setKVMap({'col1':1,'col2':2,'col3':3})\
	   .setwhereArgs([{'col1':0},'O',{'col2':10}])\  # WHERE statment is optional
	   .create()
```

## DELETE statment

Delete statment is much more simple, because you only need to specify *WHERE* statment. The usage is the same with *SELECT* statment.

**Example:**

```python
builder.setTableName('test')\
	   .setAction(QueryConstants.ACTION_DELETE)\
	   .setwhereArgs('N',{'col1':1},'A',{'col2':2})\
	   .create()
```

## CREATE TABLE Statment

