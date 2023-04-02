from selenium import webdriver
import json


web_driver_path = "chromedriver.exe"
website_link = "https://www.lambdatest.com"

class Scrapper:
    def __init__(self,web_driver_path):
        self.driver = webdriver.Chrome(web_driver_path)

    def get_page(self,url):
        self.driver.get(url)



scrapper = Scrapper("chromedriver.exe")
scrapper.get_page(website_link)

#get network log data
network_log = scrapper.driver.get_log('browser')


#save to json file
with open('network_log.json', 'w') as outfile:
    json.dump(network_log, outfile)

#close the browser
scrapper.driver.close()
