from selenium.webdriver import Chrome
driver = Chrome()
driver.get("http://www.thetestingworld.com/testings")
driver.maximize_window()
# Used for executing java script, scrolls 400 pixels down
driver.execute_script("window.scrollTo(0,400);")
