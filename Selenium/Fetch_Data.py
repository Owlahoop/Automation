from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select

driver = Firefox()
driver.get("http://www.thetestingworld.com/testings")

# Fetching title
print("Title of page is " + driver.title)

# Fetch URL of page
print("Page URL is " + driver.current_url)

# Fetch complete HTML of page
print("*****************************************************************")
print(driver.page_source)

# Fetch Element text
print("Text on link is " + driver.find_element("class_name", "displayPopup").text)

# Fetch Attribute value of Element
print("Value of button is " + driver.find_element("xpath", "//input[@type='submit']").get_attribute("value"))

# Selecting option in dropdown
obj = Select(driver.find_element("name", "sex"))
obj.select_by_visible_text("Male")

# Fetch selected option
print(obj.first_selected_option.text)

# Fetch all options in dropdown
#   For loop to print each option
for op in obj.options:
    print(op.text)
