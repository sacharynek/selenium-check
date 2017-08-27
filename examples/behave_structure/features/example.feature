Feature: Login User
  Scenario: Success login
    Given User exist
    When I go to login page
    And Fill login form
    And Click submit button
    Then I am logged in