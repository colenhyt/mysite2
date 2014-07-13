from django.conf.urls import patterns,url,include
from settings import *

urlpatterns = patterns('',
    ('^$', 'mysite2.view.index'),
    ('^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATICFILES_DIRS, 'show_indexes': True}),
    ('^home/', 'hello.views.home'),
    ('^ajax/', 'mysite2.view.ajax'),
    ('^s/', 'mysite2.view.search'),
)
