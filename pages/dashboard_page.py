from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import DashboardPageLocators
from utils.locators import MyInfoPageLocators
from utils.locators import ContactDetailsPageLocators
from faker import Faker



class DashboardPage(BasePage):
    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)

    def check_url(self, driver, dashboard_url):
        assert driver.current_url == dashboard_url

    def search(self, search_query: str):
        self.enter_text(DashboardPageLocators.search_input, search_query)

    def click_pu_clock(self):
        self.click(DashboardPageLocators.tam_clock_icon)

    def check_widgets_presence(self):
        self.widgets = [
            DashboardPageLocators.time_at_work_widget,
            DashboardPageLocators.my_actions_widget,
            DashboardPageLocators.quick_launch_widget,
            DashboardPageLocators.buzz_latest_posts_widget,
            DashboardPageLocators.employee_on_leave_widget,
            DashboardPageLocators.employee_distribution_unit_widget,
            DashboardPageLocators.employee_distribution_location_widget
        ]
        for w in self.widgets:
            EC.presence_of_element_located(w)

    def click_admin(self):
        self.click(DashboardPageLocators.admin_option)

    def click_pim(self):
        self.click(DashboardPageLocators.pim_option)

    def click_leave(self):
        self.click(DashboardPageLocators.leave_option)

    def click_time(self):
        self.click(DashboardPageLocators.time_option)

    def click_recruitment(self):
        self.click(DashboardPageLocators.recruitment_option)

    def click_my_info(self):
        self.click(DashboardPageLocators.my_info_option)

    def click_performance(self):
        self.click(DashboardPageLocators.performance_option)

    def click_dashboard(self):
        self.click(DashboardPageLocators.dashboard_option)

    def click_directory(self):
        self.click(DashboardPageLocators.directory_option)

    def click_maintenance(self):
        self.click(DashboardPageLocators.maintenance_option)

    def click_claim(self):
        self.click(DashboardPageLocators.claim_option)

    def click_buzz(self):
        self.click(DashboardPageLocators.buzz_option)

    def click_eol_settings_widget_button(self):
        self.click(DashboardPageLocators.settings_eol_widget_button)

    def show_accessible_employees(self):
        self.click(DashboardPageLocators.show_accessible_employees_switch)

    def click_save_config(self):
        self.click(DashboardPageLocators.save_config_button)

    def click_contact_details(self):
        self.click(MyInfoPageLocators.contact_details_option)

    def click_buzz(self):
        self.click(DashboardPageLocators.buzz_option)