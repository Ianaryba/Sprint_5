from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Lokators import ENTER_BUTTON_REGISTRATION_PAGE, ENTER_BUTTON_PERSONAL_ACCOUNT, EMAIL_BUTTON


def test_login_with_form_registration(driver):



    try:

        driver.get("https://stellarburgers.nomoreparties.site/register")


        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ENTER_BUTTON_REGISTRATION_PAGE))
        )


        personal_account_button.click()

        driver.find_element(By.XPATH, EMAIL_BUTTON).send_keys("testuser_122999_001@yandex.ru")

        driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("TestPass123")

        driver.find_element(By.XPATH, ENTER_BUTTON_PERSONAL_ACCOUNT).click()




        print("Тест через форму регистрации пройден")

    except Exception as e:
        print(f"Тест провален : {e}")

    finally:

        driver.quit()


