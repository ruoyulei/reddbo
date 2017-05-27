#!/usr/bin/env python


import urllib
from bs4 import BeautifulSoup as BS
import re


def get_image_link(my_url):

    url = my_url
    
    html =  urllib.urlopen(url).read()
    
    soup = BS(html,'lxml')
    
    temp = soup.select("div.media-preview-content [href]")

    return temp[0]['href']

    # image_links = re.findall('a', temp[0])
    # print image_links


