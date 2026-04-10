# Driver Manager for Appium tests

from appium import webdriver

class DriverManager:
    def __init__(self, desired_capabilities):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()