@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()
