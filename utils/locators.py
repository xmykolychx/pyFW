from selenium.webdriver.common.by import By


class DashboardPageLocators:
    dashboard_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    page_header = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]')

    # side panel
    side_panel = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav')
    search_input = (By.XPATH, '//input[@placeholder="Search"]')
    search_result_list = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul')
    admin_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
    pim_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
    leave_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')
    time_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span')
    recruitment_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
    my_info_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span')
    performance_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
    dashboard_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span')
    directory_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span')
    maintenance_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span')
    claim_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span')
    buzz_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span')
    buzz_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span')

    # widgets
    time_at_work_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]')
    tam_clock_icon = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button")

    my_actions_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]')
    quick_launch_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]')
    buzz_latest_posts_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[4]')

    employee_on_leave_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]')
    settings_eol_widget_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/i')
    show_accessible_employees_switch = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div[2]/div/div/div/form/div[1]/div/div[2]/div/label/span')
    save_config_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div[2]/div/div/div/form/div[2]/button[2]')


    employee_distribution_unit_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[6]')
    employee_distribution_location_widget = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[7]')


class LoginPageLocators:
    user_name_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    forgot_password_button = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")


class ForgotPageLocators:
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    cancel_button = (By.XPATH, "//button[@type='button']")
    reset_button = (By.XPATH, "//button[@type='submit']")


class PunchOutPageLocators:
    calendar_icon = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i")
    calendar_today_button = (By.XPATH, "//div[@class='oxd-date-input-link --today']")
    calendar_clear_button = (By.XPATH, "//div[@class='oxd-date-input-link --clear']")
    calendar_close_button = (By.XPATH, "//div[@class='oxd-date-input-link --close']")
    calendar_prev_button = (By.XPATH, "//button[@class='oxd-icon-button']//i[@class='oxd-icon bi-chevron-left']")
    calendar_next_button = (By.XPATH, "//button[@class='oxd-icon-button']//i[@class='oxd-icon bi-chevron-right']")
    calendar_select_month_arrow_button = (By.XPATH, "//div[@class='oxd-calendar-selector-month-selected']//i[@class='oxd-icon bi-caret-down-fill oxd-icon-button__icon']")
    calendar_select_year_arrow_button = (By.XPATH, "//div[@class='oxd-calendar-selector-year-selected']//i[@class='oxd-icon bi-caret-down-fill oxd-icon-button__icon']")

    notes_input = (By.XPATH, "//textarea[@placeholder='Type here']")

    out_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button")

class MyInfoPageLocators:
    personal_details_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
    contact_details_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a')
    emergency_contact_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a')
    dependents_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a')
    immigration_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a')
    job_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a')
    salary_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a')
    tax_exemptions_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a')
    report_to_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a')
    qualifications_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a')
    memberships_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a')


class PersonalDetailsPageLocators:
    # personal details
    first_name = (By.XPATH, '//input[@name="firstName"]')
    middle_name = (By.XPATH, '//input[@name="middleName"]')
    last_name = (By.XPATH, '//input[@name="lastName"]')
    nickname_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')
    employee_id_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    other_id_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
    driver_license_number_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
    license_expiry_date_picker = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/i')
    license_expiry_date_month_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]')
    # not a select html, so should do like this
    license_expiry_month_sep = (By.XPATH, "//li[normalize-space()='September']")
    license_expiry_month_sep_date = (By.XPATH, "//div[contains(text(),'30')]")

    ssn_number = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input')
    sin_number = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input')
    nationality_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')

    marital_status_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i')
    marital_status_other = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/span')

    date_of_birth_picker = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/i')
    gender_male_radio_button = (By.XPATH, "(//label/span)[1]")
    gender_female_radio_button = (By.XPATH, "(//label/span)[2]")
    military_service_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input')
    smoker_checkbox = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span/i')
    personal_details_save_button = (By.XPATH, "//form/div[4]/button")

    # custom fields
    blood_type_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]/i')
    custom_fields_save_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')

    # attachments
    add_attachment_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button/i')
    browse_text_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/div[1]')
    browse_icon_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/i')
    comment_textarea = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[2]/div/div/div/div[2]/textarea')
    cancel_attachment_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[1]')
    save_attachment_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[2]')

