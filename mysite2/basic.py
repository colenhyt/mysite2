#coding=utf-8

import pycurl
import urllib2
import lxml.etree as etree
from bs4 import BeautifulSoup
import os
import sys
import urlparse
import lxml.html
import lxml.etree
import re
import traceback
import cStringIO

def headerCookie(buf):
 print buf
def downloadPage(url):
 buf = cStringIO.StringIO()
 try:
  c = pycurl.Curl()
  uu = url
  c.setopt(c.URL,uu)
  c.setopt(c.WRITEFUNCTION,buf.write)
  c.setopt(c.CONNECTTIMEOUT,55)
  c.setopt(pycurl.MAXREDIRS,50);
  c.setopt(pycurl.SSL_VERIFYPEER,0);
  c.setopt(pycurl.SSL_VERIFYHOST, 0)
  c.setopt(pycurl.HEADERFUNCTION, headerCookie)
  ##c.setopt(pycurl.COOKIE,Cookie)
  c.setopt(c.TIMEOUT,80)
  c.perform()
  return buf.getvalue()
 except Exception,ex:
  print Exception,":",ex
  return ""

def getStringFile(strFileName):
 fileHandle = open ( strFileName )
 strFile = fileHandle.read()
 fileHandle.close()
 return strFile

import jieba

text = "我来到北京大学";

default_mode = jieba.cut(text)
full_mode = jieba.cut(text,cut_all=True)
search_mode = jieba.cut_for_search(text)

print "精确模式:","/".join(default_mode)
print "全模式:","/".join(full_mode)
print "搜索引擎模式:","/".join(search_mode)

import jieba.analyse

text = "结巴中文分词模块是一个非常好的Python分词组件";

tags = jieba.analyse.extract_tags(text)

print "关键词抽取:","/".join(tags)