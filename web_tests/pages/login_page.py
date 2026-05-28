from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def acessar_site(self):

        self.driver.get(
            "https://www.saucedemo.com/"
        )

    def fazer_login(self):

        username = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        username.send_keys("standard_user")

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        self.driver.find_element(
            By.ID,
            "login-button"
        ).click()