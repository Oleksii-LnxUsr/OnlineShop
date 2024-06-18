from django.contrib import admin
from products.models import Product, Category, Brand, Configuration, Color, Image


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Configuration)
admin.site.register(Color)
admin.site.register(Image)
