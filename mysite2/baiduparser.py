import lxml.etree as etree
from bs4 import BeautifulSoup
#import lxml.html.soupparser as soupparser
import os
import sys
import urlparse
import lxml.html
import lxml.etree
import re
from mysite2.basic import *
from mysite2.sitepage import *

class BaiduPage:
    def __init__(self):
        self.bodyValue = ''
        self.itemUrls = {}

    def parse(self,queryWord,pageCount = 5):
        i = 0
        while (len(self.itemUrls)<pageCount):
            self.url = "http://www.baidu.com/s?wd=" + queryWord + "&pn="
            self.url = "%s%d"%(self.url,i)
            htmlContent = downloadPage(self.url)
            self.findItemUrls(htmlContent)
            i += 10
        #print self.bodyValue
        return 0

    def parse2(self,strContent):
        self.bodyValue = strContent
        self.findItemUrls(strContent)
        #print self.bodyValue
        return 0

    def findBody(self):
        print 'baidu find body'

    def items_search(self):
        items = {}
        for i in range(1,5):
            items[i] = {'url':'e','c':'w'}
        return items

    def findItemUrls(self,htmlContent):
        items = []
        if (len(htmlContent)<=0):
            return 0
        ht_doc = lxml.html.fromstring(htmlContent)
        elms = ht_doc.xpath("//div[@class='result c-container ']")
        for tag in elms:
           # div_doc = tag.tag
            div2 = tag.xpath(".//div[@class='f13']")
            for subtag in div2:
                sp = subtag.xpath(".//span[@class='g']")
                for ss in sp:
                    index = ss.text_content().index("/")
                    url = ss.text_content()[0:index]
                    print url
                    print self.itemUrls.has_key(url)
                    if not self.itemUrls.has_key(url):
                        self.itemUrls[url] = url
                    #items.append(ss.text_content()[0:index])
              #  print(sp[0].text)
        return 0

    def getItemUrls(self):
        return self.itemUrls

    def getSiteItems(self):
        siteItems = []
        for url in self.itemUrls:
            siteItem = SiteItem(url)
            #siteItem.queryProps()
            print siteItem.siteSum()
            siteItems.append(siteItem.siteSum())
        return siteItems

class BaiduParser:
    def __init__(self):
        self.pages = {}
        return 1

    def findItems(self,queryWord,pageCount):
        page = self.pages[queryWord]
        if not page:
          parse(queryWord,pageCount)
        else:
            return page
        return self.pages[queryWord]

    def parse(self,queryWord,pageCount):
        p = BaiduPage()
        p.parse(queryWord,pageCount);
        self.pages[queryWord] = p
        return 0

    def queryPage(self,queryWord):
        page = self.pages[queryWord]
        return page






#a = BaiduPage()
#a.parse("app")
#items = a.getSiteItems()
#print items
#print ht_string
#ht_string = "<html><div class='result-op c-ocntainer xpath-log'>dddaaa</div></html>"
#p.parse("app",10)
#pp = p.parse2(ht_string)
#print p.getItemUrls()