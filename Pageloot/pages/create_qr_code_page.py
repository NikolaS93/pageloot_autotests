from Pageloot.base.basepage import BasePage


dynamic_qr_website = '//div[contains(text(),"Website")]'
qr_name = '//input[@formcontrolname="name"]'
qr_link = '//input[@data-placeholder="https://pageloot.com/"]'
next_button = '//span[contains(text(),"Next")]'
shortlink = 'qr-shortlink'
preview_qr_image = '//div[@class="preview-qr__view-container"]'
save_button = '//span[contains(text(),"Save")]'
name_error_message = '//mat-error[contains(text()," You must include a name ")]'
link_error_message = '//mat-error[contains(text(),"Enter a valid URL")]'
qr_created_confirmation_message = '//div[@aria-label="QR Code changes saved"]'


class CreateQRCode(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def create_website_qr_code(self, ):
        """Clicks Website QR code"""
        self.wait_to_be_clickable_by_xpath(dynamic_qr_website).click()

    def enter_qr_code_content(self, name, link):
        """Populates Content of the QR code"""
        self.wait_to_be_clickable_by_xpath(qr_name).send_keys(name)
        self.wait_to_be_clickable_by_xpath(qr_link).send_keys(link)

        self.is_element_displayed(shortlink)
        self.is_element_displayed(preview_qr_image)

        self.wait_to_be_clickable_by_xpath(next_button).click()

    def confirm_qr_code_design(self):
        """Confirm QR code design"""
        self.wait_to_be_clickable_by_xpath(save_button).click()

    def verify_qr_confirmation_message(self):
        """Verifies that confirmation message 'QR Code changes saved' is displayed"""
        self.is_element_displayed(qr_created_confirmation_message)

    def verify_type_validation(self):
        """Verifies the Name and Link fields validation messages if fields are empty"""
        self.wait_to_be_clickable_by_xpath(next_button).click()

        self.is_element_displayed(name_error_message)
        self.is_element_displayed(link_error_message)
