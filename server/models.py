from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table as sync_table
from cassandra.cqlengine.models import Model
from flask_login import UserMixin

class key_value(Model):

    id      = columns.UUID(required=True, primary_key=True)

    key      = columns.Text(required=False, index=True, )

    value      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class user(Model, UserMixin):
    hidden = ['password']

    id      = columns.UUID(required=True, primary_key=True)

    password      = columns.Bytes(required=False, index=True, )

    privacy      = columns.Text(required=False, index=True, )

    email      = columns.Text(required=False, index=True, )

    user_type      = columns.Text(required=False, index=True, )

    email_confirmed      = columns.Boolean(required=False, index=True, )

    profile_completed      = columns.Boolean(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class course_subscriptions(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, index=True, )

    course_id      = columns.Text(required=False, index=True, )

    require_accomodation      = columns.Text(required=False, index=True, )

    require_insurance      = columns.Text(required=False, index=True, )

    payment_details      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class school_profile(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, index=True, )

    status      = columns.Text(required=False, index=True, )

    contact_persons      = columns.Text(required=False, index=True, )

    school_name      = columns.Text(required=False, index=True, )

    registration_document      = columns.Text(required=False, index=True, )

    stripe_details      = columns.Text(required=False, index=True, )

    address1      = columns.Text(required=False, index=True, )

    address2      = columns.Text(required=False, index=True, )

    city      = columns.Text(required=False, index=True, )

    country      = columns.Text(required=False, index=True, )

    introduction      = columns.Text(required=False, index=True, )

    logo      = columns.Text(required=False, index=True, )

    school_photos      = columns.Text(required=False, index=True, )

    subscriptions      = columns.Text(required=False, index=True, )

    website      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class student_profile(Model):

    id      = columns.UUID(required=True, primary_key=True)
    user_id      = columns.Text(required=False, index=True, )
    status      = columns.Text(required=False, index=True, )
    currency      = columns.Text(required=False, index=True, )
    language      = columns.Text(required=False, index=True, )
    liked_courses      = columns.Text(required=False, index=True, )

    # in student profile form
    avatar = columns.Text(required=False, index=True, )
    first_name = columns.Text(required=False, index=True, )
    middle_name = columns.Text(required=False, index=True, )
    last_name = columns.Text(required=False, index=True, )
    gender = columns.Text(required=False, index=True, )
    birthday = columns.DateTime(required=False, index=True, )
    nationality = columns.Text(required=False, index=True, )
    country_of_residence = columns.Text(required=False, index=True, )
    email = columns.Text(required=False, index=True, )
    phone = columns.Text(required=False, index=True, )
    passport_info = columns.Text(required=False, index=True, )
    emergency_contact_person = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class course_detail(Model):
    fileFields = ['instructor_photo', 'cover', 'photos']

    id      = columns.UUID(required=True, primary_key=True)
    school_id      = columns.Text(required=False, index=True, )

    name = columns.Text(required=True, index=True, )
    category_id = columns.Text(required=True, index=True, )
    level = columns.Text(required=True, index=True, )
    start_date = columns.DateTime(required=True, index=True, )
    end_date = columns.DateTime(required=True, index=True, )
    description = columns.Text(required=False, index=True, )
    group_size = columns.Integer(required=True, index=True, )
    gender = columns.Text(required=False, index=True, )
    age_range = columns.List(columns.Integer, required=False, index=True, )
    hours = columns.Integer(required=True, index=True, )
    language = columns.Text(required=True, index=True, )
    instructor_photo = columns.Text(required=False, index=True, )
    instructor_info = columns.Text(required=False, index=True, )
    issue_certificate = columns.Boolean(required=True, index=True, )
    certificate = columns.Text(required=False, index=True, )
    address = columns.Text(required=True, index=True, )
    city = columns.Text(required=True, index=True, )
    country = columns.Text(required=True, index=True, )
    api_key = columns.Text(required=True, index=True, )
    location_description = columns.Text(required=False, index=True, )
    how_to_get_there = columns.Text(required=False, index=True, )
    where_to_meet = columns.Text(required=False, index=True, )
    schedule = columns.Text(required=True, index=True, )
    meals_included = columns.Boolean(required=True, index=True, )
    meals = columns.List(columns.Text, required=False, index=True, )
    meals_info = columns.Text(required=False, index=True, )
    provide = columns.Text(required=False, index=True, )
    guest_needs_to_bring = columns.Text(required=False, index=True, )
    guest_requirement = columns.Text(required=False, index=True, )
    request_form_existed = columns.Boolean(required=True, index=True, )
    request_form = columns.Text(required=False, index=True, )
    tags = columns.List(columns.Text, required=False, index=True, )
    cover = columns.Text(required=True, index=True, )
    photos = columns.List(columns.Text, required=True, index=True, )
    notes = columns.Text(required=False, index=True, )
    seats = columns.Integer(required=True, index=True, )
    price = columns.Decimal(required=True, index=True, )
    registration_start_date = columns.DateTime(required=True, index=True, )
    registration_end_date = columns.DateTime(required=True, index=True, )
    early_bird_discount = columns.Boolean(required=False, index=True, )
    discount_rate = columns.Text(required=False, index=True, )
    quota = columns.Text(required=False, index=True, )
    down_payment = columns.Boolean(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class accomodation_detail(Model):
    fileFields = ['photos']

    id      = columns.UUID(required=True, primary_key=True)
    course_id      = columns.Text(required=False, index=True, )

    options = columns.List(columns.Text, required=False, index=True, )
    other_options = columns.Text(required=False, index=True, )
    location_description = columns.Text(required=False, index=True, )
    facilities = columns.List(columns.Text, required=False, index=True, )
    other_facilities = columns.Text(required=False, index=True, )
    photos = columns.List(columns.Text, required=False, index=True, )
    room1_enabled = columns.Boolean(required=False, index=True, )
    room1_type = columns.Text(required=False, index=True, )
    room1_quota = columns.Text(required=False, index=True, )
    room1_price = columns.Text(required=False, index=True, )
    room2_enabled = columns.Boolean(required=False, index=True, )
    room2_type = columns.Text(required=False, index=True, )
    room2_quota = columns.Text(required=False, index=True, )
    room2_price = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class visa_detail(Model):

    id      = columns.UUID(required=True, primary_key=True)

    course_id      = columns.Text(required=False, index=True, )

    information      = columns.Text(required=False, index=True, )

    last_date_submission      = columns.Text(required=False, index=True, )

    document_description      = columns.Text(required=False, index=True, )

    visa_url      = columns.Text(required=False, index=True, )

    schooli_invitation_letter      = columns.Text(required=False, index=True, )

    refund_policy      = columns.Text(required=False, index=True, )

    auto_reply_message      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class featured_course(Model):

    id      = columns.UUID(required=True, primary_key=True)

    course_id      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class reviews(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.Text(required=False, index=True, )

    course_id      = columns.Text(required=False, index=True, )

    ratings      = columns.Text(required=False, index=True, )

    comments      = columns.Text(required=False, index=True, )

    photos      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class course_types(Model):

    id      = columns.UUID(required=True, primary_key=True)

    name      = columns.Text(required=False, index=True, )

    type      = columns.Text(required=False, index=True, )

    description      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

class test(Model):

    id      = columns.UUID(required=True, primary_key=True)
    ls      = columns.List(columns.Text, required=False, index=True, )
    lsi      = columns.List(columns.Integer, required=False, index=True, )
    dm      = columns.Decimal(required=False, index=True, )

    created_at = columns.DateTime(index=True, )
    updated_at = columns.DateTime(index=True, )

# this func will auto create tables
# coonect database before do this
def sync_tables():

  sync_table(user)

  sync_table(course_subscriptions)

  sync_table(school_profile)

  sync_table(student_profile)

  sync_table(course_detail)

  sync_table(accomodation_detail)

  sync_table(visa_detail)

  sync_table(featured_course)

  sync_table(reviews)

  sync_table(course_types)

  sync_table(test)
