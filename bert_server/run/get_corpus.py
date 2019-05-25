# coding: utf-8
from magic_google import MagicGoogle
from MagicBaidu import MagicBaidu
import search_google.api

import time
# import plogging.info
import Terry_toolkit as tkit
import langid
import random

import requests
from readability import Document
import html2text


import logging
#加载配置文件
# from get_corpus_conf import BUILDARGS,CSEARGS,PATH,PROXIES
#文件保存为止
PATH="/home/terry/pan/github/bert/book/"
# PATH="/terry/bert/data/corpus/book/"
SEARCH = 'baidu'

BUILDARGS = {
  'serviceName': 'customsearch',
  'version': 'v1',
  'developerKey': 'apk' #https://developers.google.com/custom-search/v1/introduction
}

# Define cseargs for search
CSEARGS = {
  'q': '柯基犬',
  'cx': '007397120899702103013:roufggcacti',
#   'num': 30
}
PROXIES = [{
      'http': '127.0.0.1:43285',
      'https': '127.0.0.1:43285',
}]


#@title 关键词
#@markdown 输入关键词搜索

#@markdown 输入关键词用空格隔开' '
keywords = "*\u72AC *\u72D7 *\u732B *\u86C7 *\u730E\u72AC \u5BA0\u7269* *\u9C7C *\u718A *\u7F8A \u9A74 \u8774\u8776\u72AC \u814A\u80A0\u72AC \u7352\u72AC \u7F57\u5A01\u7EB3\u72AC \u731B\u72AC \u5927\u578B\u72AC \u5C0F\u578B\u72AC \u4E2D\u578B\u72AC \u9B23\u72D7 \u975E\u6D32\u91CE\u72D7 \u91CE\u751F\u52A8\u7269 \u52A8\u7269\u56ED \u5BA0\u7269\u5E7C\u5D3D \u75A3\u732A \u91CE\u732A \u5927\u8C61 \u9ED1\u718A \u5317\u6781\u718A \u4F01\u9E45 \u957F\u9888\u9E7F \u9E7F \u7F9A\u7F8A \u5C71\u7F8A \u517B\u732B \u517B\u72D7 \u4ED3\u9F20 \u767D\u9E6D \u5DF4\u54E5\u72AC \u5DF4\u54E5 \u9E66\u9E49 \u91D1\u9C7C \u77ED\u8033\u732B \u72D7\u5B50 \u4E8C\u54C8 \u5BB6\u6709\u840C\u5BA0 \u840C\u5BA0 \u5BA0\u7269\u732B \u6D41\u6D6A\u732B \u6D41\u6D6A\u72D7 \u6536\u517B\u6D41\u6D6A\u732B \u5C0F\u732B \u66B9\u7F57\u732B \u77ED\u6BDB\u732B \u8FB9\u5883\u7267\u7F8A\u72AC \u7267\u7F8A\u72AC \u5FB7\u7267 \u6BD4\u7279\u72AC \u6597\u725B\u72AC \u5F69\u8679\u9CA8 \u5730\u56FE\u9C7C \u7352\u72AC \u975E\u6D32\u52A8\u7269 \u54FA\u4E73\u52A8\u7269 \u4ED3\u9F20 \u72EE\u5B50 \u8001\u864E \u7280\u725B \u52A8\u7269\u6253\u67B6 \u52A8\u7269\u4EA4\u914D \u722C\u884C\u52A8\u7269 \u4E4C\u9F9F \u86C7 \u9CA8\u9C7C \u52A8\u7269\u72E9\u730E \u52A8\u7269\u51AC\u7720 \u5403\u8D27\u840C\u5BA0 \u840C\u5BA0 \u52A8\u7269\u7F8E\u5BB9 \u8001\u9F20" #@param {type:"string"}
sites = 'http://blog.sina.com.cn/ http://www.sohu.com/a/ 163.com news.qq.com https://baike.baidu.com https://www.douban.com/'  #@param {type: "string"}

num =100
#@markdown ---

#



# Or MagicGoogle()
# mg = MagicGoogle(PROXIES)
def url_text(url):
  response = requests.get(url)
  # logging.info(response.text)
  # html = request.urlopen(url)

  # logging.info(html)

  doc = Document(response.text)
  # doc = Document(html)
  # logging.info(doc.title())

  html= doc.summary(True)
#   logging.info(doc.get_clean_html())
  t =html2text.html2text(html)
  return t
