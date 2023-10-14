from django.shortcuts import render
from myapp.models import Seller

def main(request):
    sellers = Seller.objects.all()
    return render(request,
                   'myapp/main.html',
                   {'sellers':sellers} )
