from selenium.webdriver import Chrome
# Importing Action Chains
from selenium.webdriver.common.action_chains import ActionChains
# Importing Keys
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://www.thetestingworld.com")

# Create element for ActionChains
act = ActionChains(driver)

# Uses mouse click (default: text cursor)
# act.click().perform()
# act.click(driver.find_element("xpath", "//a[text()='Login']")).perform()

# Uses right click (default: text cursor)
# act.context_click().perform()

# Uses double click (default: text cursor)
# act.double_click().perform()

# Hovers over element (drop down box)
act.move_to_element(driver.find_element("xpath", "//span[contains(text(),'TUTORIAL')]")).perform()