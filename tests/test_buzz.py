def test_add_post(driver, login, dashboard_page, buzz_page):
    dashboard_page.click_buzz()
    buzz_page.create_post()


def test_delete_post(login, dashboard_page, buzz_page):
    dashboard_page.click_buzz()
    buzz_page.delete_post()


def test_edit_post(login, dashboard_page, buzz_page):
    dashboard_page.click_buzz()
    buzz_page.edit_post()


def test_drop_comment(driver, login, dashboard_page, buzz_page):
    dashboard_page.click_buzz()
    buzz_page.drop_comment()
