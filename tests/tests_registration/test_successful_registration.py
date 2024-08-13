from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()


driver.get("https://stellarburgers.nomoreparties.site/register")


driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys("TestUser")


driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys("testuser_122999_001@yandex.ru")


driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("TestPass123")


driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()


driver.quit()