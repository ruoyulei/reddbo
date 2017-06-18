import BaiduTranslator
import ImageGetter
import RedditContent
import time
import schedule
import json
import WeiboAccess
import SQLConnector

global index_counter, content_ready
index_counter = 0

def runner():
	global index_counter,content_ready
	index_counter = 0
	content_ready = []
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

	print "all content downloaded"

	content_ready[0] = translated_titles
	content_ready[1] = image_paths
	content_ready[2] = content[2]
	

def post_all():
	global index_counter,content_ready
	if index_counter >= len(content_ready[0]):
		break

	post_weibo(content_ready[0][index_counter],content_ready[1][index_counter],content_ready[2][index_counter])

def post_weibo(title,image_path,postid):
	global index_counter
	index_counter += 1
	if image_path == "NA":
		print "image too large. not posting"
		return
	else:
		if SQLConnector.insert_into_db(postid):
			print "posting weibo: "+title
			WeiboAccess.post_weibo(title,image_path)

if __name__ == '__main__':
	print "start running..."
	runner()
	schedule.every(4).hours.do(runner)
	schedule.every(8).minutes.do(post_all)
	while 1:
		schedule.run_pending()
		time.sleep(1)
