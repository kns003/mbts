from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shanka.views.home', name='home'),
    url(r'^mangalore/', include('mangalore.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('food.urls')),
)
