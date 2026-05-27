from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def preencher_checkout(self):

        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys("Erasmo")

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

        self.driver.find_element(
            By.ID,
            "finish"
        ).click()

    def validar_compra_finalizada(self):

        mensagem = self.driver.find_element(
            By.CLASS_NAME,
            "complete-header"
        ).text

        return mensagem