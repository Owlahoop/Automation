# Imports Firefox
from selenium.webdriver import Firefox
# Needed for using dropdown selection
from selenium.webdriver.support.select import Select

# Website URL
driver = Firefox()
driver.get("http://www.theTestingWorld.com/testings")

# Maximize browser
driver.maximize_window()

# Enter data into text box
driver.find_element("name", "fld_username").send_keys("HelloWorld")
driver.find_element("xpath", "//input[@name='fld_email']").send_keys("testingworldindia@gmail.com")
driver.find_element("name", "fld_password").send_keys("abcd123")
driver.find_element("name", "fld_cpassword").send_keys("abcd123")
driver.find_element("name", "fld_username").clear()
driver.find_element("name", "fld_username").send_keys()

# Radio button
driver.find_element("xpath", "//input[@value='home']").click()

# Dropdown
obj = Select(driver.find_element("name", "sex"))
obj.select_by_value("2")
# obj.select_by_index(1)
# obj.select_by_visible_text("Female")

# Checkbox
driver.find_element("name", "terms").click()

# Signup Button
# driver.find_element("xpath", "//input[@type='submit']").click()

# Click link
driver.find_element("link text", "Read Detail").click()

# Close browser
driver.close()
