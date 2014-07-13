from django.shortcuts import render
from django.template import Template,loader,Context
from django.template.loader import  get_template
from hello.queryeng import downloadPage
from django.template import RequestContext
from django.shortcuts import render_to_response
from mysite2.baiduparser import BaiduPage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

@csrf_exempt
def home1(request):
 t = get_template('list.html')
 html = t.render(Context({'name':'wwwww'}))
 #return HttpResponse(request.META['HTTP_USER_AGENT'])
 return HttpResponse(request.GET['CC'])

@csrf_exempt
def home(request):
 t = get_template('list.html')
 html = "<b><i>colen</i></b>"
 #p = BaiduPage()
 #names = p.items_search();
 names2 = [{'a':'aa'},{'a':'bb'},{'a':'cc'},{'a':'dd'}]
 names = {'names':names2,'queryWord':'app develop'}
 return render_to_response('list.html',names,context_instance=RequestContext(request))

def home11(request):
 strWord = 'baidu.html?'+request.GET['word']
 html = downloadPage(strWord)
 return HttpResponse(html)
