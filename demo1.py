#! -*-coding:utf-8 -*-
from  bs4  import  BeautifulSoup
import urllib.request
import re
import xlsxwriter
k_art_name = []
v_art_url = []
for page in range(1,5):
    page = str(page)
    url = 'http://yujianglei.blog.51cto.com/all/7215578/page/'  + page
    request = urllib.request.urlopen(url)
    response = request.read()
    #response = unicode(response,'GBK').encode('UTF-8')
    #response = decode('GBK').encode('UTF-8')
    soup = BeautifulSoup(response,'html.parser')
    a_tag = soup.find_all(href=re.compile("^/\d{7,}/\d{7,}$"))
    for i  in a_tag:
        print(i)
        art_name = i.string
        art_url  = 'http://yujianglei.blog.51cto.com' + i['href']
        k_art_name.append(art_name)
        v_art_url.append(art_url)
#文件的基本名称和文件类型描述
workbook = xlsxwriter.Workbook(u'51cto博客.xlsx')
worksheet = workbook.add_worksheet(u'于江磊')
title = [u'文章列表',u'文章连接']
#表头边框，背景色，单元格内容位置，单元格字体加粗
format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()
format_title.set_size(15)
#表题
format_body = workbook.add_format()
format_body.set_border()
format_body.set_align('left')
#单元格高度
worksheet.set_row(0,40)
#单元格宽度
worksheet.set_column('A:B',50)
#写入文件标题
worksheet.write_row('A1',title,format_title)
#写入文件主体
worksheet.write_column('A2',k_art_name,format_body)
worksheet.write_column('B2',v_art_url,format_body)
workbook.close()
#上面的代码加上字符串+BeautifulSoup，保存文章名和文章的url到一个excel文件中。