from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Lokators import EMAIL_BUTTON, REGISTRATION_BUTTON


def test_registration_with_invalid_password(driver):



    

        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys("TestUser")

        driver.find_element(By.XPATH, EMAIL_BUTTON).send_keys("testuser_122999_001@yandex.ru")

        driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("12345")

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()


        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.input__error'))
        )


        error_message_text = error_message_element.text


        print(f"Некорректный пароль : {error_message_text}")


        if "Некорректный пароль" not in error_message_text:
            print("Не правильное ссобщение об ошибке")
            print(f"Некорректный пароль : {error_message_text}")
            assert False, "Не правильное ссобщение об ошибке"


