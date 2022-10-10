from Pageloot.base.basepage import BasePage
import time


email_input = "mat-input-0"
password_input = "mat-input-1"
log_in_button = '//span[contains(text()," Log in ")]'
dashboard = '//a[@href="/dashboard/all"]'


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        """Login and verify dashboard presence to assert that is logged in"""

        self.wait_to_be_clickable_by_id(email_input).send_keys(email)
        self.wait_to_be_clickable_by_id(password_input).send_keys(password)
        self.wait_to_be_clickable_by_xpath(log_in_button).click()

        # Sometimes it gives to resolve CAPTCHA, so this is a time to manually be solved
        time.sleep(10)

        self.is_element_displayed(dashboard)
