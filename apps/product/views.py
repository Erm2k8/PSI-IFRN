from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models.product import Product

def view_all(request):
    all_objs = Product.objects.all()
    ctx = {
        'products': all_objs,
    }

    return render(request, 'products.html', context=ctx)

def product_detail(request, id):
    obj = get_object_or_404(Product, id=id)
    ctx = {
        'product': obj,
    }
    
    return render(request, 'product_detail.html', context=ctx)