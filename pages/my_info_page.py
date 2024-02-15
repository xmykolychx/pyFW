from pages.base_page import BasePage
from utils.locators import MyInfoPageLocators


class MyInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_contact_details(self):
        self.click(MyInfoPageLocators.contact_details_option)
