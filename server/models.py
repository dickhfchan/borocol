from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table as sync_table0
from cassandra.cqlengine.models import Model

class User(Model):

    id      = columns.Text(required=True, primary_key=True)

    password      = columns.Text(required=False, )

    privacy      = columns.Text(required=False, )

    email      = columns.Text(required=False, )

    userType      = columns.Text(required=False, )


class CourseSubscriptions(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    course_id      = columns.Text(required=False, )

    requireAccomodation      = columns.Text(required=False, )

    requireInsurance      = columns.Text(required=False, )

    paymentDetails      = columns.Text(required=False, )


class SchoolProfile(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    contactPersons      = columns.Text(required=False, )

    schoolName      = columns.Text(required=False, )

    registrationDocument      = columns.Text(required=False, )

    stripeDetails      = columns.Text(required=False, )

    address1      = columns.Text(required=False, )

    address2      = columns.Text(required=False, )

    city      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    introduction      = columns.Text(required=False, )

    logo      = columns.Text(required=False, )

    schoolPhotos      = columns.Text(required=False, )

    subscriptions      = columns.Text(required=False, )

    website      = columns.Text(required=False, )


class StudentProfile(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    fristName      = columns.Text(required=False, )

    lastName      = columns.Text(required=False, )

    phoneNumber      = columns.Text(required=False, )

    gender      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    currency      = columns.Text(required=False, )

    language      = columns.Text(required=False, )

    passportInformation      = columns.Text(required=False, )

    likedCourses      = columns.Text(required=False, )


class CourseDetail(Model):

    id      = columns.Text(required=True, primary_key=True)

    school_id      = columns.Text(required=False, )

    country      = columns.Text(required=False, )

    status      = columns.Text(required=False, )

    viewCount      = columns.Text(required=False, )

    category      = columns.Text(required=False, )

    name      = columns.Text(required=False, )

    statDate      = columns.Text(required=False, )

    endDate      = columns.Text(required=False, )

    lengthOfCourse      = columns.Text(required=False, )

    noOfLessons      = columns.Text(required=False, )

    classDay      = columns.Text(required=False, )

    level      = columns.Text(required=False, )

    ageRange      = columns.Text(required=False, )

    description      = columns.Text(required=False, )

    language      = columns.Text(required=False, )

    requirement      = columns.Text(required=False, )

    certification      = columns.Text(required=False, )

    certificationName      = columns.Text(required=False, )

    quota      = columns.Text(required=False, )

    price      = columns.Text(required=False, )

    earlyBirdQuota      = columns.Text(required=False, )

    registrationStartDate      = columns.Text(required=False, )

    registrationEndDate      = columns.Text(required=False, )

    classSchedule      = columns.Text(required=False, )

    badWeatherArrangement      = columns.Text(required=False, )

    remarks      = columns.Text(required=False, )

    photos      = columns.Text(required=False, )

    tags      = columns.Text(required=False, )


class AccomodationDetail(Model):

    id      = columns.Text(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

    type      = columns.Text(required=False, )

    suggestion      = columns.Text(required=False, )

    address1      = columns.Text(required=False, )

    address2      = columns.Text(required=False, )

    shareCount      = columns.Text(required=False, )

    bedStyle      = columns.Text(required=False, )

    mealDescriptions      = columns.Text(required=False, )

    facilites      = columns.Text(required=False, )

    otherFacilites      = columns.Text(required=False, )

    schoolCommuteTime      = columns.Text(required=False, )

    airportCommuteTime      = columns.Text(required=False, )

    price      = columns.Text(required=False, )

    cancellationPolicy      = columns.Text(required=False, )

    messageToStudent      = columns.Text(required=False, )


class VisaDetail(Model):

    id      = columns.Text(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )

    information      = columns.Text(required=False, )

    lastDateSubmission      = columns.Text(required=False, )

    documentDescription      = columns.Text(required=False, )

    visaUrl      = columns.Text(required=False, )

    schooliInvitationLetter      = columns.Text(required=False, )

    refundPolicy      = columns.Text(required=False, )

    autoReplyMessage      = columns.Text(required=False, )


class FeaturedCourse(Model):

    id      = columns.Text(required=True, primary_key=True)

    course_id      = columns.Text(required=False, )


class Reviews(Model):

    id      = columns.Text(required=True, primary_key=True)

    user_id      = columns.Text(required=False, )

    course_id      = columns.Text(required=False, )

    ratings      = columns.Text(required=False, )

    comments      = columns.Text(required=False, )

    photos      = columns.Text(required=False, )


class CourseTypes(Model):

    id      = columns.Text(required=True, primary_key=True)

    name      = columns.Text(required=False, )

    type      = columns.Text(required=False, )

    description      = columns.Text(required=False, )



def sync_table():

  sync_table0(User)

  sync_table0(CourseSubscriptions)

  sync_table0(SchoolProfile)

  sync_table0(StudentProfile)

  sync_table0(CourseDetail)

  sync_table0(AccomodationDetail)

  sync_table0(VisaDetail)

  sync_table0(FeaturedCourse)

  sync_table0(Reviews)

  sync_table0(CourseTypes)
