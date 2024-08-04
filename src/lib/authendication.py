from selenium import webdriver
from selenium.webdriver.common.by import By
from .basepage import BasePage

class Authentication(BasePage):

    __UserName = (By.XPATH, '//input[@id="username"]')
    __Password = (By.XPATH, '//input[@id="password"]')
    __submit = (By.XPATH, '//button[@type="submit"]')
    __success_message = (By.XPATH, '//div[@id="flash"]')
    __logout = (By.XPATH, '//a[@href="/logout"]')
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def enter_username(self, username):
        self.input_text(self.__UserName, username)

    def enter_password(self, password):
        self.input_text(self.__Password, password)

    def click_submit(self):
        self.click_element(self.__submit)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
    
    def read_message(self):
        text = self.get_text(self.__success_message)
        try:
            self.click_element(self.__logout)
        except:
            print("Failed to login")
        return text