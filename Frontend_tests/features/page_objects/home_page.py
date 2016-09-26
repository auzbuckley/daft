from base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    LOC_CATEGORY = (By.XPATH, "//*[@id='main']//a[contains(., '{0}')]")
    LOC_CITY_OR_COUNTY_DROPDOWN = (By.XPATH, "//div[@class='search-box']//span//span[contains(., 'Select county/city')]")
    LOC_CITY_OR_COUNTY_OPTION = (By.XPATH, "//span[@class='jcf-list-content']//span[contains(., '{0}')]")
    LOC_SELECT_AREA_DROPDOWN = (By.CSS_SELECTOR, "#choose-an-area a:not(.disabled)")
    LOC_SELECT_AREA_OPTION = (By.XPATH, "//span[@class='text']//label[contains(., '{0}')]")
    LOC_SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-form button")

    def select_category(self, category):
        elem = self.wait_for_element_visibility((self.LOC_CATEGORY[0], self.LOC_CATEGORY[1].format(category)))
        elem.click()

    def select_city_or_county(self, city_or_county):
        self.select_from_dropdown(self.LOC_CITY_OR_COUNTY_DROPDOWN, self.LOC_CITY_OR_COUNTY_OPTION, city_or_county)

    def select_area(self, area):
        # wait until element does not have 'disabled' class
        self.select_from_dropdown(self.LOC_SELECT_AREA_DROPDOWN, self.LOC_SELECT_AREA_OPTION, area)

    def click_search(self):
        elem = self.wait_for_element_visibility(self.LOC_SEARCH_BUTTON)
        elem.click()