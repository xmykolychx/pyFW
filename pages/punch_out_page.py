from pages.base_page import BasePage
from utils.locators import PunchOutPageLocators
from faker import Faker


class PunchOutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_today(self):
        self.click(PunchOutPageLocators.calendar_icon)
        self.click(PunchOutPageLocators.calendar_today_button)

    def enter_notes(self):
        fake = Faker()
        self.enter_text(PunchOutPageLocators.notes_input, fake.pystr(min_chars=10, max_chars=100))

    def click_out(self):
        self.click(PunchOutPageLocators.out_button)