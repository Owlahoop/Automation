from Base import InitiateDriver
from Pages import RegistrationPage
import pytest
from DataGenerate import DataGen


# pytest is storing the list data from data_generator to the data variable
@pytest.mark.parametrize('data', DataGen.data_generator())
def test_validate_registration(data):
    driver = InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
