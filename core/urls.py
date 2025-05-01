from django.contrib import admin
from django.urls import path
from . import views
import apps.product.views as product_views

urlpatterns = [
    path('', views.hello_world),
    path('admin/', admin.site.urls),
    path('products/', product_views.view_all)
]
