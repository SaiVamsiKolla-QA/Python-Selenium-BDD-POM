from behave import *
from selenium.webdriver.common.by import By

from features.Pages.login_page import LoginPage
from utilities.capture_screenshots import capture_screenshot


@given(u'I navigate to the Swag Labs login page')
def step_impl(context):
    # Verify URL
    assert "saucedemo.com" in context.driver.current_url, \
        f"Expected 'saucedemo.com' in URL, but got: {context.driver.current_url}"
    # Verify for unique elements
    assert context.driver.find_element(By.ID, "login-button").is_displayed()
    capture_screenshot(context.driver, "Login_Page")

@when(u'I enter "standard_user" in the username field')
def step_impl(context):
    context.logger.info("Entering username: standard_user")
    login_username = LoginPage(context.driver)
    login_username.enter_username("standard_user")


@when(u'I enter "secret_sauce" in the password field')
def step_impl(context):
    login_password = LoginPage(context.driver)
    login_password.enter_password("secret_sauce")


@when(u'I click the login button')
def step_impl(context):
    login_click = LoginPage(context.driver)
    login_click.click_login()


@then(u'I should be redirected to the products page')
def step_impl(context):
    # Verify URL contains the expected path
    assert "inventory.html" in context.driver.current_url, \
        f"Expected 'inventory.html' in URL, but got: {context.driver.current_url}"
    # Verify for unique products page elements
    inventory_container = context.driver.find_element(By.ID, "inventory_container")
    assert inventory_container.is_displayed(), "Inventory container not displayed"
    capture_screenshot(context.driver, "Product_Page")