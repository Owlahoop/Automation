from selenium.webdriver import Chrome


def before_all(context):
    context.driver = Chrome()


def after_all(context):
    context.driver.close()
