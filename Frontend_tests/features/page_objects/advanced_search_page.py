from base_page import BasePage
from selenium.webdriver.common.by import By


class AdvancedSearchPage(BasePage):

    LOC_MIN_PRICE_DROPDOWN = (By.ID, "max_price")
    LOC_MIN_PRICE_OPTION = (By.XPATH, "//*[@id='max_price']//ul//li[contains(., '{0}')]")
    LOC_MAX_BEDROOMS_DROPDOWN = (By.ID, "max_bed")
    LOC_MAX_BEDROOMS_OPTION = (By.XPATH, "//*[@id='max_bed']//ul//li[contains(., '{0}')]")
    LOC_MAX_BATHROOMS_DROPDOWN = (By.ID, "max_bath")
    LOC_MAX_BATHROOMS_OPTION = (By.XPATH, "//*[@id='max_bath']//ul//li[contains(., '{0}')]")
    LOC_PROPERTY_TYPE_DROPDOWN = (By.ID, "ptId_select")
    LOC_PROPERTY_TYPE_OPTION = (By.XPATH, "//*[@id='ptId_ul']//li//span[contains(., '{0}')]")
    LOC_ADVANCED_SEARCH_SUBMIT = (By.CSS_SELECTOR, "#advanced-container span input[value='Search']")

    SEARCH_CRITERIA = {
        "max_bathrooms": None,
        "max_bedrooms": None,
        "max_price": None,
        "property_type": None
    }

    def select_max_bedrooms(self, max_bedrooms):
        self.select_from_dropdown(self.LOC_MAX_BEDROOMS_DROPDOWN, self.LOC_MAX_BEDROOMS_OPTION, max_bedrooms)
        self.SEARCH_CRITERIA["max_bedrooms"] = max_bedrooms

    def select_max_bathrooms(self, max_bathrooms):
        self.select_from_dropdown(self.LOC_MAX_BATHROOMS_DROPDOWN, self.LOC_MAX_BATHROOMS_OPTION, max_bathrooms)
        self.SEARCH_CRITERIA["max_bathrooms"] = max_bathrooms

    def select_max_price(self, max_price):
        self.select_from_dropdown(self.LOC_MIN_PRICE_DROPDOWN, self.LOC_MIN_PRICE_OPTION, max_price)
        self.SEARCH_CRITERIA["max_price"] = max_price

    def select_property_type(self, property_type):
        self.select_from_dropdown(self.LOC_PROPERTY_TYPE_DROPDOWN, self.LOC_PROPERTY_TYPE_OPTION, property_type)
        self.SEARCH_CRITERIA["property_type"] = property_type

    def click_advanced_search_button(self):
        elem = self.wait_for_element_visibility(self.LOC_ADVANCED_SEARCH_SUBMIT)
        elem.click()