Feature: Search

  Scenario: Search rental category
    Given I visit "http://www.daft.ie/"
      And I search "To Rent" and "Dublin City" and "Ballsbridge"
      And I click on advanced search
      And I perform an advanced search for "2,000", "2 bedrooms", "2 bathrooms", "Apartment to rent"
     When I submit advanced search
     Then I should see a list of results that match my search criteria
  