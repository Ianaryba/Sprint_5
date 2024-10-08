from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Lokators import BUNS_BUTTON, SAUSES_BUTTON


def test_access_to_buns(driver):



    try:

        driver.get("https://stellarburgers.nomoreparties.site/")


        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SAUSES_BUTTON))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,BUNS_BUTTON))
        )


        print("Тест пройден удачно")

    except Exception as e:
        print(f"Тест не пройден : {e}")






