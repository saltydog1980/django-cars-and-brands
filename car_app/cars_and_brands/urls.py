"""car_app URL Configuration

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

from django.urls import path
from . import views

app_name="cars_and_brands" 
urlpatterns = [
    path('', views.index, name="home"),
    path('brands', views.brands, name="brands"),
    path('brands/new', views.brand_new, name="brand_new"),
    path('brands/<int:brand_id>', views.brand, name="brand"),
    path('brands/<int:brand_id>/edit', views.brand_update, name="brand_update"),
    path('brands/<int:brand_id>/cars', views.cars, name="cars"),
    path('brands/<int:brand_id>/cars/new', views.car_new, name="car_new"),
    path('brands/<int:brand_id>/cars/<int:model_id>', views.car, name="car"),
    path('brands/<int:brand_id>/cars/<int:model_id>/edit', views.car_update, name="car_update"),
    path('brands/delete/<int:model_id>', views.delete, name="delete"),
]
