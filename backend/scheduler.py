import schedule
import time
import scrapper

def run_scrapper():
    scrapper.main(100)

schedule.every().day.at("12:00").do(run_scrapper)

while True:
    schedule.run_pending()
    time.sleep(1)