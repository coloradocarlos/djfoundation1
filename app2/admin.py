from django.contrib import admin

# Register your models here.
from .models import NutritionFact


class NutritionFactAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'calories_kcal')

admin.site.register(NutritionFact, NutritionFactAdmin)
