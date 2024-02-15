import requests


def test_click_forgot(driver, to_forgot_page, forgot_page):
    forgot_page.enter_username()
    forgot_page.click_reset()
    response = requests.get(driver.current_url)
    assert response.status_code == 200
