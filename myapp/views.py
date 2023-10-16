from django.shortcuts import render
from myapp.models import Seller, Produit


def sellers(request):
    sellers = Seller.objects.all()
    return render(request,
                   'myapp/main.html',
                   {'sellers':sellers} )


def seller_detail(request, seller_id):
    seller = Seller.objects.get(pk=seller_id)  
    products = Produit.objects.filter(seller=seller_id)  
    return render(request, 'myapp/seller.html', {'seller': seller, 'products': products})
#sources utilises: https://www.youtube.com/watch?v=7a23TbUXfWE&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=8
#https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO