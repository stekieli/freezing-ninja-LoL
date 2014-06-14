#frenin/urls.py
from django.conf.urls import patterns, url

from frenin import views

urlpatterns = patterns('',
    url('^$',views.home, name='home'),
    url(r'^reggin/$', views.reggin, name='reggin'),
    url(r'^regout/$', views.regout, name='regout'),
    url(r'^status/$', views.status, name='status'),
    url(r'^check/$', views.check_matches, name='check')#,
    #url(r'^d3/$', views.d3view, name='d3')
)
