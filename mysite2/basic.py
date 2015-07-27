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

def downloadPage(url):
 buf = cStringIO.StringIO()
 try:
  c = pycurl.Curl()
  uu = url
  c.setopt(c.URL,uu)
  c.setopt(c.WRITEFUNCTION,buf.write)
  c.setopt(c.CONNECTTIMEOUT,55)
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

aa = downloadPage("https://www.baidu.com")
print 'aaeee'+aa