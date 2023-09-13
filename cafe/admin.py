from django.contrib import admin

# Register your models here.
from .models import DishCategory


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

