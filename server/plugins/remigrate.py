# recreate database
import config
from cassandra.cqlengine import connection
import models

print('remigrate start')
connection.execute('DROP KEYSPACE IF EXISTS %s;'%(config.db_keyspace))
connection.execute("CREATE KEYSPACE %s WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};"%(config.db_keyspace))
models.sync_tables_and_materialized_views()
print('remigrate end')