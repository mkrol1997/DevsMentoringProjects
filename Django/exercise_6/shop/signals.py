from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Basket, Customer


@receiver(pre_save, sender=Customer)
def create_basket(sender, instance, **kwargs):
        instance.basket = Basket.objects.create()
