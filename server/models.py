from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table as sync_table
from plugins.materializedViews import sync_materialized_view
from cassandra.cqlengine.models import Model
from flask_login import UserMixin

class key_value(Model):

    id      = columns.UUID(required=True, partition_key=True)

    key      = columns.Text(required=False, )

    value      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class user(Model, UserMixin):
    hidden = ['password']

    id      = columns.UUID(required=True, partition_key=True)

    password      = columns.Bytes(required=False, )

    privacy      = columns.Text(required=False, )

    email      = columns.Text(required=False, index=True, )

    user_type      = columns.Text(required=False, )

    email_confirmed      = columns.Boolean(required=False, default=False)

    profile_completed      = columns.Boolean(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class activation_email(Model):

    id      = columns.UUID(required=True, partition_key=True)

    user_id      = columns.UUID(required=False, index=True)

    email      = columns.Text(required=False, )

    token      = columns.Text(required=False, index=True)

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class reset_password_email(Model):

    id      = columns.UUID(required=True, partition_key=True)

    email      = columns.Text(required=False, index=True)

    token      = columns.Text(required=False, index=True)

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_subscriptions(Model):

    id      = columns.UUID(required=True, partition_key=True)

    user_id      = columns.UUID(required=False, index=True)

    course_id      = columns.UUID(required=False, )

    require_accomodation      = columns.Text(required=False, )

    require_insurance      = columns.Text(required=False, )

    payment_details      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class school_profile(Model):

    id      = columns.UUID(required=True, partition_key=True)

    user_id      = columns.UUID(required=False, index=True)

    status      = columns.Text(required=False, )

    contact_persons      = columns.Text(required=False, )

    school_name      = columns.Text(required=False, )

    registration_document      = columns.Text(required=False, )

    stripe_details      = columns.Text(required=False, )

    address1      = columns.Text(required=False, )

    address2      = columns.Text(required=False, )

    city      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    introduction      = columns.Text(required=False, )

    logo      = columns.Text(required=False, )

    school_photos      = columns.Text(required=False, )

    subscriptions      = columns.Text(required=False, )

    website      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class student_profile(Model):

    id      = columns.UUID(required=True, partition_key=True)
    user_id      = columns.UUID(required=False, index=True)
    status      = columns.Text(required=False, )
    currency      = columns.Text(required=False, )
    language      = columns.Text(required=False, )
    liked_courses      = columns.Text(required=False, )

    # in student profile form
    avatar = columns.Text(required=False, )
    first_name = columns.Text(required=False, )
    middle_name = columns.Text(required=False, )
    last_name = columns.Text(required=False, )
    gender = columns.Text(required=False, )
    birthday = columns.DateTime(required=False, )
    nationality = columns.Text(required=False, )
    country_of_residence = columns.Text(required=False, )
    email = columns.Text(required=False, )
    phone = columns.Text(required=False, )
    passport_info = columns.Text(required=False, )
    emergency_contact_person = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_detail(Model):
    fileFields = ['instructor_photo', 'cover', 'photos']

    id      = columns.UUID(required=True, partition_key=True)
    school_id      = columns.UUID(required=False, )

    name = columns.Text(required=True, )
    category_id = columns.Text(required=True, )
    level = columns.Text(required=True, )
    start_date = columns.DateTime(required=True, )
    end_date = columns.DateTime(required=True, )
    description = columns.Text(required=False, )
    group_size = columns.Integer(required=True, )
    gender = columns.Text(required=False, )
    age_range = columns.List(columns.Integer, required=False, )
    hours = columns.Integer(required=True, )
    language = columns.Text(required=True, )
    instructor_photo = columns.Text(required=False, )
    instructor_info = columns.Text(required=False, )
    issue_certificate = columns.Boolean(required=True, )
    certificate = columns.Text(required=False, )
    address = columns.Text(required=True, )
    city = columns.Text(required=True, )
    country = columns.Text(required=True, )
    api_key = columns.Text(required=True, )
    location_description = columns.Text(required=False, )
    how_to_get_there = columns.Text(required=False, )
    where_to_meet = columns.Text(required=False, )
    schedule = columns.Text(required=True, )
    meals_included = columns.Boolean(required=True, )
    meals = columns.List(columns.Text, required=False, )
    meals_info = columns.Text(required=False, )
    provide = columns.Text(required=False, )
    guest_needs_to_bring = columns.Text(required=False, )
    guest_requirement = columns.Text(required=False, )
    request_form_existed = columns.Boolean(required=True, )
    request_form = columns.Text(required=False, )
    tags = columns.List(columns.Text, required=False, )
    cover = columns.Text(required=True, )
    photos = columns.List(columns.Text, required=True, )
    notes = columns.Text(required=False, )
    seats = columns.Integer(required=True, )
    price = columns.Decimal(required=True, )
    registration_start_date = columns.DateTime(required=True, )
    registration_end_date = columns.DateTime(required=True, )
    early_bird_discount = columns.Boolean(required=False, )
    discount_rate = columns.Text(required=False, )
    quota = columns.Text(required=False, )
    down_payment = columns.Boolean(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class accomodation_detail(Model):
    fileFields = ['photos']

    id      = columns.UUID(required=True, partition_key=True)
    course_id      = columns.UUID(required=False, )

    options = columns.List(columns.Text, required=False, )
    other_options = columns.Text(required=False, )
    location_description = columns.Text(required=False, )
    facilities = columns.List(columns.Text, required=False, )
    other_facilities = columns.Text(required=False, )
    photos = columns.List(columns.Text, required=False, )
    room1_enabled = columns.Boolean(required=False, )
    room1_type = columns.Text(required=False, )
    room1_quota = columns.Text(required=False, )
    room1_price = columns.Text(required=False, )
    room2_enabled = columns.Boolean(required=False, )
    room2_type = columns.Text(required=False, )
    room2_quota = columns.Text(required=False, )
    room2_price = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class visa_detail(Model):

    id      = columns.UUID(required=True, partition_key=True)

    course_id      = columns.UUID(required=False, )

    information      = columns.Text(required=False, )

    last_date_submission      = columns.Text(required=False, )

    document_description      = columns.Text(required=False, )

    visa_url      = columns.Text(required=False, )

    schooli_invitation_letter      = columns.Text(required=False, )

    refund_policy      = columns.Text(required=False, )

    auto_reply_message      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class featured_course(Model):

    id      = columns.UUID(required=True, partition_key=True)

    course_id      = columns.UUID(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class reviews(Model):

    id      = columns.UUID(required=True, partition_key=True)

    user_id      = columns.UUID(required=False, index=True)

    course_id      = columns.UUID(required=False, )

    ratings      = columns.Text(required=False, )

    comments      = columns.Text(required=False, )

    photos      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_types(Model):

    id      = columns.UUID(required=True, partition_key=True)

    name      = columns.Text(required=False, )

    type      = columns.Text(required=False, )

    description      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class test(Model):

    id      = columns.UUID(required=True, partition_key=True)
    ls      = columns.List(columns.Text, required=False, )
    lsi      = columns.List(columns.Integer, required=False, )
    dm      = columns.Decimal(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()


# materialized views
class user_by_email(user):
    partition_keys = ['email']

# this func will auto create tables and materialized views
# coonect database before do this
def sync_tables_and_materialized_views():
    # tables
    sync_table(user)
    sync_table(activation_email)
    sync_table(reset_password_email)
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
    # materialized views
    sync_materialized_view(user_by_email)
