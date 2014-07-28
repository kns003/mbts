'''
Created on 26-Jul-2014

@author: shashank
'''
from django.conf.urls import patterns, url
from mangalore import views

urlpatterns = patterns('',
    url(r'^$', views.routes, name='search'),
)