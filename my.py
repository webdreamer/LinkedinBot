import os, random, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=G:\\User Data');
browser = webdriver.Chrome(executable_path='driver/chromedriver.exe',chrome_options=options)

fullLink = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%2C%22gb%3A0%22%2C%22ca%3A0%22%2C%22hk%3A0%22%2C%22my%3A0%22%2C%22sg%3A0%22%2C%22tw%3A0%22%2C%22vn%3A0%22%5D&facetIndustry=%5B%224%22%2C%2296%22%5D&facetNetwork=%5B%22S%22%2C%22O%22%5D&keywords=CTO&origin=FACETED_SEARCH&page='
fullLink = fullLink + '8'
browser.get(fullLink)
visitedProfiles = []
profilesQueued = []
el = browser.find_element_by_class_name('search-global-typeahead__input')

def connect_part(els):
    for el in els:
        print(el.text)
        if(el.text=="Connect"):
            time.sleep(3)
            flag=1
            try:
                el.click()
            except:
                flag=0
            if(flag==1):
                time.sleep(5)
                modal = browser.find_element_by_class_name('artdeco-modal__actionbar')
                add = modal.find_element_by_class_name('artdeco-button--secondary')
                add.click()
                time.sleep(5)
                message = browser.find_element_by_id('custom-message')
                message.send_keys('Hi,')
                message.send_keys(Keys.ENTER)
                message.send_keys('How are you?')
                message.send_keys(Keys.ENTER)
                time.sleep(8)
                send = browser.find_element_by_class_name('artdeco-button--primary')
                if send.is_enabled():
                  send.click()
                else:
                    close_btn = browser.find_element_by_class_name("artdeco-modal__dismiss")
                    print("Close button clicked")
                    close_btn.click()

for page in (1,30):
    time.sleep(5)
    els = browser.find_elements_by_class_name('search-result__action-button')
    time.sleep(3)
    connect_part(els)
    browser.execute_script("window.scrollTo(0, window.scrollY + 900)")
    time.sleep(5)
    els = browser.find_elements_by_class_name('search-result__action-button')
    time.sleep(3)
    connect_part(els)
    if (page==1):
        browser.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(2)
    else:
        time.sleep(2)
    browser.find_element_by_class_name('artdeco-pagination__button--next').click()
    time.sleep(10)
browser.close()   