class ContactDetailsPageLocators:
    # contact details
    street_one_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input')
    street_two_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input')
    city_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input')
    state_province_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input')
    zip_postal_code_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input')
    country_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div')
    home_telephone_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input')
    mobile_telephone_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input')
    work_telephone_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input')
    work_email_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input')
    other_email_input = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input')
    save_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')

    # attachments
    add_attachments_button = (By.XPATH, '')
    browse_text_button = (By.XPATH, '')
    browse_icon_button = (By.XPATH, '')
    comment_textarea = (By.XPATH, '')
    cancel_adding_button = (By.XPATH, '')
    save_adding_button = (By.XPATH, '')

class EmergencyContactsPageLocators:
    # add contact
    add_contact_button = (By.XPATH, '')
    name_input = (By.XPATH, '')
    relationship_input = (By.XPATH, '')
    home_telephone_input = (By.XPATH, '')
    mobile_telephone_input = (By.XPATH, '')
    work_telephone_input = (By.XPATH, '')
    cancel_contact_button = (By.XPATH, '')
    save_contact_button = (By.XPATH, '')

    # attachments
    add_attachments_button = (By.XPATH, '')
    browse_text_button = (By.XPATH, '')
    browse_icon_button = (By.XPATH, '')
    comment_textarea = (By.XPATH, '')
    cancel_adding_button = (By.XPATH, '')
    save_adding_button = (By.XPATH, '')

class DependentsPageLocators:
    # add dependent
    add_dependent_button = (By.XPATH, '')
    name_input = (By.XPATH, '')
    relationship_dropdown = (By.XPATH, '')
    date_of_birth_picker = (By.XPATH, '')

    # attachments
    add_attachments_button = (By.XPATH, '')
    browse_text_button = (By.XPATH, '')
    browse_icon_button = (By.XPATH, '')
    comment_textarea = (By.XPATH, '')
    cancel_adding_button = (By.XPATH, '')
    save_adding_button = (By.XPATH, '')

class ImmigrationPageLocators:
    # add immigration
    add_passport_radio_button = (By.XPATH, '')
    add_visa_radio_button = (By.XPATH, '')
    number_input = (By.XPATH, '')
    issued_date_picker = (By.XPATH, '')
    expiry_date_picker = (By.XPATH, '')
    eligible_status_input = (By.XPATH, '')
    issued_by_dropdown = (By.XPATH, '')
    eligible_review_date_picker = (By.XPATH, '')
    comments_input = (By.XPATH, '')

    # attachments
    add_attachments_button = (By.XPATH, '')
    browse_text_button = (By.XPATH, '')
    browse_icon_button = (By.XPATH, '')
    comment_textarea = (By.XPATH, '')
    cancel_adding_button = (By.XPATH, '')
    save_adding_button = (By.XPATH, '')
    edit_attachment_button = (By.XPATH, '')
    delete_attachment_button = (By.XPATH, '')
    download_attachment_button = (By.XPATH, '')


class JobPageLocators:
    pass

class QualificationsPageLocators:
    # work experience
    add_work_experience_button = (By.XPATH, '')
    company_input = (By.XPATH, '')
    job_title_input = (By.XPATH, '')
    from_picker = (By.XPATH, '')
    to_picker = (By.XPATH, '')
    comment_work_input = (By.XPATH, '')
    cancel_work_experience_button = (By.XPATH, '')
    save_work_experience_button = (By.XPATH, '')

    # education
    add_education_button = (By.XPATH, '')
    level_dropdown = (By.XPATH, '')
    institute_input = (By.XPATH, '')
    major_specialization_input = (By.XPATH, '')
    year_input = (By.XPATH, '')
    gpa_score_input = (By.XPATH, '')
    start_date_picker = (By.XPATH, '')
    end_date_picker = (By.XPATH, '')
    cancel_education_button = (By.XPATH, '')
    save_education_button = (By.XPATH, '')
    edit_education_button = (By.XPATH, '')
    delete_education_button = (By.XPATH, '')

    # skills
    add_skill_button = (By.XPATH, '')
    skill_dropdown = (By.XPATH, '')
    years_of_experience_input = (By.XPATH, '')
    comment_skill_input = (By.XPATH, '')
    cancel_skill_button = (By.XPATH, '')
    save_skill_button = (By.XPATH, '')

    # languages
    add_language_button = (By.XPATH, '')
    language_dropdown = (By.XPATH, '')
    fluency_dropdown = (By.XPATH, '')
    competence_dropdown = (By.XPATH, '')
    comment_language_input = (By.XPATH, '')
    cancel_language_button = (By.XPATH, '')
    save_language_button = (By.XPATH, '')
    edit_language_button = (By.XPATH, '')
    delete_language_button = (By.XPATH, '')

    # license
    add_license_button = (By.XPATH, '')
    license_type_dropdown = (By.XPATH, '')
    license_number_input = (By.XPATH, '')
    issued_date_picker = (By.XPATH, '')
    expired_date_picker = (By.XPATH, '')
    cancel__button = (By.XPATH, '')
    save__button = (By.XPATH, '')

    # attachments
    add_attachment_button = (By.XPATH, '')
    browse_text_button = (By.XPATH, '')
    browse_icon_button = (By.XPATH, '')
    comment_textarea = (By.XPATH, '')
    cancel_attachment_button = (By.XPATH, '')
    save_attachment_button = (By.XPATH, '')

