from django.conf.urls import patterns, url

from app1 import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='urlIndex')
                       )
