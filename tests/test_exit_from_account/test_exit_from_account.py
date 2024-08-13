from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_logout_from_account():
    driver = webdriver.Chrome()

    try:

        driver.get("https://stellarburgers.nomoreparties.site/")


        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > header > nav > a > p"))
        )
        login_button.click()


        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input').send_keys(
            "testuser_122999_001@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("TestPass123")


        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()


        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )


        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > header > nav > a > p"))
        )
        personal_account_button.click()


        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > main > div > nav > ul > li:nth-child(3) > button"))
        )


        logout_button.click()


        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > main > div > nav > ul > li:nth-child(3) > button"))
        )

        print("Тест пройден удачно")

    except Exception as e:
        print(f"Тест не пройден : {e}")

    finally:

        driver.quit()

test_logout_from_account()