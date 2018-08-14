"""by:abdllah"""
from selenium import webdriver
from selenium.webdriver.common.by import By
 
import os
 
class WebSite():
 
    def SearchWebSite(self):
 
        self.userTwitter = 'email@gmail.com' # your username in Twitter
        self.passTwitter = 'password' # your password in Twitter
 
        self.webLocation = 'C:\\Projects\\webDriver\\chromedriver.exe' # Program chromdriver.exe Browser
        os.environ["webdriver.chrome.webdriver"] = self.webLocation #
        self.driver = webdriver.Chrome(self.webLocation)
        self.driver.get('https://www.twitter.com/login') # url website
        self.username = self.driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys(self.userTwitter)
        self.password = self.driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(self.passTwitter)
        self.sumbit = self.driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/div[2]/button').submit()
 
 
        if self.driver is not None:
            Msg = 'Test Message , Welcome Back in Twitter' # The Message
            self.Message = self.driver.find_element(By.XPATH,'//*[@id="tweet-box-home-timeline"]').send_keys(Msg)
            if self.Message != 0:
                self.Clicked = self.driver.find_element(By.XPATH,'//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]').click()
                return self.Clicked
 
if __name__ == '__main__':
 
    ChormTest = WebSite()
    ChormTest.SearchWebSite()
