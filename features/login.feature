Feature: Login to OrangeHRM

@smoke
  Scenario: Successful login with valid credentials
    Given the user is on the OrangeHRM login page
    When the user enters valid username "Admin" and password "admin123"
    And the user clicks the login button
    Then the user should be redirected to the dashboard page
    And the dashboard title should contain "OrangeHRM"
#
#  Scenario Outline: Login with invalid credentials
#    Given the user is on the OrangeHRM login page
#    When the user enters invalid username "<username>" and password "<password>"
#    And the user clicks the login button
#    Then an error message should be displayed containing "<error_message>"
#
#    Examples:
#      | username             | password      | error_message                       |
#      | AdminInvalid         | admin123      | Invalid credentials                   |
#      | Admin                | InvalidPass   | Invalid credentials                   |
#      |                      | admin123      | Required                              |
#      | Admin                |               | Required                              |