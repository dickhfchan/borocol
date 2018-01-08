from config import db_keyspace, db_host
import models

connection.setup([db_host], db_keyspace, lazy_connect=True)
models.sync_tables()
