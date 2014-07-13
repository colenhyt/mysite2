from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from mysite2.baiduparser import BaiduPage
from mysite2.datamgr import *

def index(request):
 names = {'wd':'app'}
 return render_to_response('index.html',names,context_instance=RequestContext(request))

def search(request):
 wd = request.GET['wd']
 #bdChecked = request.GET['baidu']
 p = BaiduPage()
 p.parse(wd)
 resultitems = p.getSiteItems()
 #resultitems = [{'title':'site1','desc':'site1 desc','url':'aa.com','pr':7,'baidurank':3,'alexa':133},
  #              {'title':'sit2','desc':'site2 desc','url':'bb.com','pr':17,'baidurank':33,'alexa':1233}]
 searchpages = []
 for i in range(1,11):
  url = "s/?wd=" + wd
  url = "%s&pn=%d"%(url,i)
  searchpages.append({'name':i,'url':url})
 dict = {'wd':wd,'resultitems':resultitems,'searchpages':searchpages}
 return render_to_response('list.html',dict,context_instance=RequestContext(request))

def ajax(request):
 siteUrl = request.GET['siteUrl']
 siteUrl2 = "http://"+siteUrl
 q = request.GET['q']
 str = ''
 if q=='alexa':
  str = '%d'%(g_dataMgr.getAlexa(siteUrl2))
 elif q=='pr':
  str = '%d'%g_dataMgr.getPr(siteUrl)
 elif q=='sum':
  sum = g_dataMgr.getSiteSum(siteUrl2)
  str = sum['title']+","+sum['desc']
 elif q=='baidurank':
  str = '%d'%g_dataMgr.getBaiduRank(siteUrl)
 return HttpResponse(str)