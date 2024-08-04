from selenium import webdriver
from selenium.webdriver.common.by import By
from .basepage import BasePage
from .authendication import Authentication

class HomePage(BasePage):

    __URL = 'https://the-internet.herokuapp.com/'
    __Heading = (By.XPATH, '//h1[@class="heading"]')
    __Authendication = (By.XPATH, '//a[@href="/login"]')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(self.__URL)

    def get_header(self):
        return self.find_element(self.__Heading).text

    def click_authendication(self):
        self.click_element(self.__Authendication)
        return Authentication(self.driver)