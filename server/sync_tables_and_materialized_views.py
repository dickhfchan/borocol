from config import db_keyspace, db_host
from cassandra.cqlengine import connection
import models

connection.setup([db_host], db_keyspace, lazy_connect=True)
models.sync_tables_and_materialized_views()
