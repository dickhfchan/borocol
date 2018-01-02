export default {
  stepCount: 9,
  step: null,
  progressStr: null,
  formData: {
    declared: false,
    agreed: false,
    // 1
    title: null,
    category: null,
    level: null,
    startDate: null,
    endDate: null,
    description: null,
    // 2
    groupSize: null,
    gender: null,
    ageRange: [16, 30],
    hours: null,
    language: null,
    instructorPhoto: null,
    instructorInfo: null,
    issueCertificate: null,
    certification: null,
    // 3
    address: null,
    // 4
    mealsIncluded: null,
    meals: null,
  },
  formDataMapping: {
    // 1
    title: 'name',
    // 2
    // groupSize
    // gender
    // hours
    // instructorPhoto,
    // instructorInfo,
    issueCertificate: 'certification',
    certification: 'certification_name',
    // 3
    // address
    // city
    // apiKey
    // locationDescription
    // howToGetThere
    // whereToMeetUpYourGuest
    // 4
    // schedule
    // mealsIncluded
    // meals
    // mealsInfo
    // 5

  },
}
