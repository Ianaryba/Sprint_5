
from selenium.webdriver.common.by import By


from Lokators import REGISTRATION_BUTTON, EMAIL_BUTTON

def test_successful_registration(driver):

    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys("TestUser")

    driver.find_element(By.XPATH, EMAIL_BUTTON).send_keys("testuser_122999_001@yandex.ru")

    driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("TestPass123")

    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()


