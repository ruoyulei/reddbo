#!/usr/bin/env python


import urllib
from bs4 import BeautifulSoup as BS
import re


def get_image_link(my_url):

    url = my_url
    
    html =  urllib.urlopen(url).read()
    
    soup = BS(html,'lxml')
    
    temp = soup.findAll("div",{ "class" : "media-preview-content"})
    t2 = temp[0]

    return t2
    
    #image_links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', temp)
    
    #print image_links
    # return imge_links[0]

