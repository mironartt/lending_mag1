from django.contrib import admin

from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'avaliabled']

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
