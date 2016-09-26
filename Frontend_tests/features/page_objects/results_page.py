from base_page import BasePage
import re
import logging
from selenium.webdriver.common.by import By


class ResultsPage(BasePage):

    LOC_ADVANCED_SEARCH = (By.XPATH, "//*[@class='search-form']//a[contains(., 'Advanced')]")
    LOC_ITEM = (By.XPATH, "//*[@id='sr_content']//div[@class='box'][contains(., '{0}. ')]")
    LOC_ITEM_PRICE = "div.text-block div.info-box strong.price"
    LOC_ITEM_PROPERTY_TYPE = "div.info-box ul.info li:nth-of-type(1)"
    LOC_ITEM_NUMBER_OF_BEDS = "div.info-box ul.info li:nth-of-type(2)"
    LOC_ITEM_NUMBER_OF_BATHS = "div.info-box ul.info li:nth-of-type(3)"

    def _find_number_within_text(self, text):
        number = re.sub('[^0-9,]', "", text)
        return number
        
    def _find_text_of_child_elem(self, parent, child):
        return parent.find_element_by_css_selector(child).text
        
    def click_advanced_search(self):
        elem = self.wait_for_element_visibility(self.LOC_ADVANCED_SEARCH)
        elem.click()
        
    def get_item(self, number):
        elem = self.wait_for_element_visibility((self.LOC_ITEM[0], self.LOC_ITEM[1].format(number)))
        return elem
        
    def get_item_price(self, item):
        return self._find_number_within_text(self._find_text_of_child_elem(item, self.LOC_ITEM_PRICE))
        
    def get_item_property_type(self, item):
        property_type = item.find_element_by_css_selector(self.LOC_ITEM_PROPERTY_TYPE).text
        return property_type
        
    def get_item_number_of_beds(self, item):
        return self._find_number_within_text(self._find_text_of_child_elem(item, self.LOC_ITEM_NUMBER_OF_BEDS))
        
    def get_item_number_of_baths(self, item):
        return self._find_number_within_text(self._find_text_of_child_elem(item, self.LOC_ITEM_NUMBER_OF_BATHS))
    