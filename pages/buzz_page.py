from pages.base_page import BasePage
from utils.locators import BuzzPageLocators
from faker import Faker


class BuzzPage(BasePage):
    def __init__(self, driver):
        super(BuzzPage, self).__init__(driver)

    def create_post(self):
        fake = Faker()
        fake_post_text = fake.pystr(min_chars=10, max_chars=100)
        self.click(BuzzPageLocators.post_text_input)
        self.enter_text(BuzzPageLocators.post_text_input, fake_post_text)
        self.click(BuzzPageLocators.post_post_button)

    def delete_post(self):
        self.click(BuzzPageLocators.latest_post_context_menu_button)
        self.click(BuzzPageLocators.delete_post_button)
        self.click(BuzzPageLocators.yes_delete_post_button)

    def edit_post(self):
        fake = Faker()
        fake_post_text = fake.pystr(min_chars=10, max_chars=100)
        self.click(BuzzPageLocators.latest_post_context_menu_button)
        self.click(BuzzPageLocators.edit_post_button)
        self.click(BuzzPageLocators.edit_post_text_input)
        self.clear_text(BuzzPageLocators.edit_post_text_input)
        self.enter_text(BuzzPageLocators.edit_post_text_input, fake_post_text)
        self.click(BuzzPageLocators.edit_post_post_button)

    def drop_comment(self):
        fake = Faker()
        fake_comment_text = fake.pystr(min_chars=10, max_chars=100)
        self.click(BuzzPageLocators.comment_latest_post_button)
        self.click(BuzzPageLocators.comment_latest_text_input)
        self.enter_text(BuzzPageLocators.comment_latest_text_input, fake_comment_text)
        self.press_enter(BuzzPageLocators.comment_latest_text_input)
