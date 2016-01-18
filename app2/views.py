from django.shortcuts import render
from django.views.generic.list import ListView
from .models import NutritionFact

# Create your views here.


def index(request):
    return render(request, 'app2/index.html')


class NutritionFactListView(ListView):
    model = NutritionFact
