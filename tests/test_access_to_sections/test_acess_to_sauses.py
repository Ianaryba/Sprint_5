from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_access_to_sauces():

    driver = webdriver.Chrome()

    try:

        driver.get("https://stellarburgers.nomoreparties.site/")


        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2)"))
        )

        print("Тест пройден удачно")

    except Exception as e:
        print(f"Тест не пройден : {e}")

    finally:

        driver.quit()


test_access_to_sauces()