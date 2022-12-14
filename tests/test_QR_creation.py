from Pageloot.base.__init__ import WebApp
from Pageloot.pages.login_page import LoginPage
from Pageloot.pages.dashboard_page import DashboardPage
from Pageloot.pages.create_qr_code_page import CreateQRCode
import unittest


class TestQRCreation(unittest.TestCase):

    driver = None

    def setUp(self):
        self.driver = WebApp.start()
        self.LoginPage = LoginPage(self.driver)
        self.DashboardPage = DashboardPage(self.driver)
        self.CreateQRCode = CreateQRCode(self.driver)

    def test_qr_website_creation(self):
        self.LoginPage.login(email="nikola.stankovic@live.com", password="Test@123")
        self.DashboardPage.open_dashboard()
        self.DashboardPage.create_qr_code()
        self.CreateQRCode.create_website_qr_code()
        self.CreateQRCode.enter_qr_code_content("QR code name test", "www.google.com")
        self.CreateQRCode.confirm_qr_code_design()
        self.CreateQRCode.verify_qr_confirmation_message()

    def test_qr_website_content_validation(self):
        self.LoginPage.login(email="nikola.stankovic@live.com", password="Test@123")
        self.DashboardPage.create_qr_code()
        self.CreateQRCode.create_website_qr_code()
        self.CreateQRCode.verify_type_validation()

    def tearDown(self):
        WebApp.quit()
