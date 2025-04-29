from behave import *


@given(u'I navigate to the Swag Labs login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigate to the Swag Labs login page')


@when(u'I enter "standard_user" in the username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "standard_user" in the username field')


@when(u'I enter "secret_sauce" in the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "secret_sauce" in the password field')


@when(u'I click the login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the login button')


@then(u'I should be redirected to the products page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be redirected to the products page')


@then(u'I should see the inventory of products')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the inventory of products')


@when(u'I enter "invalid_user" in the username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "invalid_user" in the username field')


@when(u'I enter "wrong_password" in the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "wrong_password" in the password field')


@then(u'I should see an error message "Epic sadface: Username and password do not match any user in this service"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see an error message "Epic sadface: Username and password do not match any user in this service"')


@then(u'I should remain on the login pagels')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should remain on the login pagels')
