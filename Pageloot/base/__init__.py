from selenium import webdriver
import os


class WebApp:

    driver: webdriver = None

    @classmethod
    def start(cls, url='https://app.pageloot.com/auth/login'):
        """Creates instance of browser"""

        executable_path = os.path.join(os.path.dirname(__file__), '../../drivers/chromedriver')

        cls.driver = webdriver.Chrome(executable_path)
        cls.driver.maximize_window()
        cls.driver.get(url)

        return cls.driver

    # Quit app
    @classmethod
    def quit(cls):
        cls.driver.quit()
