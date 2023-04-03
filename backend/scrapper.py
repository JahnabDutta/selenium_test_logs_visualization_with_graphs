from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from db import collection
from datetime import datetime
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

web_driver_path = "chromedriver.exe"
website_link = "https://www.lambdatest.com"

home_xml= '//*[@id="header"]/nav/div/div/div[1]/div/div/a'
platforms_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[1]/div[1]/a'
enterprise_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/a[1]'
pricing_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/a[2]'

paths = [home_xml,platforms_xml,enterprise_xml,pricing_xml]


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
    



scrapper  = Scrapper(web_driver_path)
scrapper.get_page(website_link)
scrapper.maximize_window()

itr = 2
while itr:
    for path in paths:
        scrapper.find_element(by="xpath",value=path).click()
        logs = scrapper.get_logs()
        for entry in logs:
            #convert the string to json
            json_entry = json.loads(entry['message'])

            
            with open('logs.json','a') as f:
                f.write(json.dumps(json_entry,indent=4))
                f.write('\n')

            collection.insert_one(json_entry)
    itr-=1

