#!/usr/bin/env python


import urllib
from bs4 import BeautifulSoup as BS
import re


def get_image_link(my_url):

    url = my_url
    
    html =  urllib.urlopen(url).read()
    
    soup = BS(html)
    
    temp = soup.find_all("img", class = "preview")
    
    
    imge_links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', temp)
    
    return imge_links[0]

