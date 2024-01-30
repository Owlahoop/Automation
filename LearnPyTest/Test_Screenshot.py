from selenium.webdriver import Chrome
import Screenshot_Function
driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")
driver.maximize_window()
Screenshot_Function.take_page_screenshot(driver, "test_screenshot")
