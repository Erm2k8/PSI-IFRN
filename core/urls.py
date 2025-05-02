from django.contrib import admin
from django.urls import path
from . import views
import apps.product.views as product_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hello_world, name='index'),
    path('admin/', admin.site.urls),
    path('products/', product_views.view_all, name='products')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
