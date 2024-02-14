def test_change_personal_details(driver, login, dashboard_page, personal_details_page):
    dashboard_page.click_my_info()
    personal_details_page.set_names()
    personal_details_page.set_ids()
    personal_details_page.set_license()
    personal_details_page.set_marital_status()
    personal_details_page.set_gender()
    personal_details_page.click_save_button()


def test_change_contact_details(driver, login, dashboard_page, my_info_page, contact_details_page):
    dashboard_page.click_my_info()
    my_info_page.click_contact_details()
    contact_details_page.set_address()
    contact_details_page.set_telephone()
    contact_details_page.set_email()
    contact_details_page.click_save_button()
