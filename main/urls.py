"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from products import views
from main import settings

from products.views import brands, types

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('findus/', views.findus, name='findus'),
    path('accessories/', views.accessories, name='accessories'),
    path('other/',views.other_products, name='other_products'),
    path('<str:cate>/<str:id>/', views.get_product, name='get_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

for p, a in brands.items():
    urlpatterns.append(path('%s/' % p, views.get_bags, name='get_bags'))


for p, a in types.items():
    urlpatterns.append(path('%s/' % p, views.get_bags, name='get_bags'))


urlpatterns.append(path('<str:id>/', views.get_product_index, name='get_product'))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
