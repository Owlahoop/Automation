from Library import ConfigReader


class RegistrationClass:

    # Constructor, necessary
    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element("name",
                            ConfigReader.fetch_element_locators("Registration", "user_name")).send_keys(username)

    def enter_email(self, email):
        driver.find_element("name",
                            ConfigReader.fetch_element_locators("Registration", "email_name")).send_keys(email)

    def enter_password(self, password):
        driver.find_element("name",
                            ConfigReader.fetch_element_locators("Registration", "password_name")).send_keys(password)
