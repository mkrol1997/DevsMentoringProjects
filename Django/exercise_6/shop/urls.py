from django.urls import path
from .views import GenerateCustomer

urlpatterns = [
    path('generate_customer/', GenerateCustomer, name='homepage'),
]
