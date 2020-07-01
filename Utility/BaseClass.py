import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


@pytest.mark.usefixtures("setup_teardown")
class BaseClass:

    def xpath_presence(self, xpath):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def select_text(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    @pytest.fixture(params= [("kavya", "kavya@gmail.com" , "Female"), ("satish", "satish@gmail.com", "Male")])
    def get_multiple_data(self, request):
        return request.param

    def getLogger(self):
        log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        file_handler = logging.FileHandler("logfile.log")
        file_handler.setFormatter(log_format)
        logger = logging.getLogger()
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger












