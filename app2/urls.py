from django.conf.urls import url
from .views import NutritionFactListView
from .views import NutritionFactUpdateView

from app2 import views

urlpatterns = [
    url(r'^mockup$', views.index, name='mockup'),
    url(r'^$', NutritionFactListView.as_view(), name='nutritionfact-list'),
    url(r'^update/(?P<pk>\d+)/$', NutritionFactUpdateView.as_view(), name="nutritionlist-update"),
]
