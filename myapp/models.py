from django.db import models
from datetime import date
# Create your models here.

class Seller(models.Model):
    name = models.fields.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    dateOfBirth = models.DateField(null =True, blank=True, default='2000-01-01')
    profilePicture = models.ImageField()
    shopifyLink = models.URLField(max_length = 200)
    def __str__(self):
        return self.name
    


class Produit(models.Model):
    name = models.fields.CharField(max_length=100)   
    pic = models.ImageField()
    description = models.fields.TextField(max_length=1000)
    price = models.fields.DecimalField(max_digits = 3,  decimal_places = 2,null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    