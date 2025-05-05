Feature: Swag Labs Authentication


  Scenario: Successful login with standard user credentials
    Given I navigate to the Swag Labs login page
    When I enter "standard_user" in the username field
    And I enter "secret_sauce" in the password field
    When I click the login button
    Then I should be redirected to the products page


