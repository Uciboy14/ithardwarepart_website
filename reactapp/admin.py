from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, CustomUser

# Register your models with the admin site
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
