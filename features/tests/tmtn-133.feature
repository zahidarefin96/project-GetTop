# Created by zahid at 2/12/2022
Feature: Tests for GetTop Quick-View and Cart functionality

  Scenario: User can click Quick View and add product to cart
    Given Open GetTop page
    When Scroll down to “LATEST PRODUCTS ON SALE” and hover over a product
    And Click on “QUICK VIEW” tab that comes up when hovering over product
    And Click on “Add to cart” to add product to cart
    Then View that product is added to cart (Message will say product is in cart)