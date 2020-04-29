from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import time
import requests
import shutil

PATH = "chromedriver.exe"
browser = webdriver.Chrome(PATH)
username = 'writing_beyond_everything'

def download_image(url, name="Untitled.jpg"):
        # Open the url image, set stream to True, this will return the stream content.
        resp = requests.get(url,  verify=True)
        # Open a local file with wb ( write binary ) permission.
        local_file = open(name, 'wb')
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)
        # Remove the image url response object.

browser.get('https://www.instagram.com/'+username+'/?hl=en')
Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#Extract links from user profile page
links=[]
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
page_json = script.text.split(' = ', 1)[1].rstrip(';')
data = json.loads(page_json)
for link in data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']:
    links.append('https://www.instagram.com'+'/p/'+link['node']['shortcode']+'/')

for i,l in enumerate(links):
    download_image(l, "-".join(["post",str(i),".jpg"]))





time.sleep(5)
browser.quit()


