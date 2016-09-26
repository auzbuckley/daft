from behave import *
from page_objects.home_page import HomePage
from page_objects.results_page import ResultsPage
from page_objects.advanced_search_page import AdvancedSearchPage
from random import randint
import logging

LOG = logging.getLogger(__name__)


@given('I visit "{url}"')
def step_impl(context, url):
    context.homepage = HomePage(context)
    context.homepage.navigate_to(url)


@given('I search "{category}" and "{city_or_county}" and "{area}"')
def step_impl(context, category, city_or_county, area):
    context.homepage.select_category(category)
    context.homepage.select_city_or_county(city_or_county)
    context.homepage.select_area(area)
    context.homepage.click_search()


@given('I click search')
def step_impl(context):
    context.homepage.click_search()


@given('I click on advanced search')
def step_impl(context):
    context.resultspage = ResultsPage(context)
    context.resultspage.click_advanced_search()


@given('I perform an advanced search for "{max_price}", "{max_bedrooms}", "{max_bathrooms}", "{property_type}"')
def step_impl(context, max_price, max_bedrooms, max_bathrooms, property_type):
    context.advancedsearchpage = AdvancedSearchPage(context)
    context.advancedsearchpage.select_max_price(max_price)
    context.advancedsearchpage.select_max_bedrooms(max_bedrooms)
    context.advancedsearchpage.select_max_bathrooms(max_bathrooms)
    context.advancedsearchpage.select_property_type(property_type)


@when('I submit advanced search')
def step_impl(context):
    context.advancedsearchpage.click_advanced_search_button()
    
    
@then('I should see a list of results that match my search criteria')
def step_impl(context):
    number = randint(1, 10)
    item = context.resultspage.get_item(number)
    item_price = context.resultspage.get_item_price(item)
    max_price = context.advancedsearchpage.SEARCH_CRITERIA["max_price"]
    try:
        assert item_price <= max_price
    except AssertionError:
        print("{0} is not less than or equal to {1}".format(item_price, max_price))
        raise
        
    item_number_of_beds = context.resultspage.get_item_number_of_beds(item)
    max_bedrooms = context.advancedsearchpage.SEARCH_CRITERIA["max_bedrooms"]
    try:
        assert item_number_of_beds <= max_bedrooms
    except AssertionError:
        print("{0} is not less than or equal to {1}".format(item_number_of_beds, max_bedrooms))
        raise
        
    item_number_of_baths = context.resultspage.get_item_number_of_baths(item)
    max_bathrooms = context.advancedsearchpage.SEARCH_CRITERIA["max_bathrooms"]
    try:
        assert item_number_of_baths <= max_bathrooms
    except AssertionError:
        print("{0} is not less than or equal to {1}".format(item_number_of_baths, max_bathrooms))
        raise
        
    item_property_type = context.resultspage.get_item_property_type(item)
    property_type = context.advancedsearchpage.SEARCH_CRITERIA["property_type"]
    try:
        assert property_type.lower() in item_property_type.lower()
    except AssertionError:
        print("{0} is not in {1}".format(property_type, item_property_type))
        raise
