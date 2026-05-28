from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def preencher_checkout(self):

        primeiro_nome = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        primeiro_nome.send_keys("Erasmo")

        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys("Alves")

        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys("64000000")

        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def finalizar_compra(self):

        botao_finish = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        )

        botao_finish.click()

    def validar_compra_finalizada(self):

        mensagem = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        return mensagem.text