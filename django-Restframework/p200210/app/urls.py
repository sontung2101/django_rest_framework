from django.urls import path,include
from .views import *
urlpatterns = [
    path('hello/',hello),
    path('get_products',getProducts),
]
   