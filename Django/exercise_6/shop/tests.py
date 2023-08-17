from django.test import TestCase
from django.test.client import Client
from unittest.mock import patch
from django.shortcuts import reverse
from .models import Customer, Basket


class TestCustomerGeneratorView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_should_return_true_when_get_response_status_code_200(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('shop/generate_customer.html')

    def test_should_return_true_when_customer_created(self):
        with patch('shop.views.NAMES', ['test user']):
            response = self.client.post(reverse('homepage'))

        created_customer = Customer.objects.filter(name='test user').first()

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('shop/generate_customer.html')
        self.assertEqual(Customer.objects.all().count(), 1)
        self.assertEqual(created_customer.name, 'test user')


class TestShopSignals(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.customer = Customer.objects.create(name='testuser')

    def test_should_return_true_if_customer_basket_created(self):
        self.assertEqual(Basket.objects.all().count(), 1)
