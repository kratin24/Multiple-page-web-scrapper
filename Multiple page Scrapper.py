#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup


# In[7]:


dress_name=[]
link=[]
start='https://www.flipkart.com'
page_no=input("enter page number")
for i in range(1,int(page_no)+1):
    #url="https://www.flipkart.com/search?q=women&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    url="https://www.flipkart.com/search?q=women+dresses&sid=clo%2Codx%2Cmaj%2Cjhy&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=women+dresses%7CWomen%27s+Dresses&requestId=359464dc-b51d-4de5-ad30-2706928e9d22&as-searchtext=women&page="+str(i)
    req=requests.get(url)
    content=BeautifulSoup(req.content,'html.parser')
    data=content.find_all('div',{'class':'_13oc-S'})   #class having name
    #print(len(data))    no of items in each page
   

    for i in data:
        dress_name.append(i.text)
    for i in data:
        rest_link=i.find('a')['href']
        link.append(start+rest_link)
    


# In[8]:


for i in range(len(link)): # to print name along with link
    print(link[i])
    print(dress_name[i])


# In[9]:


final_data.to_csv('flipkart_data.csv')

