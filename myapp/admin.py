from django.contrib import admin

# Register your models here.
from .models import Seller, Product, Picture

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Picture)