from django.forms import ModelForm
from .models import NutritionFact

# Put our custom forms here


class NutritionFactForm(ModelForm):
    class Meta:
        model = NutritionFact
        fields = ['product_name', 'servings_per_container', 'serving_size_g', 'calories_kcal', 'calories_from_fat_kcal', 'total_fat_g', 'sodium_mg', 'total_carbs_g']
        labels = {
            'product_name': 'Food Product Name',
        }
