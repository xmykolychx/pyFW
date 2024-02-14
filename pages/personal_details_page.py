from pages.base_page import BasePage
from utils.locators import PersonalDetailsPageLocators
from faker import Faker


class PersonalDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def set_names(self):
        fake = Faker()
        fake_first_name = fake.first_name()
        fake_middle_name = fake.first_name_nonbinary()
        fake_last_name = fake.last_name()
        self.clear_text(PersonalDetailsPageLocators.first_name)
        self.clear_text(PersonalDetailsPageLocators.middle_name)
        self.clear_text(PersonalDetailsPageLocators.last_name)
        self.enter_text(PersonalDetailsPageLocators.first_name, fake_first_name)
        self.enter_text(PersonalDetailsPageLocators.middle_name, fake_middle_name)
        self.enter_text(PersonalDetailsPageLocators.last_name, fake_last_name)

    def set_ids(self):
        fake = Faker()
        fake_employee_id = fake.pystr_format(string_format='######')
        fake_other_id = fake.pystr_format(string_format='######')
        self.clear_text(PersonalDetailsPageLocators.employee_id_input)
        self.clear_text(PersonalDetailsPageLocators.other_id_input)
        self.enter_text(PersonalDetailsPageLocators.employee_id_input, fake_employee_id)
        self.enter_text(PersonalDetailsPageLocators.other_id_input, fake_other_id)

    def set_license(self):
        fake = Faker()
        fake_license_number = fake.pystr_format(string_format='######')
        self.clear_text(PersonalDetailsPageLocators.driver_license_number_input)
        self.enter_text(PersonalDetailsPageLocators.driver_license_number_input, fake_license_number)
        self.click(PersonalDetailsPageLocators.license_expiry_date_picker)
        self.click(PersonalDetailsPageLocators.license_expiry_date_month_dropdown)
        self.click(PersonalDetailsPageLocators.license_expiry_month_sep)
        self.click(PersonalDetailsPageLocators.license_expiry_month_sep_date)



    def set_nationality(self):
        pass

    def set_marital_status(self):
        self.click(PersonalDetailsPageLocators.marital_status_dropdown)
        self.click(PersonalDetailsPageLocators.marital_status_other)

    def set_date_of_birth(self):
        pass

    def set_gender(self):
        pass

    def click_save_button(self):
        self.click(PersonalDetailsPageLocators.personal_details_save_button)