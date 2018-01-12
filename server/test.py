from config import db_keyspace, db_host
from cassandra.cqlengine import connection
from cassandra import util
import models
import time

connection.setup([db_host], db_keyspace, lazy_connect=True)
models.sync_tables()

# models.test.objects.all().delete()
# models.test.create(id = util.uuid_from_time(time.time()),
# dm = 233.33
# )
# print(models.test.objects.all()[0:9])
# uuid.UUID'>
# <class 'decimal.Decimal'>
# <class 'uuid.UUID'>
# <class 'NoneType'>
# <class 'uuid.UUID'>
# <class 'decimal.Decimal'>
# <class 'uuid.UUID'>
# <class 'NoneType'>
# <class 'uuid.UUID'>
# <class 'NoneType'>
# <class 'uuid.UUID'>
# <class 'NoneType'>
# datetime.datetime
