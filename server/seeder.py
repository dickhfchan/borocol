# insert test data into databse
from cassandra.cqlengine import connection
import config
from config import db_keyspace, db_host, app_debug, app_host, app_port
import models
from utils import str_rand, dt2ts
from plugins.ResourceController import ResourceController, store, update
import random
from datetime import datetime
from dateutil import parser as datetimeParser
from faker import Faker
fake = Faker()
from faker.providers import BaseProvider
class MyFakeProvider(BaseProvider):
    def rand(self, *ls):
        n = random.randint(0, len(ls) - 1)
        return ls[n]
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


# connect databse
try:
    connection.setup([db_host], db_keyspace, lazy_connect=True)
    print("Make connection to DB lazily")
except Exception as e:
    print("Error: connection db failed")
    raise

# 
import utils as ut
def pop(ls):
    if len(ls):
        return ls.pop(0)
    return None
# student
emails = ['1@test.com', '2@test.com']
passwords = ['123456', '123456']
for i in range(5):
    data = {
        'email': pop(emails) or fake.email(),
        'password': ut.hash_pwd(pop(passwords) or fake.password()),
        'user_type': 'student',
        'email_confirmed': True,
    }
    user = store(models.user, data)
    data = {
        'user_id': user.id,
        'avatar': fake.img(),
        'first_name': fake.fstname(),
        'middle_name': fake.mdname(),
        'last_name' : fake.lstname(),
        'gender' : fake.gender(),
        'birthday': fake.ts(),
        'nationality' : fake.country_code(),
        'country_of_residence' : fake.country_code(),
        'phone' : fake.phone(),
        'passport_info' : '{"number":"%s","issued_country":"%s","expiry_date":%s}'%(str_rand(), fake.country_code(), fake.ts()),
        'emergency_contact_persons' : '[{"name":"%s","relationship":"%s","tel":"%s"},{"name":null,"relationship":null,"tel":null}]'
        %(fake.name(), 'father', fake.phone()),
    }

    profile = store(models.student_profile, data)
# school
emails = ['3@test.com', '4@test.com']
passwords = ['123456', '123456']
status = ['normal', 'normal']
for i in range(5):
    data = {
        'email': pop(emails) or fake.email(),
        'password': ut.hash_pwd(pop(passwords) or fake.password()),
        'user_type': 'school',
        'email_confirmed': True,
    }
    user = store(models.user, data)
    data = {
        'user_id': user.id,
        'status': pop(status) or fake.rand('pending', 'normal'),
        'name': fake.sentence(),
        'address': fake.address(),
        'city': fake.city(),
        'country': fake.country_code(),
        'introduction': fake.paragraph(),
        'website' : fake.url(),
        'contact_persons' : '[{"last_name":"%s","first_name":"%s","title":"%s","email":"%s","tel":"%s"},{"last_name":null,"first_name":null,"title":null,"email":null,"tel":null}]'
        %(fake.lstname(), fake.fstname(), 'Admin', fake.email(), fake.phone()),
        'registration_document' : fake.img(),
        'logo': fake.img(),
        'photos' : fake.imgs(),
    }
    profile = store(models.school_profile, data)