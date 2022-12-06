from bs4 import BeautifulSoup as bs
from selenium import webdriver
from twilio.rest import Client
import time
import schedule
def scraping():
    account_sid = ' ' # enter the ssid of twilio account
    auth_token = ' '  #enter the auth token of your twilio account
    path='C:\\Users\\Hi\\AppData\\Local\\Programs\\Python\\chromedriver' # enter the location of your chrome web driver
    driver=webdriver.Chrome(path)
    driver.get('https://www.covid19india.org/')
    time.sleep(100)
    page = driver.page_source
    driver.quit()
    soup = bs(page, 'html.parser')
    res=soup.find_all('div',{'class':'level-item is-confirmed'})
    mani=res[0].find_all('h1')
    a = mani[0].get_text()
    b = 'corona cases in india are '+ a
    client = Client(account_sid, auth_token)
    message = client.messages.create( from_='',body =b, to =' ')
schedule.every(30).minutes.do(scraping)      
while True:
    schedule.run_pending() 
    time.sleep(1)           
