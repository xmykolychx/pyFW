import pytest
from selenium import webdriver
from modules.pages import *


URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
DEFAULT_USER = {'username': 'Admin', 'password': 'admin123'}


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver, url=URL):
    driver.get(url)
    login_page = LoginPage(driver)
    login_page.enter_user_credentials(DEFAULT_USER['username'], DEFAULT_USER['password'])


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture
def forgot_page(driver):
    return ForgotPage(driver)


@pytest.fixture
def punch_out_page(driver):
    return PunchOutPage(driver)


@pytest.fixture
def personal_details_page(driver):
    return PersonalDetailsPage(driver)

@pytest.fixture
def my_info_page(driver):
    return MyInfoPage(driver)

@pytest.fixture
def contact_details_page(driver):
    return ContactDetailsPage(driver)


@pytest.fixture
def buzz_page(driver):
    return BuzzPage(driver)

@pytest.fixture
def to_forgot_page(driver, url=URL):
    driver.get(url)
    login_page = LoginPage(driver)
    login_page.click_forgot_password()





# pages to test: admin, buzz, performance
# request.addfinalizer(do_screenshot), for instance