from Base import InitiateDriver
from Pages import RegistrationPage


def test_registration_invalid_data():
    driver = InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_email("4321")
