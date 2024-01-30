Feature: Verifying registration functionality

    @sanity
    Scenario: Registration with valid data
    Given   User is on Registration page
    When    User enters username
    And     User enters email id
    And     User enters password
    And     User clicks on signup button
    Then    User should be registered successfully

    @sanity @smoke
    Scenario: Registration with duplicate username
    Given   User is on Registration page
    When    User enters duplicate username
    And     User enters email id
    And     User enters password
    And     User clicks on signup button
    Then    User should be registered successfully

