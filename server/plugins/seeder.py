# insert test data into databse
from cassandra.cqlengine import connection
from utils import str_rand, dt2ts
import random
from datetime import datetime
from dateutil import parser as datetimeParser
from faker import Faker
fake = Faker()
from faker.providers import BaseProvider
import importlib

class MyFakeProvider(BaseProvider):
    def rand(self, *ls):
        n = random.randint(0, len(ls) - 1)
        return ls[n]
    def randmany(self, *ls, min = 0):
        total = random.randint(min, len(ls))
        r = []
        for i in range(total):
            n = random.randint(0, len(ls) - 1)
            val = ls[n]
            if val not in r:
                r.append(val)
        return r
    def randstr(self, *a, **b):
        return str_rand(*a, **b)
    def gender(self):
        return self.rand('male', 'female')
    # custom country code
    def ctcd(self):
        return self.rand('US', 'GB')
    def img(self, w=200, h=200, id=None):
        return 'https://picsum.photos/%s/%s?image=%s'%(w, h, id or random.randint(1, 1000))
    def imgs(self, n = None, *a, **b):
        if not n:
            n = random.randint(2,6)
        return [self.img(*a, **b) for i in range(n)]
    def dt(self):
        return datetimeParser.parse(fake.date() + ' ' + fake.time())
    # timestamp
    def ts(self):
        return dt2ts(self.dt())
    def fstname(self):
        return fake.first_name()
    def lstname(self):
        return fake.last_name()
    def mdname(self):
        return fake.lstname()
    def phone(self):
        return '+1 ' + str(random.randint(100000, 999999))
fake.add_provider(MyFakeProvider)

# 
import utils as ut
def pop(ls):
    if len(ls):
        return ls.pop(0)
    return None
def execute(pt):
    print('seed start')
    importlib.import_module(pt)
    print('seed end')