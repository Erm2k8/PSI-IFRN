from django.contrib import admin
from django.urls import path
from . import views
import product.views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.my_view),
    path('products/', product_views.view_all)
]
