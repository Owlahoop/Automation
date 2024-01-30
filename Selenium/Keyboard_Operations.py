from selenium.webdriver import Chrome
# Importing Action Chains
from selenium.webdriver.common.action_chains import ActionChains
# Importing Keys
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://www.theTestingWorld.com/testings")
driver.find_element("name", "fld_username").send_keys("Hello")

# Creating obj of Action Chains
act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').perform()
