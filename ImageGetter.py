#!/usr/bin/env python

import urllib
import os
import glob

# this method will not be called directly
# either returns a valid url that can be downloaded as an image, or an empty string
def get_image_url(link_url):
	three = [".jpg",".gif",".png"]
	imgurGifv = ".gifv"
	last = link_url[-4:].lower()

	if last in three:
		return link_url
	elif link_url[-5:] == imgurGifv:
		return link_url[:-1]
	else:
		return ""

# download the image to local storage
# parameter: urls is an array of urls that may or may not be an image url
# return: an array contains the local path to images
def download_images(urls):
	images = []
	counter = 0
	mb = 1024*1024.0

	if not os.path.exists("img"):
		os.makedirs("img")

	for url in urls:
		u = get_image_url(url)
		if u == "":
			images.append("")
		else:
			relative_path = "img/"+"00"+str(counter)+u[-4:].lower()
			f = open(relative_path,'wb')
			f.write(urllib.urlopen(u).read())
			f.close()

			# check if the file > 5 MB
			# TODO: downcast image to <= 5 MB
			if (os.path.getsize(relative_path) / mb) > 5.0:
				os.remove(relative_path)
				images.append("")
			else:
				images.append(relative_path)
		counter += 1

	return images

# removes all files under img/
def remove_all_images():
	files = glob.glob('img/*')
	for f in files:
		os.remove(f)
