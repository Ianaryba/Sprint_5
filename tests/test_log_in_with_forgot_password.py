from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Lokators import FORGOT_PASSWORD_BUTTON, EMAIL_BUTTON, RESTORE_BUTTON


def test_login_with_forgot_password(driver):


    try:

        driver.get("https://stellarburgers.nomoreparties.site/login")


        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FORGOT_PASSWORD_BUTTON))
        )


        personal_account_button.click()


        driver.find_element(By.XPATH, EMAIL_BUTTON).send_keys("testuser_122999_001@yandex.ru")



        login_button = driver.find_element(By.XPATH, RESTORE_BUTTON)

        login_button.click()




        print("Тест через форму восстановления пароля пройден")

    except Exception as e:
        print(f"Тест провален : {e}")

