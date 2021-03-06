# hidden and file_fields can be dot path
# json_fields can't be dot path
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

class file(Model):

    id      = columns.UUID(required=True, partition_key=True)

    path      = columns.Text(required=False, index=True)

    tmp      = columns.Boolean(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class user(Model, UserMixin):
    hidden = ['password', 'google_id', 'facebook_id']

    id      = columns.UUID(required=True, partition_key=True)

    password      = columns.Bytes(required=False, )

    privacy      = columns.Text(required=False, )

    email      = columns.Text(required=False, index=True, )

    user_type      = columns.Text(required=False, )

    email_confirmed      = columns.Boolean(required=False, default=False)

    profile_completed      = columns.Boolean(required=False, )

    google_id      = columns.Text(required=False, index=True, )
    facebook_id      = columns.Text(required=False, index=True, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class confirmation_email(Model):

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
    file_fields = ['logo', 'photos', 'registration_document']
    json_fields = ['contact_persons']

    id      = columns.UUID(required=True, partition_key=True)

    user_id      = columns.UUID(required=False, index=True)

    status    = columns.Text(required=False, )
    name      = columns.Text(required=False, )
    address      = columns.Text(required=False, )
    city      = columns.Text(required=False, )
    country      = columns.Text(required=False, )
    introduction      = columns.Text(required=False, )
    website      = columns.Text(required=False, )
    contact_persons      = columns.Text(required=False, default='[{"last_name":null,"first_name":null,"title":null,"email":null,"tel":null},{"last_name":null,"first_name":null,"title":null,"email":null,"tel":null}]')
    registration_document      = columns.Text(required=False, )
    stripe      = columns.Text(required=False, )
    logo      = columns.Text(required=False, )
    photos = columns.List(columns.Text, required=True, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class student_profile(Model):
    file_fields = ['avatar']
    json_fields = ['passport_info', 'emergency_contact_persons']

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
    phone = columns.Text(required=False, )
    passport_info = columns.Text(required=False, default='{"number":null,"issued_country":null,"expiry_date":null}')
    emergency_contact_persons = columns.Text(required=False, default='[{"name":null,"relationship":null,"tel":null},{"name":null,"relationship":null,"tel":null}]')

    created_at = columns.DateTime()
    updated_at = columns.DateTime()
    
class course(Model):
    file_fields = ['instructors.*.photo', 'cover', 'photos']
    json_fields = ['instructors', 'request_form', 'early_bird', 'down_payment']

    id      = columns.UUID(required=True, partition_key=True)
    school_id      = columns.UUID(required=False, )

    # 
    with_accom = columns.Boolean(required=False, )
    # 
    start_date = columns.DateTime(required=False, )
    end_date = columns.DateTime(required=False, )
    category_id = columns.Text(required=False, )
    level = columns.Text(required=False, )
    title = columns.Text(required=False, )
    # 
    gender = columns.Text(required=False, )
    age_range = columns.List(columns.Integer, required=False, )
    hours = columns.List(columns.Integer, required=False, )
    description = columns.Text(required=False, )
    # 
    language = columns.Text(required=False, )
    instructors = columns.Text(required=False, default='[{"name":null,"phone":null,"description":null,"photo":null},{"name":null,"phone":null,"description":null,"photo":null}]')
    # 
    street = columns.Text(required=False, )
    city = columns.Text(required=False, )
    province = columns.Text(required=False, )
    zip_code = columns.Text(required=False, )
    country = columns.Text(required=False, )
    api_key = columns.Text(required=False, )
    location_description = columns.Text(required=False, )
    how_to_get_there = columns.Text(required=False, )
    where_to_meet = columns.Text(required=False, )
    # 
    schedule = columns.Text(required=False, )
    meals_included = columns.Boolean(required=False, )
    meals = columns.List(columns.Text, required=False, )
    weather_arrangement = columns.Text(required=False, )
    # 
    provide = columns.Text(required=False, )
    guest_needs_to_bring = columns.Text(required=False, )
    issue_certificate = columns.Boolean(required=False, )
    certificate = columns.Text(required=False, )
    # 
    entry_requirment = columns.Text(required=False, )
    request_form_enabled = columns.Boolean(required=False, )
    request_form = columns.Text(required=False, default='[{"enabled":false,"value":null},{"enabled":false,"value":null}]')
    # in frontend, create program page 9 is accomodation
    # 
    group_size = columns.Integer(required=False, )
    seat_quota = columns.Integer(required=False, )
    price = columns.Decimal(required=False, )
    # 
    early_bird = columns.Text(required=False, default='{"enabled":false,"discount":null,"quota":null,"end_date":null}')
    down_payment = columns.Text(required=False, default='{"enabled":false,"discount":null,"rest":null}')
    # 
    cover = columns.Text(required=False, )
    photos = columns.List(columns.Text, required=False, )
    youtube_video_link = columns.Text(required=False, )
    tags = columns.List(columns.Text, required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class accomodation(Model):
    file_fields = ['photos']
    json_fields = ['rooms']

    id      = columns.UUID(required=True, partition_key=True)
    course_id      = columns.UUID(required=False, )

    type = columns.Text(required=False, )
    name = columns.Text(required=False, )
    phone = columns.Text(required=False, )
    address = columns.Text(required=False, )
    facilities = columns.List(columns.Text, required=False, )
    description = columns.Text(required=False, )
    photos = columns.List(columns.Text, required=False, )
    rooms = columns.Text(required=False, default='[{"enabled":false,"type":"shared half","quota":null,"price":null},{"enabled":false,"type":"shared 3 ppl","quota":null,"price":null},{"enabled":false,"type":"private double bed","quota":null,"price":null}]')

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
    sync_table(key_value)
    sync_table(file)
    sync_table(user)
    sync_table(confirmation_email)
    sync_table(reset_password_email)
    sync_table(course_subscriptions)
    sync_table(school_profile)
    sync_table(student_profile)
    sync_table(course)
    sync_table(accomodation)
    sync_table(visa_detail)
    sync_table(featured_course)
    sync_table(reviews)
    sync_table(course_types)
    sync_table(test)
    # materialized views
    sync_materialized_view(user_by_email)
