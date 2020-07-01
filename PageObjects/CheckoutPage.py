from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    product_name = (By.XPATH, "//div[@class='card-body']//a")
    add_button = (By.XPATH, "/a[text()='Blackberry']//ancestor::div[@class='card h-100']//div[@class='card-footer']/button")
    checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def get_required_product(self):
        return self.driver.find_element(*CheckoutPage.product_name)

    def add_to_cart(self):
        return self.driver.find_element(*CheckoutPage.add_button)

    def click_checkout(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        return ConfirmPage(self.driver)




