from behave import *
from selenium.webdriver.common.by import By


@given(u'I navigate to the Swag Labs login page')
def step_impl(context):
    # Verify URL
    assert "saucedemo.com" in context.driver.current_url, \
        f"Expected 'saucedemo.com' in URL, but got: {context.driver.current_url}"
    # Verify for unique elements
    assert context.driver.find_element(By.ID, "login-button").is_displayed()


@when(u'I enter "standard_user" in the username field')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")


@when(u'I enter "secret_sauce" in the password field')
def step_impl(context):
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")


@when(u'I click the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then(u'I should be redirected to the products page')
def step_impl(context):
    # Verify URL contains the expected path
    assert "inventory.html" in context.driver.current_url, \
        f"Expected 'inventory.html' in URL, but got: {context.driver.current_url}"
    # Verify for unique products page elements
    inventory_container = context.driver.find_element(By.ID, "inventory_container")
    assert inventory_container.is_displayed(), "Inventory container not displayed"


@when(u'I enter "invalid_user" in the username field')
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("invalid_user")


@when(u'I enter "wrong_password" in the password field')
def step_impl(context):
    context.driver.find_element(By.ID, "password").send_keys("secrt_sauce")


@then(u'I should see an error message "Epic sadface: Username and password do not match any user in this service"')
def step_impl(context):
    error_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    # Verify error message is displayed
    assert error_element.is_displayed(), "Error message element is not displayed"


@then(u'I should remain on the login page')
def step_impl(context):
    # Verify URL
    assert "saucedemo.com" in context.driver.current_url, \
        f"Expected 'saucedemo.com' in URL, but got: {context.driver.current_url}"
    # Verify for unique elements
    assert context.driver.find_element(By.ID, "login-button").is_displayed()
