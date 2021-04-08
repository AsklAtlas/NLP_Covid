import pandas as pd
import numpy as np 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.edge.options import Options
import time

#-------ARGS-----------------------------------#
URL = 'https://twitter.com/hashtag/generation2021?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Ehashtag'
exec_path = "../bin/geckodriver" # charger le driver pour chrome ou edge
#----------------------------------------------#
def get_driver():
#-------OPTIONS--------------------------------#
	options = Options()
	options.headless = True
	options.add_argument("--window-size=1920,1200")
	options.add_argument("--enable-javascript")
	#----------------------------------------------#
	firefox_profile = webdriver.FirefoxProfile()
	firefox_profile.set_preference("intl.accept_languages", "fr")
	firefox_profile.update_preferences()
	# driver = webdriver.Firefox(executable_path=exec_path, options=options,firefox_profile=firefox_profile)
	# driver = webdriver.Chrome(executable_path=exec_path, options=options)
	# driver = webdriver.Edge(executable_path=exec_path, options=options)
	return webdriver.Firefox(executable_path=exec_path, options=options,firefox_profile=firefox_profile)
def get_url(driver, URL):	
	driver.get(URL)
	time.sleep(10)

	SCROLL_PAUSE_TIME = 8

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    result=[]
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        if len(URL.split('/')) > 4:
        	text = driver.find_elements_by_xpath('//div[@class="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
        	dates = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time')
        
        else:
        	
                                      
        # print(driver.page_source)  /html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div
#         text = driver.find_elements_by_xpath('//div[@class="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
        text = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
#         dates = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time')
        dates = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/a/time')
    #     link_conv = driver.find_elements_by_xpath('//a[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-t2kpel r-1ny4l3l r-1udh08x r-ymttw5 r-1vvnge1 r-o7ynqc r-6416eg"]')

        for date, text in zip(dates, text):
#             print(date.get_attribute("datetime")[:10],"\n\n",
#                   text.text, "\n\n",
#                  "#-----------------------------------------------#")
            result.append([date.get_attribute("datetime")[:10], text.text])

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        time.sleep(randint(1,9) * random())
    driver.quit()
    return pd.DataFrame(result, columns = ["date", "text"])

#-------DATES-------------#
dates = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time')
for date in dates:
    print(date.get_attribute("datetime"))
#-------------------------#
driver.quit()