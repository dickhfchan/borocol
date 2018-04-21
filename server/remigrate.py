# recreate database

from config import db_keyspace, db_host
import config
from cassandra.cqlengine import connection
import models
connection.setup([db_host], db_keyspace, lazy_connect=True)

connection.execute('DROP KEYSPACE IF EXISTS %s;'%(config.db_keyspace))
connection.execute("CREATE KEYSPACE %s WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};"%(config.db_keyspace))
models.sync_tables_and_materialized_views()