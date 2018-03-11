from cassandra.cqlengine import connection

def sync_materialized_view(mv):
    viewName = getattr(mv, 'view_name', mv.__name__)
    partitionKeys = mv.partition_keys
    primaryKeys = getattr(mv, 'primary_keys', None)
    basePrimaryKeys = getattr(mv, 'base_primary_keys', ['id'])
    baseTableName = getattr(mv, 'base_table_name', None)
    if not baseTableName:
        baseTableName = viewName.split('_by_')[0]
    cols = mv._defined_columns # key is col name
    select = ','.join(colName for colName in cols)
    where = ' AND '.join('%s IS NOT NULL'%(key) for key in partitionKeys)
    primary = ['(%s)'%(','.join(partitionKeys))]
    if primaryKeys:
        primary.append(','.join(primaryKeys))
    primary.append(','.join(basePrimaryKeys))
    from cassandra.cqlengine import models
    keyspace = models.DEFAULT_KEYSPACE
    connection.execute('use %s;'%(keyspace))
    connection.execute('DROP MATERIALIZED VIEW IF EXISTS %s;'%(viewName))
    cql = """
CREATE MATERIALIZED VIEW %s AS
  SELECT %s FROM %s
  WHERE %s
PRIMARY KEY (%s);
"""%(viewName, select, baseTableName, where, ','.join(primary))
    connection.execute(cql)
