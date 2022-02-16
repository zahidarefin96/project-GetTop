# Created by zahid at 2/15/2022
Feature: Tests GetTop search

  Scenario: User can see the expected product by using search feature
    Given Open GetTop page
    When Click search icon
    And Input product in the search field
    Then Verify expected product is shown