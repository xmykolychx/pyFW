from pages.base_page import BasePage
from utils.locators import ContactDetailsPageLocators
from utils.test_data import TestData


class ContactDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_address(self):
        self.clear_text(ContactDetailsPageLocators.street_one_input)
        self.clear_text(ContactDetailsPageLocators.street_two_input)
        self.clear_text(ContactDetailsPageLocators.city_input)
        self.clear_text(ContactDetailsPageLocators.state_province_input)
        self.clear_text(ContactDetailsPageLocators.zip_postal_code_input)
        self.enter_text(ContactDetailsPageLocators.street_one_input, TestData.street_one)
        self.enter_text(ContactDetailsPageLocators.street_two_input, TestData.street_two)
        self.enter_text(ContactDetailsPageLocators.city_input, TestData.city)
        self.enter_text(ContactDetailsPageLocators.state_province_input, TestData.province)
        self.enter_text(ContactDetailsPageLocators.zip_postal_code_input, TestData.postcode)

    def set_telephone(self):
        self.clear_text(ContactDetailsPageLocators.home_telephone_input)
        self.clear_text(ContactDetailsPageLocators.mobile_telephone_input)
        self.clear_text(ContactDetailsPageLocators.work_telephone_input)
        self.enter_text(ContactDetailsPageLocators.home_telephone_input, TestData.home_number)
        self.enter_text(ContactDetailsPageLocators.mobile_telephone_input, TestData.mobile_number)
        self.enter_text(ContactDetailsPageLocators.work_email_input, TestData.work_number)

    def set_email(self):
        self.clear_text(ContactDetailsPageLocators.work_email_input)
        self.clear_text(ContactDetailsPageLocators.other_email_input)
        self.enter_text(ContactDetailsPageLocators.work_email_input, TestData.work_email)
        self.enter_text(ContactDetailsPageLocators.other_email_input, TestData.other_email)

    def click_save_button(self):
        self.click(ContactDetailsPageLocators.save_button)
