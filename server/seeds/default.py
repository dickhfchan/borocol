from plugins.seeder import fake, pop
import utils as ut
import models
from plugins.ResourceController import store, update

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
        'passport_info' : {"number":fake.randstr(),"issued_country":fake.country_code(),"expiry_date":fake.ts()},
        'emergency_contact_persons' : [{"name":fake.name(),"relationship":"father","tel":fake.phone()},{"name":None,"relationship":None,"tel":None}],
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
        'contact_persons' : [{"last_name":fake.lstname(),"first_name":fake.fstname(),"title":'Admin',"email":fake.email(),"tel":fake.phone()},{"last_name":None,"first_name":None,"title":None,"email":None,"tel":None}],
        'registration_document' : fake.img(),
        'logo': fake.img(),
        'photos' : fake.imgs(),
    }
    profile = store(models.school_profile, data)