def test_search(driver, login, dashboard_page):
    dashboard_page.search('main')
    assert 'Maintenance' in driver.page_source
