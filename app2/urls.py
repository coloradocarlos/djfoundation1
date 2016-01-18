from django.conf.urls import url
from .views import NutritionFactListView

from app2 import views

urlpatterns = [
    url(r'^mockup$', views.index, name='urlIndex'),
    url(r'^$', NutritionFactListView.as_view(), name='nutitrionfact-list'),
]
