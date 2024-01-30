from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader


def start_browser():
    global driver

    if ConfigReader.read_config_data('Details', 'Browser') == "chrome":
        driver = Chrome()
    elif ConfigReader.read_config_data('Details', 'Browser') == "firefox":
        driver = Firefox()
    else:
        driver = Chrome()

    driver.get(ConfigReader.read_config_data('Details', 'Application_URL'))
    driver.maximize_window()
    return driver


def close_browser():
    driver.close()
