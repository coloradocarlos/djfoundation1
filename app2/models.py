from django.db import models

# Create your models here.


class NutritionFact(models.Model):
    product_name = models.CharField(max_length=255)
    servings_per_container = models.IntegerField()
    serving_size_g = models.IntegerField()
    calories_kcal = models.IntegerField()
    calories_from_fat_kcal = models.IntegerField()
    total_fat_g = models.IntegerField()
    sodium_mg = models.IntegerField()
    total_carbs_g = models.IntegerField()
