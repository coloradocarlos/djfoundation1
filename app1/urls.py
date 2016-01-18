from django.conf.urls import url

from app1 import views

urlpatterns = [
    url(r'^$', views.index),
]
