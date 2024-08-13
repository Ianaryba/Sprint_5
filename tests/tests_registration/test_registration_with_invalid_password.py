from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_registration_with_invalid_password():

    driver = webdriver.Chrome()

    try:

        driver.get("https://stellarburgers.nomoreparties.site/register")


        driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys("TestUser")


        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys(
            "testuser_1999_002@yandex.ru")


        driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]').send_keys("12345")


        driver.find_element(By.CSS_SELECTOR, '#root > div > main > div > form > button').click()


        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.input__error'))
        )


        error_message_text = error_message_element.text


        print(f"Некорректный пароль : {error_message_text}")


        if "Некорректный пароль" not in error_message_text:
            print("Не правильное ссобщение об ошибке")
            print(f"Некорректный пароль : {error_message_text}")
            assert False, "Не правильное ссобщение об ошибке"

    finally:

        driver.quit()



test_registration_with_invalid_password()