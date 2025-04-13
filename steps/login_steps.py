from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.browser_manager import BrowserManager

@given('the user is on the OrangeHRM login page')
def step_impl(context):
    context.login_page = LoginPage(context.browser)
    context.login_page.load()

@when('the user enters valid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('the user enters invalid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('the user clicks the login button')
def step_impl(context):
    context.login_page.click_login()

@then('the user should be redirected to the dashboard page')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
    EC.title_contains("OrangeHRM")
    )
    assert "OrangeHRM" in context.browser.title

@then('the dashboard title should contain "{expected_title}"')
def step_impl(context, expected_title):
    WebDriverWait(context.browser, 10).until(
    EC.title_contains(expected_title)
    )
    assert expected_title in context.browser.title

@then('an error message should be displayed containing "{error_message}"')
def step_impl(context, error_message):
    WebDriverWait(context.browser, 10).until(
    EC.visibility_of_element_located(LoginPage.LOCATORS['invalid_credentials']))
    actual_error = context.login_page.get_error_message()
    assert error_message in actual_error