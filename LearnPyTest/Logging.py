from selenium.webdriver import Chrome
# First step: import logging
import logging

# Second step: Create log variable and set log level
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Third step:
info = logging.FileHandler('Info_logs.txt')
info.setLevel(logging.INFO)

warn = logging.FileHandler('Warning_logs.txt')
warn.setLevel(logging.WARNING)

# Fourth step: Create logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Fifth step: Apply format
info.setFormatter(formatter)
warn.setFormatter(formatter)

driver = Chrome()
driver.get("http://thetestingworld.com/testings")
driver.maximize_window()
log.info("[ My URL is Opened ]")
log.warn("[ There is delay in the opening of the browser ]")
