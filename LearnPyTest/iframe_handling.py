from selenium.webdriver import Chrome
driver = Chrome()
driver.get("http://toolsqa.com/iframe-practice-page/")
driver.maximize_window()

# switches focus to an iframe, can use name, ID or html
driver.switch_to.frame("iframe2")
driver.find_element("xpath", "//a[contains(text(),'Read More')]").click()

# HTML example
# driver.switch_to.frame(driver.find_element("xpath", "//iframe[@name='iframe2']"))

# Switches focus back to the original webpage (parent window)
driver.switch_to.default_content()