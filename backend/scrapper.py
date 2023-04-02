from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json


web_driver_path = "chromedriver.exe"
website_link = "https://www.lambdatest.com"

home_xml= '//*[@id="header"]/nav/div/div/div[1]/div/div/a'
platforms_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[1]/div[1]/a'
enterprise_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/a[1]'
pricing_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/a[2]'
# blog_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/ul/li[1]/a'
# dev_xml = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div[1]/ul/li[1]/a'
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

itr = 5
while itr:
    for path in paths:
        scrapper.find_element(by="xpath",value=path).click()
        logs = scrapper.get_logs()
        for log in logs:
            #write each log to json file
            with open("logs.json","w") as f:
                json.dump(log,f,indent=4)

        
        
    itr-=1
