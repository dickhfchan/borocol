from config import keyspace, host, debug, api_port
from cassandra.cqlengine import connection
import models
import json
from utils import toDict
connection.setup([host], keyspace)

rows = models.User.objects().all()[0:20]
row = rows[0]
