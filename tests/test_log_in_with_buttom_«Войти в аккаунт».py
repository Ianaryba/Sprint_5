from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Lokators import LOGIN_WITH_BUTTON_ON_MAIN_PAGE, EMAIL_BUTTON, ENTER_BUTTON_PERSONAL_ACCOUNT


def test_login_button(driver):



    try:

        driver.get("https://stellarburgers.nomoreparties.site/")


        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LOGIN_WITH_BUTTON_ON_MAIN_PAGE))
        )


        login_button.click()

        driver.find_element(By.XPATH, EMAIL_BUTTON).send_keys("testuser_122999_001@yandex.ru")

        driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("TestPass123")

        driver.find_element(By.XPATH, ENTER_BUTTON_PERSONAL_ACCOUNT).click()


        print("Тест пройден удачно")

    except Exception as e:
        print(f"Тест не пройден : {e}")

