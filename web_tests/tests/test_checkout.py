from web_tests.utils.driver import iniciar_driver
from web_tests.pages.login_page import LoginPage
from web_tests.pages.products_page import ProductsPage
from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_page import CheckoutPage


def test_fluxo_completo_checkout():

    driver = iniciar_driver()

    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.acessar_site()

    login.fazer_login()

    products.adicionar_produto_no_carrinho()

    products.abrir_carrinho()

    cart.ir_para_checkout()

    checkout.preencher_checkout()

    checkout.finalizar_compra()

    mensagem = checkout.validar_compra_finalizada()

    assert mensagem == "Thank you for your order!"

    driver.quit()