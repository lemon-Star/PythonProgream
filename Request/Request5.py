import requests
import re

headers={
    'User-Agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '1',
    'upgrade-insecure-requests': '1'
    }
url='https://github.com/favicon.ico'

r=requests.get(url,headers=headers)
with open('favicon.ico', 'wb') as f:
    f.write(requests.get(url).content)

print(r.text)
print(r.content)
"""
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
title=re.findall(pattern, r.next)
print(title)
"""