from behave import *
from selenium.webdriver import Chrome


@given(u'User is on Registration page')
def step_impl(context):
    context.driver.get('http://www.thetestingworld.com/testings')


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element("name", "fld_username").send_keys("abcd")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element("name", "fld_email").send_keys("abcd@gmail.com")


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element("name", "fld_password").send_keys("abcd")


@when(u'User clicks on signup button')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@type='submit' and @value='Sign up']").click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")


@when(u'User enters duplicate username')
def step_impl(context):
    print("Not Registered")

