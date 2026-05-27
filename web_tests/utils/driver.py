from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def iniciar_driver():

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    return driver