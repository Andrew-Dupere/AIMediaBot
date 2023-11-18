

import re
import requests

from datetime import datetime
import json

def dataPull():

    key = '819a7132af434afba91a7739c54ab02f'

    topic = 'Stock Market'

    endpoint = 'everything'

    # start = datetime.now().strftime('%Y-%m-%d')

    site = f'https://newsapi.org/v2/{endpoint}?q={topic}&sortBy=publishedAt&apiKey={key}&pageSize=20'

    r = requests.get(site).json()

    data = json.dumps(r, indent=2)

    # with open('testData.py', 'w') as f:
    #     f.write(f'data = {data}\n') 

    # data = json.dumps(r, indent=2)
        
    newObj = []

    for num in range(10):
        newObj.append(r['articles'][num]['description'])

    #this returns a list of descriptions for each article pulled
    return(newObj)

print(dataPull())

