from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterProduct

def view_all(request):
    return render(request, 'products.html')
