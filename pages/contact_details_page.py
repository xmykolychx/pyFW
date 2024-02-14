from pages.base_page import BasePage
from utils.locators import ContactDetailsPageLocators
from faker import Faker

class ContactDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    def set_address(self):
        fake = Faker()
        fake_street_one = fake.street_address()
        fake_street_two = fake.street_address()
        fake_city = fake.city()
        fake_province = fake.city()
        fake_postcode = fake.postcode()
        self.clear_text(ContactDetailsPageLocators.street_one_input)
        self.clear_text(ContactDetailsPageLocators.street_two_input)
        self.clear_text(ContactDetailsPageLocators.city_input)
        self.clear_text(ContactDetailsPageLocators.state_province_input)
        self.clear_text(ContactDetailsPageLocators.zip_postal_code_input)
        self.enter_text(ContactDetailsPageLocators.street_one_input, fake_street_one)
        self.enter_text(ContactDetailsPageLocators.street_two_input, fake_street_two)
        self.enter_text(ContactDetailsPageLocators.city_input, fake_city)
        self.enter_text(ContactDetailsPageLocators.state_province_input, fake_province)
        self.enter_text(ContactDetailsPageLocators.zip_postal_code_input, fake_postcode)


    def set_telephone(self):
        fake = Faker()
        fake_home_number = fake.phone_number()
        fake_mobile_number = fake.phone_number()
        fake_work_number = fake.phone_number()
        self.clear_text(ContactDetailsPageLocators.home_telephone_input)
        self.clear_text(ContactDetailsPageLocators.mobile_telephone_input)
        self.clear_text(ContactDetailsPageLocators.work_telephone_input)
        self.enter_text(ContactDetailsPageLocators.home_telephone_input, fake_home_number)
        self.enter_text(ContactDetailsPageLocators.mobile_telephone_input, fake_mobile_number)
        self.enter_text(ContactDetailsPageLocators.work_email_input, fake_work_number)


    def set_email(self):
        fake = Faker()
        fake_work_email = fake.email()
        fake_other_email = fake.email()
        self.clear_text(ContactDetailsPageLocators.work_email_input)
        self.clear_text(ContactDetailsPageLocators.other_email_input)
        self.enter_text(ContactDetailsPageLocators.work_email_input, fake_work_email)
        self.enter_text(ContactDetailsPageLocators.other_email_input, fake_other_email)

    def click_save_button(self):
        self.click(ContactDetailsPageLocators.save_button)