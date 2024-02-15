import pytest
import requests


@pytest.mark.run(order=1)
def test_login(driver, login):
    response = requests.get(driver.current_url)
    assert response.status_code == 200

