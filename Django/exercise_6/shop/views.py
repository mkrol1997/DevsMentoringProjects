from .models import Customer
from django.shortcuts import render, redirect
from random import choice


NAMES = ['Connor Pope', 'Emery Hanson', 'Delilah Reyes', 'Kareem Arroyo',
         'Kendall Armstrong', 'Christina Buck', 'Barrett Maynard',
         'Maleah Drake', 'Eliana Cannon', 'Jax Hess', 'Izabelle Fletcher']


def GenerateCustomer(request):
    if request.method == 'POST':
        Customer.objects.create(name=choice(NAMES))
        return redirect('homepage')

    return render(request, 'shop/generate_customer.html')
