Feature: Myntra browsing
  Scenario: User visiting myntra page
    When  user on home page.
    When user enters top on search bar
    When user clicks "search" button
    Then user enters new site
    Then user selects size
    Then user clicks add to bag
    When user has navigates to add to bag
    And close browser
