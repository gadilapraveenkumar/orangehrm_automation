Feature: Login to OrangeHRM

@lhn_menu_validation
  Scenario Outline: Login with valid credentials and navigate all LNH Menu
    Given the user is on the OrangeHRM login page
    When the user enters invalid username "<username>" and password "<password>"
    And the user clicks the login button
    Then Get The all LHN Menu "<TestCase>"
    Then Navigate to Each Page "<TestCase>"

    Examples:
      | TestCase | username | password |
      | TC001    | Admin    | admin123 |