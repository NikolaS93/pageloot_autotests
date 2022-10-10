from Pageloot.base.basepage import BasePage


create_qr_code_button = '//a[@routerlink="/qrcodes/create"]'
dashboard = '//a[@href="/dashboard/all"]'


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_dashboard(self):
        """Clicks Dashboard hyperlink"""
        self.wait_to_be_clickable_by_xpath(dashboard).click()

    def create_qr_code(self):
        """Clicks Create QR code button"""
        self.wait_to_be_clickable_by_xpath(create_qr_code_button).click()

