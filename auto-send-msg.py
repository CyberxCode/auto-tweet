"""by:abdllah"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
 
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
            self.count = 0
            while self.count <= len('msg.txt'):
                self.lines = [line for line in open('msg.txt',encoding='utf-8')]
                self.Msg = self.lines[self.count]
                self.Message = self.driver.find_element(By.XPATH, '//*[@id="tweet-box-home-timeline"]').send_keys(self.Msg)
                self.clicked = self.driver.find_element(By.XPATH, '//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]').click()
                time.sleep(60)
                self.count += 1
 
 
if __name__ == '__main__':
 
    ChormTest = WebSite()
    ChormTest.SearchWebSite()
