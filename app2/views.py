from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .models import NutritionFact
from .forms import NutritionFactForm

# Create your views here.


def index(request):
    return render(request, 'app2/index.html')


class NutritionFactListView(ListView):
    model = NutritionFact


class NutritionFactUpdateView(UpdateView):
    model = NutritionFact
    form_class = NutritionFactForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('nutritionfact-list')