class MembershipsPageLocators:
    # assigned memberships
    add_membership_button = (By.XPATH, '')
    membership_dropdown = (By.XPATH, '')
    subscription_paid_by_dropdown = (By.XPATH, '')
    subscription_amount_input = (By.XPATH, '')
    currency_dropdown = (By.XPATH, '')
    subscription_commence_date_picker = (By.XPATH, '')
    subscription_renewal_date_picker = (By.XPATH, '')
    cancel_membership_button = (By.XPATH, '')
    save_membership_button = (By.XPATH, '')

    # attachments
    add_attachment_button = (By.XPATH, '')
    browse_text_button = (By.XPATH, '')
    browse_icon_button = (By.XPATH, '')
    comment_textarea = (By.XPATH, '')
    cancel_attachments_button = (By.XPATH, '')
    save_attachment_button = (By.XPATH, '')
    edit_attachment_button = (By.XPATH, '')
    delete_attachment_button = (By.XPATH, '')


class BuzzPageLocators:
    # add post
    post_text_input = (By.XPATH, '//textarea[@placeholder="What\'s on your mind?"]')
    post_post_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    share_photos_button = (By.XPATH, '')
    share_videos_button = (By.XPATH, '')

    # edit post
    edit_post_text_input = (By.XPATH, "(//textarea[@class='oxd-buzz-post-input'])[2]")
    edit_post_post_button = (By.XPATH, "(//button[@type='submit'][normalize-space()='Post'])[2]")

    # most posts
    most_recent_posts_button = (By.XPATH, '')
    most_liked_posts_button = (By.XPATH, '')
    most_commented_posts_button = (By.XPATH, '')

    # post itself
    commentator_name = (By.XPATH, '')
    commentator_avatar = (By.XPATH, '')
    latest_post_context_menu_button = (By.XPATH, "(//*[@class='orangehrm-buzz-post-header-config']//button)[1]")

    delete_post_button = (By.XPATH, "//*[@class='orangehrm-buzz-post-header-config-item'][1]")
    no_delete_post_button = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    yes_delete_post_button = (By.XPATH, "//button[normalize-space()='Yes, Delete']")

    edit_post_button = (By.XPATH, "//*[@class='orangehrm-buzz-post-header-config-item'][2]")
    like_post_button = (By.XPATH, '')

    # comment
    comment_latest_post_button = (By.XPATH, "//div[@class='orangehrm-buzz-newsfeed']//div[1]//div[1]//div[3]//div[1]//button[1]")
    comment_latest_text_input = (By.XPATH, "(//input[@placeholder='Write your comment...'])[1]")
    like_comment_button = (By.XPATH, '')
    edit_comment_button = (By.XPATH, '')
    delete_comment_button = (By.XPATH, '')

    like_count_button = (By.XPATH, '')
    comment_count_button = (By.XPATH, '')

    # upcoming anniversaries
    upcoming_anniversary_avatar = (By.XPATH, '')
    upcoming_anniversary_name = (By.XPATH, '')
    upcoming_anniversary_title = (By.XPATH, '')
    upcoming_anniversary_years = (By.XPATH, '')