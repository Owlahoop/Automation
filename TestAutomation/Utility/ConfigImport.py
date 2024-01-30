from configparser import ConfigParser

# Created object of Configparser class
config = ConfigParser()

# To read data from config file
config.read("../Utility/config.cfg")

print(config.get("Section1", "username"))
