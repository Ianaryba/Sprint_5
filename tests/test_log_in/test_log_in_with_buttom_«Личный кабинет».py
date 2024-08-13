from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_login_via_personal_account():

    driver = webdriver.Chrome()

    try:

        driver.get("https://stellarburgers.nomoreparties.site/")


        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > header > nav > a > p"))
        )


        personal_account_button.click()


        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input'))
        )
        password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]')


        email_field.send_keys("testuser_122999_001@yandex.ru")
        password_field.send_keys("TestPass123")


        login_button = driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button')
        login_button.click()


        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        print("Тест через кнопку 'Личный кабинет' пройден")

    except Exception as e:
        print(f"Тест провален : {e}")

    finally:

        driver.quit()


test_login_via_personal_account()