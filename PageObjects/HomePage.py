from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop_menu = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    gender = (By.ID, "exampleFormControlSelect1")
    sunmit = (By.XPATH, "//input[@value='Submit']")
    sucess_msg = (By.XPATH ,"//div[@class='alert alert-success alert-dismissible']")


    def navigate_to_shop(self):
        self.driver.find_element(*HomePage.shop_menu).click()
        return CheckoutPage(self.driver)

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def submit_button(self):
        return self.driver.find_element(*HomePage.sunmit)

    def get_success(self):
        return self.driver.find_element(*HomePage.sucess_msg)


