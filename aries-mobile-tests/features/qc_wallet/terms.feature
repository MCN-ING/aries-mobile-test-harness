@TermsAndConditionsQC @qc_wallet @normal
Feature: Terms and Conditions
  In order to understand my legal obligations when using the app
  As a new holder, i want to review the terms and conditions

  @T01-TandC @AcceptanceTest
  Scenario: User Accepts Terms and Conditions
    Given the User is on the Terms and Conditions screen
    When the users accepts the Terms and Conditions
    And the user clicks continue
    Then the user transitions to the PIN creation screen

  @T02-TandC @AcceptanceTest
  Scenario: User don't Accepts Terms and Conditions
    Given the User is on the Terms and Conditions screen
    When the user clicks continue without accepting the Terms and Conditions
    Then the user is on the Terms and Conditions screen

  @T03-useAppGuides @AcceptanceTest
  Scenario: the user chooses to use app guides
    Given the user has setup the wallet
    And the user land on the Home screen and the modal welcome to QC Wallet is displayed
    When the user chooses to use app guides
    Then the add and share credentials modal appears
    When the user click next
    Then the notifications modal appears
    When the user click next 
    Then your credentials modal appears
    When the user click done button 
    Then the user land on the Home screen after using app guides

  @T04-useAppGuides @AcceptanceTest
  Scenario: the user land on the Home screen after choosing "Don't use app guides" button
    Given the user has setup the wallet
    And the user land on the Home screen and the modal welcome to QC Wallet is displayed
    When the user click "Don't use app guides" button 
    Then the user land on the Home screen
