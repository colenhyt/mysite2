from mysite2.sitepage import *


class DataMgr:
    def __init__(self):
        self.alexaData = {}
        self.prData = {}
        self.aa = {}
        self.baiduRankData = {}
        self.siteSumData = {}

    def getAlexa(self,url):
        hIndex = url.find("http://")
        if (hIndex==-1):
            url = "http://" + url
        alexa = -1
        if self.alexaData.has_key(url):
            alexa = self.alexaData[url]
        else:
            alexa = FindAlexaRank(url)
            self.alexaData[url] = alexa
        return alexa

    def getPr(self,url):
        hIndex = url.find("http://")
        if (hIndex==0):
            url = url[7:len(url)]
        pr = -1
        if self.prData.has_key(url):
            pr = self.prData[url]
        else:
            pr = FindGoogleRank(url)
            self.prData[url] = pr
        return pr

    def getBaiduRank(self,url):
        hIndex = url.find("http://")
        if (hIndex==0):
            url = url[7:len(url)]
        bdRank = -1
        if self.baiduRankData.has_key(url):
            bdRank = self.baiduRankData[url]
        else:
            bdRank = FindBaiduRank(url)
            self.baiduRankData[url] = bdRank
        return bdRank

    def getSiteSum(self,url):
        hIndex = url.find("http://")
        if (hIndex==-1):
            url = "http://" + url
        sum = {'title':'notitle','desc':'nodesc'}
        if self.siteSumData.has_key(url):
            sum = self.siteSumData[url]
        else:
            sum = FindSiteSum(url)
            self.siteSumData[url] = sum
        return sum

g_dataMgr = DataMgr()

print 'aaa'