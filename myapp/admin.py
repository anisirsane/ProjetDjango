from django.contrib import admin

# Register your models here.
from .models import Seller, Produit

admin.site.register(Seller)
admin.site.register(Produit)
