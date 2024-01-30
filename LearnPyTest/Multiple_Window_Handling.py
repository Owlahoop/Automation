from selenium.webdriver import Chrome
driver = Chrome()
driver.get("https://www.naukri.com")
driver.maximize_window()
# Used for handling multiple windows, stores all unique window ID's in the Allwindows variable
Allwindows = driver.window_handles
# Used as an empty variable to place the main window url in
mainWin = ""
# Prints the unique window values for each window
print(Allwindows)

# for loop that cycles through each window and then closes any window that isn't the target
# places target url in mainWin
for win in Allwindows:
    driver.switch_to.window(win)
    if driver.current_url == "https://www.naukri.com":
        mainWin = win
    else:
        driver.close()

# Switches control back to the target url
driver.switch_to.window(mainWin)

# **************************************************************************
# This section is for handling multiple tabs, but is not executable code

# Stores all tab unique window ID's into the allTabs variable
allTabs = driver.window_handles
# prints all window ID's
print(allTabs)

# for loop cycles through tabs until it matches the url and clicks a specific element
for tab in allTabs:
    driver.switch_to.window(tab)
    if driver.current_url == "":
        driver.find_element("xpath", "").click()
