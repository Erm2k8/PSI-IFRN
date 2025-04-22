from urllib.robotparser import RequestRate
from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterProduct

def view_all(request):

    if request.method == 'POST':
        form = RegisterProduct(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form, 'registered': True})
    
    else:
        form = RegisterProduct()

    return render(request, 'index.html', {'form': form, 'registered': False})
