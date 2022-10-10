from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def get_driver(self):
        return self.driver

    def wait_to_be_clickable_by_xpath(self, element):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))
        return element

    def wait_to_be_clickable_by_id(self, element):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, element)))
        return element

    def is_element_displayed(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element))).is_displayed()

