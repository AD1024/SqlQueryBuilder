# SqlQueryBuilder
A SQL query builder written in Python3

# Usage:
	import QueryBuilder
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
	Builder = QueryBuilder
	Builder.setAction(QueryConstants.ACTION_SELECT)
	Builder.setWhereArgs([{'FirstName':'Mike'},'and', 'Gender':'M'])
	Builder.create()

#### About WhereArgs
WhereArgs is a *list* and it need to be written in following format:
Provide that we use zero indexing, the value in even index need to be a dictionary, keys are column names and values are the value you want to pass to the where statment.

## **INSERT** statment
If you want to create an INSERT statment with this builder, values are required to be provided to the builder and the column names are optional. However, if you are considering to pass both column names and values, the length of two list is required to be exactly the same.(column names and values are two lists and in later version might be changed to dictionary)

TO BE CONTINUED