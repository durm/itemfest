from django.contrib import admin
from products.models import Product, Ingredient, IngredientFraction

admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(IngredientFraction)