#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
import pymongo
import pandas as pd
import html5lib
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from urllib.parse import urljoin


# In[3]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
db = client.classDB


# In[4]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
response = requests.get(url)


# In[5]:


soup = bs(response.text, 'html.parser')
print(soup.prettify())


# In[6]:


headlines = soup.find_all('div', class_='content_title')

headlines


# In[7]:


for headline in headlines:
    # Error handling
    try:
        # Identify and return title of listing
        news_title = headline.find('a').text

        # Print results only if title is available
        if (news_title):
            print('-------------')
            print(news_title)
            
    except AttributeError as e:
        print(e)


# In[8]:


captions = soup.find_all('div', class_='rollover_description')

captions


# In[9]:


for caption in captions:
    # Error handling
    try:
        # Identify and return title of listing
        news_p = caption.find('div', class_='rollover_description_inner').text

        # Print results only if title is available
        if (news_p):
            print('-------------')
            print(news_p)
            
    except AttributeError as e:
        print(e)


# In[10]:


# executable_path = {'executable_path': r'C:\Users\Babyta\AppData\Local\Temp\chromedriver_win32.zip\chromedriver.exe'}
# executable_path = {'executable_path' : r'C:\Users\Babyta\Downloads\chromedriver.exe'}
executable_path = {'executable_path': r'C:\Users\Babyta\Desktop\Columbia BCS\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[12]:


html = browser.html
soup = bs(html, 'html.parser')

image = soup.find('a', class_='button fancybox')

base_url = 'https://www.jpl.nasa.gov'
featured_image_url = urljoin(base_url, image['data-fancybox-href'])
featured_image_url


# In[13]:


url3 = 'https://space-facts.com/mars/'


# In[19]:


tables = pd.read_html(url3)
tables


# In[19]:


print(f'Total tables: {len(tables)}')


# In[21]:


table = tables[0]
table


# In[25]:


df = pd.DataFrame(table)
df
data = df.to_html()
data


# In[36]:


url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
url5 ='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
url6 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
url7 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
base_url2 = 'https://astrogeology.usgs.gov/'


# In[68]:


browser.visit(url4)


# In[69]:


html = browser.html
soup = bs(html, 'html.parser')

cerberus = soup.find('img', class_='wide-image')
cerberus_img = urljoin(base_url2, cerberus['src'])
cerberus_title = soup.find('h2', class_='title').text
cerberus_dict = {'title': cerberus_title, 'img_url': cerberus_img}
cerberus_dict


# In[63]:


browser.visit(url5)


# In[64]:


html = browser.html
soup = bs(html, 'html.parser')

schiaparelli = soup.find('img', class_='wide-image')
schiaparelli_img = urljoin(base_url2, schiaparelli['src'])
schiaparelli_title = soup.find('h2', class_='title').text
schiaparelli_dict = {'title': schiaparelli_title, 'img_url': schiaparelli_img}
schiaparelli_dict


# In[61]:


browser.visit(url6)


# In[62]:


html = browser.html
soup = bs(html, 'html.parser')

syrtis_major = soup.find('img', class_='wide-image')
syrtis_major_img = urljoin(base_url2, syrtis_major['src'])
syrtis_major_title = soup.find('h2', class_='title').text
syrtis_major_dict = {'title': syrtis_major_title, 'img_url': syrtis_major_img}
syrtis_major_dict


# In[65]:


browser.visit(url7)


# In[67]:


html = browser.html
soup = bs(html, 'html.parser')

valles_marineris = soup.find('img', class_='wide-image')
valles_marineris_img = urljoin(base_url2, valles_marineris['src'])
valles_marineris_title = soup.find('h2', class_='title').text
valles_marineris_dict = {'title': valles_marineris_title, 'img_url': valles_marineris_img}
valles_marineris_dict


# In[70]:


hemisphere_image_urls = [cerberus_dict, schiaparelli_dict, syrtis_major_dict, valles_marineris_dict]
hemisphere_image_urls


# In[ ]:

