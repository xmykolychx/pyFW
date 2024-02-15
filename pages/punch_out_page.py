from pages.base_page import BasePage
from utils.locators import PunchOutPageLocators
from utils.test_data import TestData


class PunchOutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_today(self):
        self.click(PunchOutPageLocators.calendar_icon)
        self.click(PunchOutPageLocators.calendar_today_button)

    def enter_notes(self):
        self.enter_text(PunchOutPageLocators.notes_input, TestData.text_data)

    def click_out(self):
        self.click(PunchOutPageLocators.out_button)