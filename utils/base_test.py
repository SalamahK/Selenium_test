import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BaseTest:
    def __init__(self):
        self.driver = None

    def setup(self, request):
        # Initialize the WebDriver (e.g., Chrome)
        service = Service('/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service)

        # Maximize the browser window or perform any other setup tasks
        self.driver.maximize_window()

    def teardown(self):
        # Quit the WebDriver when the test is finished
        if self.driver:
            self.driver.quit()

