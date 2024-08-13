from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_login_with_forgot_password():

    driver = webdriver.Chrome()

    try:

        driver.get("https://stellarburgers.nomoreparties.site/login")


        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > main > div > div > p:nth-child(2) > a"))
        )


        personal_account_button.click()


        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > main > div > form > fieldset > div > div > input'))
        )

        email_field.send_keys("testuser_122999_001@yandex.ru")



        login_button = driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button')
        login_button.click()




        print("Тест через форму регистрации пройден")

    except Exception as e:
        print(f"Тест провален : {e}")

    finally:

        driver.quit()


test_login_with_forgot_password()