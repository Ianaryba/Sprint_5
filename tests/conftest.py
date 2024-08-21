import pytest

from selenium import webdriver
@pytest.fixture(scope = 'session') # фикстура, которая добавляет webdriver
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

