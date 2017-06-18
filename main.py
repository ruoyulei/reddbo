import BaiduTranslator
import ImageGetter
import RedditContent
import time
import schedule
import json
import WeiboAccess

global index_counter
index_counter = 0

def runner():
	global index_counter
	index_counter = 0
	content = RedditContent.get_content()

	ImageGetter.remove_all_images()
	image_paths = ImageGetter.download_images(content[3])

	translated_titles = []

	for post in content[0]:
		zn = BaiduTranslator.translate(post)
		translated_titles.append(zn)

	for i in range(len(content[3])):
		url = ImageGetter.get_image_url(content[3][i])
		if url == "":
			translated_titles[i] += " "+content[3][i].encode('utf-8')

	print "all content downloaded and ready"

	schedule.every(1).minutes.do(lambda: post_weibo(translated_titles[index_counter],image_paths[index_counter]))
	while 1:
		#if index_counter >= len(translated_titles):
		if index_counter >= 5:
			index_counter = 0
			break
		schedule.run_pending()
		time.sleep(1)

def post_weibo(title,image_path):
	global index_counter
	index_counter += 1
	if image_path == "NA":
		return
	else:
		print "posting weibo: "+title
		WeiboAccess.post_weibo(title,image_path)

if __name__ == '__main__':
	print "running..."
	runner()
	#schedule.every(1).minutes.do(weibo_text)
	#while 1:
	#	schedule.run_pending()
	#	time.sleep(1)