import configparser


# section is the section targeted in the config file
# key is the variable in which you want to read data from
def read_config_data(section, key):
    # creates object of configparser
    config = configparser.ConfigParser()
    # reads the configuration files
    config.read(".\\ConfigurationFiles\\Config.cfg")
    return config.get(section, key)


# Does the same thing, but for the elements.cfg
def fetch_element_locators(section, key):
    config = configparser.ConfigParser()
    config.read(".\\ConfigurationFiles\\Elements.cfg")
    return config.get(section, key)
