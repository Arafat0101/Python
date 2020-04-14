from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list__display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)