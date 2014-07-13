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
import cStringIO

buf = cStringIO.StringIO()

def downloadPage(url):
 c = pycurl.Curl()
 c.setopt(c.URL,url)
 c.setopt(c.WRITEFUNCTION,buf.write)
 c.setopt(c.CONNECTTIMEOUT,5)
 c.setopt(c.TIMEOUT,8)
 c.perform()
 return buf.getvalue()

#print downloadPage('http://www.baidu.com')