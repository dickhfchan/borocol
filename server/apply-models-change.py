from config import keyspace, host, debug, api_port
import models

connection.setup([host], keyspace)
models.sync_tables()
