from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table as sync_table
from cassandra.cqlengine.models import Model
from flask_login import UserMixin

class key_value(Model):

    id      = columns.UUID(required=True, primary_key=True)

    key      = columns.Text(required=False, primary_key=True, )

    value      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class user(Model, UserMixin):
    hidden = ['password']

    id      = columns.UUID(required=True, primary_key=True)

    password      = columns.Bytes(required=False, primary_key=True, )

    privacy      = columns.Text(required=False, primary_key=True, )

    email      = columns.Text(required=False, primary_key=True, )

    user_type      = columns.Text(required=False, primary_key=True, )

    email_confirmed      = columns.Boolean(required=False, primary_key=True, default=False)

    profile_completed      = columns.Boolean(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class activation_email(Model):
    hidden = ['password']

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.UUID(required=False, primary_key=True, )

    email      = columns.Text(required=False, primary_key=True, )

    token      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class course_subscriptions(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.UUID(required=False, primary_key=True, )

    course_id      = columns.UUID(required=False, primary_key=True, )

    require_accomodation      = columns.Text(required=False, primary_key=True, )

    require_insurance      = columns.Text(required=False, primary_key=True, )

    payment_details      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class school_profile(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.UUID(required=False, primary_key=True, )

    status      = columns.Text(required=False, primary_key=True, )

    contact_persons      = columns.Text(required=False, primary_key=True, )

    school_name      = columns.Text(required=False, primary_key=True, )

    registration_document      = columns.Text(required=False, primary_key=True, )

    stripe_details      = columns.Text(required=False, primary_key=True, )

    address1      = columns.Text(required=False, primary_key=True, )

    address2      = columns.Text(required=False, primary_key=True, )

    city      = columns.Text(required=False, primary_key=True, )

    country      = columns.Text(required=False, primary_key=True, )

    introduction      = columns.Text(required=False, primary_key=True, )

    logo      = columns.Text(required=False, primary_key=True, )

    school_photos      = columns.Text(required=False, primary_key=True, )

    subscriptions      = columns.Text(required=False, primary_key=True, )

    website      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class student_profile(Model):

    id      = columns.UUID(required=True, primary_key=True)
    user_id      = columns.UUID(required=False, primary_key=True, )
    status      = columns.Text(required=False, primary_key=True, )
    currency      = columns.Text(required=False, primary_key=True, )
    language      = columns.Text(required=False, primary_key=True, )
    liked_courses      = columns.Text(required=False, primary_key=True, )

    # in student profile form
    avatar = columns.Text(required=False, primary_key=True, )
    first_name = columns.Text(required=False, primary_key=True, )
    middle_name = columns.Text(required=False, primary_key=True, )
    last_name = columns.Text(required=False, primary_key=True, )
    gender = columns.Text(required=False, primary_key=True, )
    birthday = columns.DateTime(required=False, primary_key=True, )
    nationality = columns.Text(required=False, primary_key=True, )
    country_of_residence = columns.Text(required=False, primary_key=True, )
    email = columns.Text(required=False, primary_key=True, )
    phone = columns.Text(required=False, primary_key=True, )
    passport_info = columns.Text(required=False, primary_key=True, )
    emergency_contact_person = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class course_detail(Model):
    fileFields = ['instructor_photo', 'cover', 'photos']

    id      = columns.UUID(required=True, primary_key=True)
    school_id      = columns.UUID(required=False, primary_key=True, )

    name = columns.Text(required=True, primary_key=True, )
    category_id = columns.Text(required=True, primary_key=True, )
    level = columns.Text(required=True, primary_key=True, )
    start_date = columns.DateTime(required=True, primary_key=True, )
    end_date = columns.DateTime(required=True, primary_key=True, )
    description = columns.Text(required=False, primary_key=True, )
    group_size = columns.Integer(required=True, primary_key=True, )
    gender = columns.Text(required=False, primary_key=True, )
    age_range = columns.List(columns.Integer, required=False, )
    hours = columns.Integer(required=True, primary_key=True, )
    language = columns.Text(required=True, primary_key=True, )
    instructor_photo = columns.Text(required=False, primary_key=True, )
    instructor_info = columns.Text(required=False, primary_key=True, )
    issue_certificate = columns.Boolean(required=True, primary_key=True, )
    certificate = columns.Text(required=False, primary_key=True, )
    address = columns.Text(required=True, primary_key=True, )
    city = columns.Text(required=True, primary_key=True, )
    country = columns.Text(required=True, primary_key=True, )
    api_key = columns.Text(required=True, primary_key=True, )
    location_description = columns.Text(required=False, primary_key=True, )
    how_to_get_there = columns.Text(required=False, primary_key=True, )
    where_to_meet = columns.Text(required=False, primary_key=True, )
    schedule = columns.Text(required=True, primary_key=True, )
    meals_included = columns.Boolean(required=True, primary_key=True, )
    meals = columns.List(columns.Text, required=False, )
    meals_info = columns.Text(required=False, primary_key=True, )
    provide = columns.Text(required=False, primary_key=True, )
    guest_needs_to_bring = columns.Text(required=False, primary_key=True, )
    guest_requirement = columns.Text(required=False, primary_key=True, )
    request_form_existed = columns.Boolean(required=True, primary_key=True, )
    request_form = columns.Text(required=False, primary_key=True, )
    tags = columns.List(columns.Text, required=False, )
    cover = columns.Text(required=True, primary_key=True, )
    photos = columns.List(columns.Text, required=True, )
    notes = columns.Text(required=False, primary_key=True, )
    seats = columns.Integer(required=True, primary_key=True, )
    price = columns.Decimal(required=True, primary_key=True, )
    registration_start_date = columns.DateTime(required=True, primary_key=True, )
    registration_end_date = columns.DateTime(required=True, primary_key=True, )
    early_bird_discount = columns.Boolean(required=False, primary_key=True, )
    discount_rate = columns.Text(required=False, primary_key=True, )
    quota = columns.Text(required=False, primary_key=True, )
    down_payment = columns.Boolean(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class accomodation_detail(Model):
    fileFields = ['photos']

    id      = columns.UUID(required=True, primary_key=True)
    course_id      = columns.UUID(required=False, primary_key=True, )

    options = columns.List(columns.Text, required=False, )
    other_options = columns.Text(required=False, primary_key=True, )
    location_description = columns.Text(required=False, primary_key=True, )
    facilities = columns.List(columns.Text, required=False, )
    other_facilities = columns.Text(required=False, primary_key=True, )
    photos = columns.List(columns.Text, required=False, )
    room1_enabled = columns.Boolean(required=False, primary_key=True, )
    room1_type = columns.Text(required=False, primary_key=True, )
    room1_quota = columns.Text(required=False, primary_key=True, )
    room1_price = columns.Text(required=False, primary_key=True, )
    room2_enabled = columns.Boolean(required=False, primary_key=True, )
    room2_type = columns.Text(required=False, primary_key=True, )
    room2_quota = columns.Text(required=False, primary_key=True, )
    room2_price = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class visa_detail(Model):

    id      = columns.UUID(required=True, primary_key=True)

    course_id      = columns.UUID(required=False, primary_key=True, )

    information      = columns.Text(required=False, primary_key=True, )

    last_date_submission      = columns.Text(required=False, primary_key=True, )

    document_description      = columns.Text(required=False, primary_key=True, )

    visa_url      = columns.Text(required=False, primary_key=True, )

    schooli_invitation_letter      = columns.Text(required=False, primary_key=True, )

    refund_policy      = columns.Text(required=False, primary_key=True, )

    auto_reply_message      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class featured_course(Model):

    id      = columns.UUID(required=True, primary_key=True)

    course_id      = columns.UUID(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class reviews(Model):

    id      = columns.UUID(required=True, primary_key=True)

    user_id      = columns.UUID(required=False, primary_key=True, )

    course_id      = columns.UUID(required=False, primary_key=True, )

    ratings      = columns.Text(required=False, primary_key=True, )

    comments      = columns.Text(required=False, primary_key=True, )

    photos      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class course_types(Model):

    id      = columns.UUID(required=True, primary_key=True)

    name      = columns.Text(required=False, primary_key=True, )

    type      = columns.Text(required=False, primary_key=True, )

    description      = columns.Text(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

class test(Model):

    id      = columns.UUID(required=True, primary_key=True)
    ls      = columns.List(columns.Text, required=False, )
    lsi      = columns.List(columns.Integer, required=False, )
    dm      = columns.Decimal(required=False, primary_key=True, )

    created_at = columns.DateTime(primary_key=True, )
    updated_at = columns.DateTime(primary_key=True, )

# this func will auto create tables
# coonect database before do this
def sync_tables():

  sync_table(user)

  sync_table(activation_email)

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