#   logging.info(t)
#进行分句的核心函数
def Cut(cutlist,lines):          #参数1：引用分句标志符；参数2：被分句的文本，为一行中文字符
    l = []         #句子列表，用于存储单个分句成功后的整句内容，为函数的返回值
    line = []    #临时列表，用于存储捕获到分句标志符之前的每个字符，一旦发现分句符号后，就会将其内容全部赋给l，然后就会被清空

    for i in lines:         #对函数参数2中的每一字符逐个进行检查 （本函数中，如果将if和else对换一下位置，会更好懂）
        if FindToken(cutlist,i):       #如果当前字符是分句符号
            line.append(i)          #将此字符放入临时列表中
            l.append(''.join(line))   #并把当前临时列表的内容加入到句子列表中
            line = []  #将符号列表清空，以便下次分句使用
        else:         #如果当前字符不是分句符号，则将该字符直接放入临时列表中
            line.append(i)
    return l
#检查某字符是否分句标志符号的函数；如果是，返回True，否则返回False
def FindToken(cutlist, char):
    if char in cutlist:
        return True
    else:
        return False

#预处理文档
def text_pre(text):

  text = text.strip().split("\n" )
  # logging.info(text)
#   logging.info(len(text))

  while '' in text:
      text.remove('')
  # logging.info(len(text))
  Paragraph_length=len(text)
  #设置分句的标志符号；可以根据实际需要进行修改
  cutlist ="。！？"
  new_text_list =[]
  sentences_num = 0
  for item in text:
    t = Cut(cutlist,item)
    sentences_num=sentences_num+len(t)

    text_p = "\n".join(t)
  #   text_list
  #   logging.info(text_p)
  #   logging.info("*"*10)
    new_text_list.append(text_p)

  # logging.info(new_text_list)

  # new_text = "\n\n".join(new_text_list)
  while '' in new_text_list:
    new_text_list.remove('')
  new_text = " \n".join(new_text_list)

  # logging.info(len(t))
  # new_text=''
  # for it in t :
  #   new_text = new_text+it

#   logging.info(new_text)
  data ={
      'text' : new_text,
      'paragraph_num':Paragraph_length,
      'sentences_num':sentences_num
  }
  return data


def search(keyword ,num=num,ty='google'):

  logging.info('搜索关键词:'+keyword)
#   lang,p=langid.classify(keyword)
#   if lang=='zh':
#     logging.info('中文关键词')
#   else:
#     logging.info('非中文')
#     return []

  if ty=='google':

    mg = MagicGoogle(PROXIES)
    urls=mg.search_url(query=keyword , num=num,start=0, pause=5)
  elif ty =='gcs':
    results = search_google.api.results(BUILDARGS, CSEARGS)
    urls = results.get_values('items', 'link')
    # logging.info(links)
  else:
    mg = MagicBaidu()
    urls= mg.search_url(query=keyword ,start=0, pause=5)
  #  Crawling the whole page
#   result = mg.search_page(query=keyword)


  cx=tkit.CxExtractor()
  # Crawling url
  keywords=[]
#   for url in mg.search_url(query=keyword):
  n = 0
  file_name= PATH+'corpu'+str(time.time())+".txt"

  for url in urls: #google
  #for url in mg.search_url(query=keyword ,start=0, pause=10): #百度
      logging.info(url)

      try:

  #         items= cx.url_text_no_br(url=url)
        items=url_text(url=url)
      except:
        continue

#       logging.info("*"*50)
#       plogging.info.plogging.info(items)
#       plogging.info.plogging.info("*"*50)

  #       items= tkit.Text().text_processing(items)
      items= text_pre(items)
  #       plogging.info.plogging.info('句子数目为: ',len(items['sentence']))
      logging.info('句子数目为: '+str(items['sentences_num']))
  #       plogging.info.plogging.info(items)

      if items['sentences_num']>5:
        n = n+1
        if n % 5 ==0 :

       # keywords = keywords+ items['keywords']
          file_name= PATH+'corpu'+str(time.time())+".txt"

        logging.info('写入文件:  '+file_name)
        my_open = open(file_name, 'a')


        my_open.write(str( items['text'])+'\n\n')
        my_open.close()

  t = random.randint(30,100)


  logging.info('搜索结束休息中 '+str(t)+'s')
  logging.info ("Start : %s" % time.ctime())
  time.sleep(t)
  logging.info ("End : %s" % time.ctime())
  return
#   return keywords
#     logging.info(items)
# Output
# 'https://www.python.org/'


# Get {'title','url','text'}
# for i in mg.search(query='python', num=1):
#     plogging.info.plogging.info(i)
sites = sites.split( )
keywords = keywords.split( )
random.shuffle(sites)
random.shuffle(keywords)
ty =SEARCH

logging.info(sites)
logging.info(keywords)
# 匹配网站
for site in sites:
  if not site:
     s_site=''
  else:
    s_site=" site:"+site

  for keyword in keywords:
    keyword_new= keyword+s_site


    logging.info(keyword_new)
    search(keyword_new  , num=num,ty=ty)


#进行通用搜索内容
for keyword in keywords:
  keyword_new= keyword


  logging.info(keyword_new)
  search(keyword_new  , num=num,ty=ty)

