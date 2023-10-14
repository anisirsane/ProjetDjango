from django.db import models
from datetime import date
# Create your models here.

class Seller(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.fields.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    dateOfBirth = models.DateField(null =True, blank=True, default='2000-01-01')
    profilePicture = models.ImageField()

class Product(models.Model):
    name = models.fields.CharField(max_length=100)   
    pic = models.ImageField()
    description = models.fields.TextField(max_length=1000)
    price = models.fields.DecimalField(max_digits = 5, 
                         decimal_places = 2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Picture(models.Model):
    alternative = models.fields.CharField(max_length=100)   
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)


    ###############  sources: ######################
    # pour les images:   https://stackoverflow.com/questions/537593/multiple-images-per-model