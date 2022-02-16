# Created by zahid at 2/15/2022
Feature: Test for lost password functionality

  Scenario: User can change password by using lost password link
    Given Open GetTop page
    When Click the user icon and verify MY ACCOUNT PAGE  is shown
    And Click Lost your password link
    And User can able to put the email
    Then Click RESET PASSWORD button