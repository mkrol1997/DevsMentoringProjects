from django.urls import path
from .views import generate_customer

urlpatterns = [
    path('generate_customer/', generate_customer, name='homepage'),
]
