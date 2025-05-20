from django.http import HttpResponse
from django.shortcuts import render
from apps.product.models.product import Product

def hello_world(request):
    return render(request, template_name="index.html")
