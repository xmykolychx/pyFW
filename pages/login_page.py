from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_user_credentials(self, username: str, password: str):
        self.enter_text(LoginPageLocators.user_name_input, username)
        self.enter_text(LoginPageLocators.password_input, password)
        self.click(LoginPageLocators.login_button)

    def click_forgot_password(self):
        self.click(LoginPageLocators.forgot_password_button)
