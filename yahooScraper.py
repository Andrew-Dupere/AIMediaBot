import re
import requests
import bs4
from bs4 import BeautifulSoup

from datetime import datetime
import json

def yahoo():

    url = 'https://www.yahoo.com/'
    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")
    box = doc.find('ul',class_='List(n) P(0) grid-layout stream-grid stream-items')

    yahoo = {}
    idx = 0

    for item in box.find_all('li')[:10]:
        
        try:
            yahoo[idx] = {
                'link' : item.find('a').get('href'),
                'category' : item.get('data-property'),
                'title' : item.find_all('a')[1].text,
                'tags' : item.get('data-wikis')
            }
            
        except:
            continue
        idx +=1

    list_of_topics = []

    for num in range(8):
        list_of_topics.append(yahoo[num]['title'])

    return(list_of_topics)


