from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from db import collection, es_client
from datetime import datetime
import time


web_driver_path = "chromedriver.exe"
website_link = "https://www.lambdatest.com"

home_xml =          '/html/body/div[1]/header/nav/div/div/div[1]/div/div/a'
platform_xml =      '/html/body/div[1]/header/nav/div/div/div[2]/div/div/div[1]/div[1]/div[1]/a'
pricing_xml =    '/html/body/div[1]/header/nav/div/div/div[2]/div/div/div[1]/a[1]'

paths = [home_xml,platform_xml,pricing_xml]


class Scrapper:
    def __init__(self,web_driver_path):
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Chrome(web_driver_path,desired_capabilities=caps)

    def get_page(self,url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def find_element(self,by,value):
        return self.driver.find_element(by=by,value=value)
    
    def get_logs(self):
        logs = self.driver.get_log('performance')
        return logs
    




def main(itr=100):
    scrapper  = Scrapper(web_driver_path)
    scrapper.get_page(website_link)
    scrapper.maximize_window()

    
    while itr:
        for path in paths:
            print("Clicking on path: " + path)
            scrapper.find_element(by="xpath",value=path).click()
            time.sleep(5)
            logs = scrapper.get_logs()
            for entry in logs:
                message = entry['message']
                collection.insert_one(json.loads(message))
            

                
        itr-=1

