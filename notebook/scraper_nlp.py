import pandas as pd
import numpy as np 
from random import randint, random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time



# URL = 'https://www.textfocus.net/synonyme/d%C3%A9pression'

class scraper:
    def __init__(self):
        
        exec_path = "../bin/geckodriver"
        options = Options()
        options.headless = True
        options.add_argument("--enable-javascript")
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", "fr")
        firefox_profile.update_preferences()

        self.driver = webdriver.Firefox(executable_path=exec_path, options=options,firefox_profile=firefox_profile)


def get_synonym(word):
   

    URL = 'https://www.textfocus.net/synonyme/'+ word 

    self.driver.get(URL)

    # for word in driver.find_elements_by_xpath('//div[@class="row mb45"][3]'):
    list_w = [ i.text.split("\n") for i in driver.find_elements_by_xpath('//div[@class="row mb45"][3]') ]
    [ i for j in list_w for i in j]
    self.driver.quit()
    return [ i for j in list_w for i in j]



def tweet_scraper(URL):
    
    self.driver.get(URL)
    time.sleep(10)

    SCROLL_PAUSE_TIME = 8

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    result=[]
    while True:
        # Scroll down to bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

                                      
        text = self.driver.find_elements_by_xpath('//div[@class="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
        dates = self.driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time')

        for date, text in zip(dates, text):
            # print(date.get_attribute("datetime")[:10],"\n\n",
            #       text.text, "\n\n",
            #      "#-----------------------------------------------#")
            result.append([date.get_attribute("datetime")[:10], text.text])

        # Calculate new scroll height and compare with last scroll height
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        time.sleep(randint(1,9) * random())
    self.driver.quit()
    return pd.DataFrame(result, columns = ["date", "Comment"])

    def gdocs_scrapper(URL):

        self.driver.get(URL)
        rs=[]
        # for word in driver.find_elements_by_xpath('//div[@class="row mb45"][3]'):
        for i in self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/p/span'):
            if re.match("^\d", i.text):
                rs.append(re.sub("^\d*\.","",i.text))
        
        self.driver.quit()
        data = pd.DataFrame(rs, columns=["Comment"])
        data = data[data["Comment"]!=""]
        return data
