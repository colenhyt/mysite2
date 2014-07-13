from mysite2.basic import *
import lxml.html
import lxml.etree
from xml.etree import ElementTree

googlePr = "http://toolbarqueries.google.com/search?client=navclient-auto&features=Rank&ch=8&q=info:"
alexaapi = "http://data.alexa.com/data?cli=10&url=%s"
baiduRank = "http://baidurank.aizhan.com/baidu/%s/position/"

def FindSiteSum(url):
    siteSum = {'title':'notitle','desc':'nodesc'}
    print url
    ht_string = downloadPage(url)
    index = url.find("store.apple.com")
    if len(ht_string)<=0:
        return siteSum
    ht_doc = lxml.html.fromstring(ht_string)
    title = ht_doc.find(".//title")
    print len(title)
    if title is not None:
        siteSum['title'] = title.text_content()[0:20]
    desc = ht_doc.find(".//meta[@name='description']")
    if desc is not None:
        siteSum['desc'] = desc.get('content')[0:30]
    return siteSum

def FindAlexaRank(url):
    rank = -1
    alexaUrl = alexaapi%(url)
    ht_string = downloadPage(alexaUrl)
    #print alexaUrl,ht_string
    if ht_string.find("<?xml version")!=0:
        return rank
    ht_doc = ElementTree.fromstring(ht_string)
    #print alexaUrl
    pops = ht_doc.findall("SD/POPULARITY")
    if pops is not None and len(pops)>0:
        rank = int(pops[0].attrib['TEXT'])
    return rank

def FindGoogleRank(url):
    pr = -1
    #prQy = googlePr + url
    #prTxt = downloadPage(prQy)
    #prs = prTxt.split(":")
    #if (len(prs)>2):
    #    pr = prs[1]
    return pr

def FindBaiduRank(url):
        brs = 0
        bdQy = baiduRank%(url)
        ht_string = downloadPage(bdQy)
        if len(ht_string)<=0:
            return brs
        ht_doc = lxml.html.fromstring(ht_string, "")
        divs =  ht_doc.xpath("//div[@class='box_17']")
        for div in divs:
            imgs = div.xpath(".//img[@align='absmiddle']")
            if (len(imgs)>0):
                imgname = imgs[0].get('src')
                index1 = imgname.index("brs/")
                index2 = imgname.index(".gif")
                brsstr = imgname[index1+4:index2]
                brs = int(brsstr)
        return brs

class SiteItem:
    def __init__(self,url):
        self.title = ''
        self.desc = ''
        self.url = url
        self.alexa = -1
        self.pr = 0
        self.baidurank = 0
        index = url.find("://")
        if (index>0):
            self.siteUrl = self.url[index+3:len(self.url)]
        else:
            self.siteUrl = url

    def queryProps(self):
        #site sum
        siteSum = FindSiteSum(self.url)
        self.title = siteSum['title']
        self.desc = siteSum['desc']
        ##google pr :
        self.pr = FindGoogleRank(self.siteUrl)
        #alexa rank:
        self.alexa = FindAlexaRank(self.siteUrl)
        #baidu rank:
        self.baidurank = FindBaiduRank(self.siteUrl)

    def siteSum(self):
        return {'title':self.title,'desc':self.desc,'url':self.url, 'id':self.url.replace('.','-'),
                'alexa':self.alexa,'pr':self.pr,'baidurank':self.baidurank}

    @property
    def title(self):
        return self.title

    @property
    def url(self):
        return self.url

    @property
    def desc(self):
        return self.desc

    @property
    def pr(self):
        return self.pr

    @property
    def alexa(self):
        return self.alexa

    @property
    def baidurank(self):
        return self.baidurank

import thread

def test1(url,item):
    item.url = "aaa"
    print "this is in thread" + item.url
    thread.exit_thread()

b = SiteItem("ww")
#thread.start_new_thread(test1,("ddd",b))
#print b.url
a = "a:b:d"
print len(a.split(":"))

#print b