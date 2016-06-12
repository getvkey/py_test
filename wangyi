#!/usr/bin/python
#coding:utf8

import re
import urllib
import json

#获取第一页搜索页面URL 人工输入关键字进行搜索
# http://so.v.163.com/search/000-0-0000-1-1-0-%E6%9A%B4%E8%B5%B0%E5%A4%A7%E4%BA%8B%E4%BB%B6/

def getHtml(url):
	page = urllib.urlopen(url).read()
	return page

def getList(page):
	re_key = "<h3>.+</h3>"
	#re_key = "<p>.+</p>"
	#re_key = "<div class=\"category-panel video-w635\" id=\"js_CategoryPanel\">.*"
	#re_key = "<ul class=\"clearfix\".+"
	#re_key ="<div class=\"ui-list18 video-pl6 video-dot\">.*?</div>"
	data = re.findall(re_key,page)
	return data



info = raw_input("请输入搜索关键字:\n")
page = 1
while page <= 2:
	url = "http://so.v.163.com/search/000-0-0000-1-%d-0-%s/" % (page,info)
	web = getHtml(url)
	arrdata = getList(web)
	#print len(arrdata)
	print url
	page += 1

	for i in range(0,len(arrdata)):
		lis = arrdata[i].decode("gb2312").encode("utf-8")
		print lis
		i = i + 1

# 去掉重复URL
# news_ids = []
# for id in arrdata:
#     if id not in news_ids:
#         news_ids.append(id)

# print news_ids

# for i in range(0,len(news_ids)):
# 	lis = news_ids[i].decode("gb2312").encode("utf-8")
# 	print lis

# 	i = i + 1

# for i in range(0,len(arrdata)):
# 	lis = arrdata[i].decode("gb2312").encode("utf-8")
# 	print lis
#
# 	i = i + 1
