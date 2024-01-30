from selenium.webdriver import Chrome
import pytest

a = 101


# Executes this function before all test cases
# scope="module" means it will execute only once instead of before and after each test case
@pytest.fixture(scope="module")
def driver_path():
    # Makes driver accessible to all functions
    global driver
    driver = Chrome()
    # Executes after test case
    yield
    print("Have a nice day!")


# Allows for grouping test cases
@pytest.mark.Smoke
def test_registration_data(driver_path):
    driver.get("http://www.thetestingworld.com/testings")
    # Compares result with expected result, if failed then console will print error
    assert driver.title == "Login & Sign Up Forms"


# Will skip the test case
@pytest.mark.skip("Don't execute on current build")
@pytest.mark.Sanity
def test_registration_data_1(driver_path):
    driver.get("http://www.thetestingworld.com/testings")


# Will skip test case based on a condition
@pytest.mark.skip(a > 100, reason="a is greater than 100")
@pytest.mark.Sanity
def test_registration_data_2(driver_path):
    driver.get("http://www.thetestingworld.com/testings")
