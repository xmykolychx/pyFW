from pages.base_page import BasePage
from utils.locators import BuzzPageLocators
from utils.test_data import TestData


class BuzzPage(BasePage):
    def __init__(self, driver):
        super(BuzzPage, self).__init__(driver)

    def create_post(self):
        self.click(BuzzPageLocators.post_text_input)
        self.enter_text(BuzzPageLocators.post_text_input, TestData.text_data)
        self.click(BuzzPageLocators.post_post_button)

    def delete_post(self):
        self.click(BuzzPageLocators.latest_post_context_menu_button)
        self.click(BuzzPageLocators.delete_post_button)
        self.click(BuzzPageLocators.yes_delete_post_button)

    def edit_post(self):
        self.click(BuzzPageLocators.latest_post_context_menu_button)
        self.click(BuzzPageLocators.edit_post_button)
        self.click(BuzzPageLocators.edit_post_text_input)
        self.clear_text(BuzzPageLocators.edit_post_text_input)
        self.enter_text(BuzzPageLocators.edit_post_text_input, TestData.text_data)
        self.click(BuzzPageLocators.edit_post_post_button)

    def drop_comment(self):
        self.click(BuzzPageLocators.comment_latest_post_button)
        self.click(BuzzPageLocators.comment_latest_text_input)
        self.enter_text(BuzzPageLocators.comment_latest_text_input, TestData.text_data)
        self.press_enter(BuzzPageLocators.comment_latest_text_input)
