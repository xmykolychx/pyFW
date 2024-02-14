import requests
from faker import Faker


def test_click_forgot(driver, to_forgot_page, forgot_page):
    fake = Faker()
    forgot_page.enter_username(username=fake.name())
    forgot_page.click_reset()
    response = requests.get(driver.current_url)
    assert response.status_code == 200
