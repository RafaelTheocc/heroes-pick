import time
from typing import Counter
import requests #
import pandas as pd #
from bs4 import BeautifulSoup #
from selenium import webdriver #
from selenium.webdriver.firefox.options import Options
import json
import re
from pprint import pprint

Ndict = {}
Pdict = {}
x=0

url = "https://www.hotslogs.com/Default"



option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

#r = re.compile("\(.*")


driver.get(url)

while True:
    x += 1
    dict = {}
    try:
        pers_element = driver.find_element_by_xpath(
            '/html/body/form/div[4]/section/div[5]/div[1]/table/tbody/tr['+str(x)+']/td[2]/a') 
        personagem_name = pers_element.get_attribute('innerHTML')
        
        element = driver.find_element_by_xpath(
            '/html/body/form/div[4]/section/div[5]/div[1]/table/tbody/tr['+str(x)+']/td[6]') 
        html_content = str(element.get_attribute('innerHTML'))
        html_content = html_content.split('<')[0]
        dict[personagem_name] = [html_content]
        
    except:
        break
    Ndict[x] = dict
driver.quit()
pprint(Ndict,sort_dicts=False)
js = json.dumps(Ndict, indent=4, ensure_ascii=False)
fp = open('WinRate.json', 'w', encoding='utf-8')
fp.write(js)
fp.close()
