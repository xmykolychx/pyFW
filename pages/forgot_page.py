from pages.base_page import BasePage
from utils.locators import ForgotPageLocators


class ForgotPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username: str):
        self.enter_text(ForgotPageLocators.username_input, username)

    def click_cancel(self):
        self.click(ForgotPageLocators.cancel_button)

    def click_reset(self):
        self.click(ForgotPageLocators.reset_button)
