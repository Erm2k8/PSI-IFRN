from django.shortcuts import render
from django.http import HttpResponse

def view_all(request):
    return render(request, 'products.html')

