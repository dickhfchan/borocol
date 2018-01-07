from config import keyspace, db_host
import models

connection.setup([db_host], keyspace)
models.sync_tables()
