from django.conf.urls import patterns, include, url
from inshorts import views

urlpatterns = [
	url(r'^en/(?P<section_name>\w+)/$', views.get_news),
]
