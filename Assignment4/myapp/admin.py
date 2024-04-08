from django.contrib import admin
from .models import User, Product

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity','price')
