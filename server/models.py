from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table as sync_table
from cassandra.cqlengine.models import Model


class user(Model):

    id      = columns.Text(required=True, primary_key=True)

    password      = columns.Text(required=False, )

    privacy      = columns.Text(required=False, )

    email      = columns.Text(required=False, )

    user_type      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_subscriptions(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    course_id      = columns.Text(required=False, )

    require_accomodation      = columns.Text(required=False, )

    require_insurance      = columns.Text(required=False, )

    payment_details      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class school_profile(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

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

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    frist_name      = columns.Text(required=False, )

    last_name      = columns.Text(required=False, )

    phone_number      = columns.Text(required=False, )

    gender      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    currency      = columns.Text(required=False, )

    language      = columns.Text(required=False, )

    passport_information      = columns.Text(required=False, )

    liked_courses      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_detail(Model):

    id      = columns.Text(required=True, primary_key=True)

    school_id      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    view_count      = columns.Text(required=False, )

    category      = columns.Text(required=False, )

    name      = columns.Text(required=False, )

    stat_date      = columns.Text(required=False, )

    end_date      = columns.Text(required=False, )

    length_of_course      = columns.Text(required=False, )

    no_of_lessons      = columns.Text(required=False, )

    class_day      = columns.Text(required=False, )

    level      = columns.Text(required=False, )

    age_range      = columns.Text(required=False, )

    description      = columns.Text(required=False, )

    language      = columns.Text(required=False, )

    requirement      = columns.Text(required=False, )

    certification      = columns.Text(required=False, )

    certification_name      = columns.Text(required=False, )

    quota      = columns.Text(required=False, )

    price      = columns.Text(required=False, )

    early_bird_quota      = columns.Text(required=False, )

    registration_start_date      = columns.Text(required=False, )

    registration_end_date      = columns.Text(required=False, )

    class_schedule      = columns.Text(required=False, )

    bad_weather_arrangement      = columns.Text(required=False, )

    remarks      = columns.Text(required=False, )

    photos      = columns.Text(required=False, )

    tags      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class accomodation_detail(Model):

    id      = columns.Text(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

    type      = columns.Text(required=False, )

    suggestion      = columns.Text(required=False, )

    address1      = columns.Text(required=False, )

    address2      = columns.Text(required=False, )

    share_count      = columns.Text(required=False, )

    bed_style      = columns.Text(required=False, )

    meal_descriptions      = columns.Text(required=False, )

    facilites      = columns.Text(required=False, )

    other_facilites      = columns.Text(required=False, )

    school_commute_time      = columns.Text(required=False, )

    airport_commute_time      = columns.Text(required=False, )

    price      = columns.Text(required=False, )

    cancellation_policy      = columns.Text(required=False, )

    message_to_student      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class visa_detail(Model):

    id      = columns.Text(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

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

    id      = columns.Text(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class reviews(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    course_id      = columns.Text(required=False, )

    ratings      = columns.Text(required=False, )

    comments      = columns.Text(required=False, )

    photos      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

class course_types(Model):

    id      = columns.Text(required=True, primary_key=True)

    name      = columns.Text(required=False, )

    type      = columns.Text(required=False, )

    description      = columns.Text(required=False, )

    created_at = columns.DateTime()
    updated_at = columns.DateTime()

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
