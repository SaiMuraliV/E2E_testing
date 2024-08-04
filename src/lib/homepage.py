from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .basepage import BasePage

class HomePage(BasePage):

    __URL = 'https://the-internet.herokuapp.com/'
    __Heading = (By.XPATH, '//h1[@class="heading"]')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(self.__URL)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_header(self):
        return self.find_element(self.__Heading).text
