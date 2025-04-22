from django.http import HttpResponse
from product.models import Product

def my_view(request):
    return HttpResponse("<h1>App online ✔</h1>")
