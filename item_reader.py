
# coding: utf-8

# In[1]:

import lxml.html
from selenium import webdriver
import requests
import time
# -*- coding: utf-8 -*-


# In[2]:

def findItemUrl(url):
#     target_url = "https://s.1688.com/selloffer/-CAD6CCE1B0FC.html?priceStart=40&cps=1&n=y&priceEnd=70&filt=y&uniqfield=pic_tag_id"
    target_html = requests.get(target_url).text
    root = lxml.html.fromstring(target_html)
    tags = root.body.xpath("//link[@rel='canonical']")
    for i in range(len(tags)):
        tag = tags[i].attrib['href']
        print("Changed:"+tag)
        return tag
      


# In[3]:

def toId(url):
    start = tag.find("offer")+6
    end = tag.find(".html")
    id = tag[start:end]
    print (id)
    return id


# In[ ]:

def loadHtml(url):
    driver.get(target_url)
    print ("Loading",end="")
    for i in range(10):
        print(".", end="")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("")
    return driver.page_source


# In[16]:

if __name__ == '__main__':
    target_url = 'https://s.1688.com/selloffer/-CAD6CCE1B0FC.html?cps=1&n=y&feature=87850&uniqfield=pic_tag_id'
    driver = webdriver.PhantomJS()
    target_html = loadHtml(target_url)


# In[17]:

root = lxml.html.fromstring(target_html)
links = root.body.xpath("//a")
print(len(links))
s = set([])
for i in range(len(links)):
    link = links[i]
    url = link.attrib["href"]
    print(url)
    if url.count("ci_") or url.count('/offer/'):
        if len(url) > 50:
            url = findItemUrl(url)
            time.sleep(1)
        s.add(url)
        print (url)

print(len(s))


# In[ ]:



