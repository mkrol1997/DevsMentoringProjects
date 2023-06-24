from django.db import models


class Basket(models.Model):
    shopping_items = models.CharField(max_length=200)
    total_price = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer.name}'s Basket"


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    registration_date = models.DateField(auto_now_add=True)
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
