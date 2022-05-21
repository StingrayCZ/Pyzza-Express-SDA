from django.contrib import admin
from .models import Meal
from django.db import models


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
    'food_name', 'food_description', 'food_price', 'food_image', 'food_types', 'created_on', 'created_by')
    list_filter = (
    'food_name', 'food_description', 'food_price', 'food_image', 'food_types', 'created_on', 'created_by')


admin.site.register(Meal, RestaurantAdmin)
