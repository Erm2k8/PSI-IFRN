from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def view_all(request):
    all_objs = Product.objects.all()
    ctx = {
        'products': all_objs,
    }

    return render(request, 'products.html', context=ctx)

