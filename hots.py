
import time
from typing import Counter
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import re
from pprint import pprint

Mdict = {}

url = [
    "https://www.heroescounters.com/map/dragonshire",
    "https://www.heroescounters.com/map/alteracpass",
    "https://www.heroescounters.com/map/battlefieldofeternity",
    "https://www.heroescounters.com/map/braxisholdout",
    "https://www.heroescounters.com/map/cursedhollow",
    "https://www.heroescounters.com/map/gardenofterror",
    "https://www.heroescounters.com/map/hanamura",
    "https://www.heroescounters.com/map/infernalshrines",
    "https://www.heroescounters.com/map/tombofthespiderqueen",
    "https://www.heroescounters.com/map/towersofdoom",
    "https://www.heroescounters.com/map/warheadjunction",
    # "https://www.heroescounters.com/map/blackheartsbay",
    "https://www.heroescounters.com/map/skytemple"
    # "https://www.heroescounters.com/map/volskayafoundry"
]


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
#r = re.compile("\(.*")

for mapa in url:
    driver.get(mapa)
    dict = {}
    x = 0
    map_element = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[1]/div[2]/div/h1')
    map_content = map_element.get_attribute('innerHTML')

    while True:
        x += 1
        try:
            pers_element = driver.find_element_by_xpath(
                '/html/body/div/div[2]/ul/li['+str(x)+']/div/h3/a')
            personagem_name = pers_element.get_attribute('innerHTML')

            element = driver.find_element_by_xpath(
                '/html/body/div/div[2]/ul/li['+str(x)+']/div/a/span[2]/strong')
            html_content = int(element.get_attribute('innerHTML'))
            dict[personagem_name] = [html_content]
        except:
            break
    Mdict[map_content] = dict
pprint(Mdict, sort_dicts=False)
js = json.dumps(Mdict)
fp = open('charmap.json', 'w')
fp.write(js)
fp.close()
driver.quit()
