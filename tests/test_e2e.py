from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utility.BaseClass import BaseClass


class TestOne(BaseClass):
    global log

    def test_end2end(self):
        global log
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Navigating to shop page")
        checkoutpage = homepage.navigate_to_shop()
        products = checkoutpage.get_products()
        for product in products:
            product_name = checkoutpage.get_required_product()
            if product_name == 'Blackberry':
                log.debug("message to see in the log")
                log.info("message")
                log.info("Selected Product: "+product_name)
                checkoutpage.add_to_cart().click()
        confirmpage = checkoutpage.click_checkout()
        confirmpage.clcik_checkout().click()
        confirmpage.enter_country().send_keys("ind")
        self.xpath_presence(confirmpage.get_xpath())
        confirmpage.select_entered_country().click()
        confirmpage.check_conditions().click()
        confirmpage.click_purchase().click()
        suceess_text = confirmpage.get_success().text
        log.info(suceess_text)
        assert "Success" in suceess_text
        #driver.get_screenshot_as_file("SS.png")







