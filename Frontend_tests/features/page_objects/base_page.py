import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    """
    Base class containing common attributes and methods across pages objects.
    """
    def __init__(self, context):
        self.driver = context.driver
        self.log = logging.getLogger(__name__)

    def navigate_to(self, path):
        self.log.info(self.driver)
        self.driver.get(path)

    def select_from_dropdown(self, dropdown_loc, option_loc, data):
        dropdown_elem = self.wait_for_element_visibility(dropdown_loc)
        dropdown_elem.click()
        modified_locator = (option_loc[0], option_loc[1].format(data))
        option_elem = self.wait_for_element_visibility(modified_locator)
        option_elem.click()

    def wait_for_element_visibility(self, locator, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.log.warning("Timeout occured after {0} seconds.".format(timeout))
            raise
