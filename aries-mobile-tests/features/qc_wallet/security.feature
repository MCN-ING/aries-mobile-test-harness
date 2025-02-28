@SecurityQC @qc_wallet
Feature: Secure your Wallet 
  In order to be reassured that my digital wallet will not be used maliciously
  As a person who is curious but cautious of digital wallets
  I want to set my security settings to maximum security


  @T001-Security @AcceptanceTest @normal @critical
  Scenario: New User Sets Up PIN
    Given the User has accepted the Terms and Conditions
    And the User is on the PIN creation screen
    When the User enters the first PIN as "369369"
    And the User re-enters the PIN as "369369"
    And the User selects Create PIN
    Then the User transitions to biometric screen


  @T002-Security @FunctionalTest @ExceptionTest @normal 
  Scenario Outline: New User Sets Up PIN but does not follow conventions
    Given the User has accepted the Terms and Conditions
    And the User is on the PIN creation screen
    When the User enters the first PIN as <pin>
    And the User re-enters the PIN as <pin> 
    And the User selects Create PIN
    Then they are informed of <pin_error> 

    Examples:
      | pin    | pin_error                                                            |
      | @28193 | Your PIN needs to only contain digits. Please try again.             |
      | D28193 | Your PIN needs to only contain digits. Please try again.             |
      | 123893 | A series was detected in your PIN. Please try again.                 |
      | 333752 | The PIN can't have a repetition of the same digit. Please try again. |
      | 65237  | Your PIN is too short. Please try again.                             |

  @T003-Security @FunctionalTest @ExceptionTest @normal
  Scenario: New User Sets Up PIN and checks pin by toggling visibility
    Given the User has accepted the Terms and Conditions
    And the User is on the PIN creation screen
    When the User enters the first PIN as "728193"
    Then they select visibility toggle on the first PIN as "728193"
    When the User re-enters the PIN as "278596"
    Then they select visibility toggle on the second PIN as "278596"

  # @TCL_PNG_ACC_009 @FunctionalTest @extra_config_security_idle_timeout @test04
  # Scenario: Holder has app locked after 5 minutes of inactivity
  #   Given the Holder has setup thier Wallet
  #   When the Holder stops interacting with the app 
  #   Then the app is locked for security reasons and a message is shown to the Holder
  #     | lock_time | lock_message      |
  #     | 300       | You're logged out |


  @T004-Security @AcceptanceTest @normal @critical
  Scenario: New User Sets Up PIN and connect to the application
    Given the User has accepted the Terms and Conditions
    And the User is on the PIN creation screen
    When the User enters the first PIN as "369369"
    And the User re-enters the PIN as "369369"
    And the User selects Create PIN
    Then the User transitions to biometric screen
    When the user click continue on the biometrics screen 
    Then the user land on the Home screen

  @T005-Security @AcceptanceTest @normal  @critical
  Scenario: New User Sets Up PIN and connect to the application with biometrics enabled
    Given the User has accepted the Terms and Conditions
    And the User is on the PIN creation screen
    When the User enters the first PIN as "369369"
    And the User re-enters the PIN as "369369"
    And the User selects Create PIN
    Then the User transitions to biometric screen
    When the user enable using biometrics to unlock wallet
    And the user click continue on the biometrics screen 
    Then the user land on the Home screen

  # PIN Update Tests
  # In order to keep my wallet secure with a stronger PIN
  # As a wallet user i want to change my wallet PIN

  @T006.1-Security @AcceptanceTest @critical
  Scenario: Wallet User Changes PIN
    Given the user has setup thier wallet 
    When the user updates thier PIN to "963963"
    Then the modal Successfully changed your PIN appears
    When the user click Okay in the modal Successfully changed your PIN
    Then the user land on the settings screen
    When the user go check the history page
    Then notification wallet pin update is added in the history page

  @T006.2-Security @FunctionalTest @ExceptionTest @normal
  Scenario: Wallet User Changes PIN but PINs do not match
    Given the user has setup thier wallet
    And the user wants to update thier PIN
    When the user enters thier old PIN as "369369"
    And the user enters thier first PIN as "963963"
    And they select visibility toggle on the first PIN as "963963"
    And the User re-enters the PIN as "369363"
    And they select visibility toggle on the first PIN as "963963"
    And the User selects Change PIN
    Then they are informed that the PINs do not match
    When the User re-enters the PIN as "963963"
    And they select visibility toggle on the first PIN as "963963"
    And the User selects Change PIN
    # And the User has successfully updated PIN
    Then the modal Successfully changed your PIN appears
    When the user click Okay in the modal Successfully changed your PIN
    And the user close and relaunch the application
    Then they have access to the app with the new PIN

  @T006.3-Security @FunctionalTest @ExceptionTest @normal @qc_wallet_not
  Scenario Outline: User Changes PIN but does not follow conventions
    Given the user has setup thier wallet
    And the user wants to update thier PIN
    When the user enters thier old PIN as "369369"
    When the User enters the first PIN as <pin>
    And the User re-enters the PIN as <pin>
    And the User selects Change PIN
    Then they are informed of <pin_error>

    Examples:
      | pin    | pin_error                                                |
      | 2357   | Your PIN is too short. Please try again.                 |
      | 27463A | Your PIN needs to only contain digits. Please try again. |