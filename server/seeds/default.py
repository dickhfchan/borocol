from plugins.seeder import fake, pop
import utils as ut
import models
from plugins.ResourceController import store, update
import random

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
# course
schools = []
for user in models.user.all():
    if user.user_type == 'school':
        schools.append(user)
        if len(schools) == 20:
            break
for i in range(5):
    school = fake.rand(*schools)
    with_accom = random.random() > 0.3
    data = {
        'school_id': school.id,
        #
        'with_accom': with_accom,
        #
        'start_date': fake.ts(),
        'end_date': fake.ts(),
        'category_id': fake.word(),
        'level': fake.word(),
        'title': fake.sentence(),
        #
        'gender': 'male',
        'age_range': [16,50],
        'hours': [20,50],
        'description': fake.sentence(),
        #
        'language': fake.word(),
        'instructors': [{"name":fake.name(),"phone":fake.phone(),"description":fake.paragraph(),"photo":fake.img()},{"name":None,"phone":None,"description":None,"photo":None}],
        #
        'street': fake.sentence(),
        'city': fake.word(),
        'province': fake.word(),
        'zip_code': fake.word(),
        'country': fake.country_code(),
        'api_key': fake.word(),
        'location_description': fake.sentence(),
        'how_to_get_there': fake.sentence(),
        'where_to_meet': fake.sentence(),
        #
        'schedule': fake.sentence(),
        'meals_included': random.random() > 0.5,
        'meals':  fake.randmany('breakfast', 'lunch', 'bunch', 'dinner', 'snacks'),
        'weather_arrangement': fake.sentence(),
        #
        'provide': fake.sentence(),
        'guest_needs_to_bring': fake.sentence(),
        'issue_certificate': random.random() > 0.5,
        'certificate': fake.paragraph(),
        #
        'entry_requirment': fake.paragraph(),
        'request_form_enabled': random.random() > 0.5,
        'request_form': [{"enabled":True,"value":fake.paragraph()},{"enabled":False,"value":None}],
        #
        'group_size': fake.random_int(),
        'seat_quota': fake.random_int(),
        'price': 66.66,
        #
        'early_bird': {"enabled": random.random() > 0.5,"discount": 0.2,"quota": 0.2,"end_date":fake.ts()},
        'down_payment': {"enabled": random.random() > 0.5,"discount":None,"rest":fake.paragraph()},
        #
        'cover': fake.img(),
        'photos': fake.imgs(),
        'youtube_video_link': fake.img(),
        'tags': ['Design', 'IT'],
    }
    course = store(models.course, data)
    # accomodation
    if not with_accom:
        continue
    data = {
        'course_id': course.id,
        'type': 'hotel',
        'name': fake.sentence(),
        'phone': fake.phone(),
        'address': fake.address(),
        'facilities': ['wifi', 'gym'],
        'description': fake.paragraph(),
        'photos': fake.imgs(),
        'rooms': [{"enabled":random.random() > 0.5,"type":"shared half","quota":fake.random_int(),"price":666.66},{"enabled":False,"type":"shared 3 ppl","quota":None,"price":None},{"enabled":False,"type":"private double bed","quota":None,"price":None}],
    }
    accm = store(models.accomodation, data)