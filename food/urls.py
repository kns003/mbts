'''
Created on 10-Aug-2014

@author: shashank
'''
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, url
from food.views import register,logout_view, profile, add_product, search_product_autocomplete, \
view_product

urlpatterns = patterns('',
    # existing patterns here...
    (r'^login/$',  login),
    (r'^logout/$', logout_view),
    (r'^register/$', register),
    (r'^product/add/$', add_product),
    (r'^profile/$', profile),
    (r'^search_product_autocomplete/$', search_product_autocomplete),
    (r'^product/view/(?P<product_id>\d+)$', view_product),
)