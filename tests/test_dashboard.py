# import pytest
# from modules.pages import *


# @pytest.mark.parametrize('dashboard_page', [('DashboardPage', 'driver')])
def test_dashboard_url(driver, login, dashboard_page):
    # dashboard_page = DashboardPage(driver)
    dashboard_page.check_url(driver, driver.current_url)


def test_widget_presence(driver, login, dashboard_page):
    dashboard_page.check_widgets_presence()


def test_punch_out_from_dashboard(driver, login, dashboard_page, punch_out_page):
    dashboard_page.click_pu_clock()
    punch_out_page.select_today()
    punch_out_page.enter_notes()
    punch_out_page.click_out()


def test_employee_on_leave_settings(driver, login, dashboard_page):
    dashboard_page.click_eol_settings_widget_button()
    dashboard_page.show_accessible_employees()
    dashboard_page.click_save_config()
