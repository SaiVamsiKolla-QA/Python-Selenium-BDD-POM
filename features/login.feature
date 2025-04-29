Feature: Swag Labs Authentication

  Scenario: Successful login with standard user credentials
    Given I navigate to the Swag Labs login page
    When I enter "standard_user" in the username field
    And I enter "secret_sauce" in the password field
    And I click the login button
    Then I should be redirected to the products page
    And I should see the inventory of products

  Scenario: Failed login with invalid credentials
    Given I navigate to the Swag Labs login page
    When I enter "invalid_user" in the username field
    And I enter "wrong_password" in the password field
    And I click the login button
    Then I should see an error message "Epic sadface: Username and password do not match any user in this service"
    And I should remain on the login pagels