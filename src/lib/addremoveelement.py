from selenium import webdriver
from selenium.webdriver.common.by import By
from .basepage import BasePage

class AddRemoveElement(BasePage):
    __Header = (By.XPATH, '//h3')
    __AddButton = (By.XPATH, '//button[text()="Add Element"]')
    __DeleteButton = (By.XPATH, '//button[text()="Delete"]')

    def __init__(self, driver):
        super().__init__(driver)
        
    def get_header(self):
        return self.get_text(self.__Header)
    
    def addbutton(self, count=1):
        for _ in range(count):
            self.click_element(self.__AddButton)

    def deletebutton(self, count=1):
        elements = self.find_elements(self.__DeleteButton)
        if count > len(elements):
            print("Not enough delete buttons to delete")
            return False
        else:
            for _ in range(count):
                elements[_].click()
        return True