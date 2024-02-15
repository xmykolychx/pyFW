from pages.base_page import BasePage
from utils.locators import PersonalDetailsPageLocators
from utils.test_data import TestData


class PersonalDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def set_names(self):
        self.clear_text(PersonalDetailsPageLocators.first_name)
        self.clear_text(PersonalDetailsPageLocators.middle_name)
        self.clear_text(PersonalDetailsPageLocators.last_name)
        self.enter_text(PersonalDetailsPageLocators.first_name, TestData.first_name)
        self.enter_text(PersonalDetailsPageLocators.middle_name, TestData.middle_name)
        self.enter_text(PersonalDetailsPageLocators.last_name, TestData.last_name)

    def set_ids(self):
        self.clear_text(PersonalDetailsPageLocators.employee_id_input)
        self.clear_text(PersonalDetailsPageLocators.other_id_input)
        self.enter_text(PersonalDetailsPageLocators.employee_id_input, TestData.employee_id)
        self.enter_text(PersonalDetailsPageLocators.other_id_input, TestData.other_id)

    def set_license(self):
        self.clear_text(PersonalDetailsPageLocators.driver_license_number_input)
        self.enter_text(PersonalDetailsPageLocators.driver_license_number_input, TestData.license_number)
        self.click(PersonalDetailsPageLocators.license_expiry_date_picker)
        self.click(PersonalDetailsPageLocators.license_expiry_date_month_dropdown)
        self.click(PersonalDetailsPageLocators.license_expiry_month_sep)
        self.click(PersonalDetailsPageLocators.license_expiry_month_sep_date)


    def set_marital_status(self):
        self.click(PersonalDetailsPageLocators.marital_status_dropdown)
        self.click(PersonalDetailsPageLocators.marital_status_other)

    def set_male_gender(self):
        self.click(PersonalDetailsPageLocators.gender_male_radio_button)

    def set_female_gender(self):
        self.click(PersonalDetailsPageLocators.gender_female_radio_button)

    def click_save_button(self):
        self.click(PersonalDetailsPageLocators.personal_details_save_button)
