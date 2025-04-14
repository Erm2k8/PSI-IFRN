from django.http import HttpResponse
from product.models import Product

def my_view(request):
    return HttpResponse("<h1>HOLA MUNDITO</h1>")

def products(request):
    items = ''.join(f"<li>{p.id}, {p.description}, {p.price}</li>" for p in Product.objects.all())
    return HttpResponse(f"<ul>{items}</ul>")