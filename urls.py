import django.conf.urls.defaults import *
from mysite2.views import hello

urlpatterns = patterns("",url('^hello/$',hello),)
