from django.contrib import admin
from product.models import Category, Product, Comment, Brand, GroupProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Brand)
admin.site.register(GroupProduct)
