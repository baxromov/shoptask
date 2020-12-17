from django.contrib import admin
from .models import (
    Store,
    Manufacturer,
    Measure,
    Category,
    Product,
)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Manufacturer)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Measure)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['type']

@admin.register(Category)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']