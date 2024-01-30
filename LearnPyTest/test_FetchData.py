from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
import time
import pytest


@pytest.fixture()
def environment_setup():
    global driver
    driver = Chrome()
    # Sets amount of time to give page to load, must be before driver.get(url) (default=30)
    driver.set_page_load_timeout(30)
    driver.get("http://thetestingworld.com/testings")
    # (Implicit Wait) Waits x amount of time if driver cannot find element
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()


def test_verify_registration(environment_setup):
    # (Explicit Wait) Waits for dropdown to load, max wait time
    wait = WebDriverWait(driver, 20)

    # Work on dropdowns
    wait.until(text_to_be_present_in_element((By.NAME, "sex"), "Male"))
    obj = Select(driver.find_element("name", "sex"))
    obj.select_by_visible_text("Male")

    wait.until(text_to_be_present_in_element((By.ID, "countryID"), "India"))
    obj = Select(driver.find_element("id", "countryID"))
    obj.select_by_visible_text("India")

    wait.until(text_to_be_present_in_element((By.ID, "stateID"), "Delhi"))
    obj = Select(driver.find_element("id", "stateID"))
    obj.select_by_visible_text("Delhi")

    # Waits x amount of seconds
    time.sleep(0)

    # Work on radio button
    driver.find_element("xpath", "//input[@value='office']").click()

    # Work on checkbox
    driver.find_element("name", "terms").click()

    # Work on button
    driver.find_element("xpath", "//input[@type='submit']").click()

    # Work on links
    driver.find_element("link_text", "Read Detail").click()
