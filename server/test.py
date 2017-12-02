from config import keyspace, host, debug, api_port
from cassandra.cqlengine import connection
import models
import json

connection.setup([host], keyspace)

rows = models.User.objects().all()[0:20]
