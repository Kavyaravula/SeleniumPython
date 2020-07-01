import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Please enter valid values")


# def get_browser(request):
#     return request.config.getoption("--browser_name")


@pytest.fixture(scope="class")
def setup_teardown(request):
    browser = request.config.getoption("browser_name")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path="F:/PythonSelenium/Drivers/chromedriver.exe")
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path="F:\\PythonSelenium\\Drivers\\geckodriver.exe")
    elif browser.lower() == "ie":
        driver = webdriver.Ie(executable_path="F:\\PythonSelenium\\Drivers\\geckodriver.exe")
    else:
        print("Please select valid browser names: chrome or firefox or ie")

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.quit()



# @pytest.fixture(scope="class")
# def setup_teardown(request):
#     #driver = webdriver.Chrome(executable_path="F:/PythonSelenium/Drivers/chromedriver.exe")
#     driver = webdriver.Firefox(executable_path="F:\\PythonSelenium\\Drivers\\geckodriver.exe")
#     driver.maximize_window()
#     driver.delete_all_cookies()
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     request.cls.driver = driver
#     yield
#     driver.quit()






