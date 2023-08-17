from .views import sites_view, SitesListView
from django.test import TestCase
from django.test.client import Client
from .models import SiteUrlModel
from django.shortcuts import reverse


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        super(ViewsTest, cls).setUpClass()
        cls.site_1 = SiteUrlModel.objects.create(url='www.onet.pl')
        cls.site_2 = SiteUrlModel.objects.create(url='www.interia.pl')

    def test_should_return_status_code_200_when_homepage_function_based_view_request_method_get(self):
        response = self.client.get(reverse('home-default'))
        sites = response.context.get('sites')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('exercise_1/index.html')
        self.assertSetEqual(SiteUrlModel.objects.all(), sites)

    def test_should_return_status_code_405_when_homepage_function_based_view_request_method_post(self):
        response = self.client.post(reverse('home-default'))

        self.assertEqual(response.status_code, 405)


class ClassBasedViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        super(ClassBasedViewsTest, cls).setUpClass()
        cls.site_1 = SiteUrlModel.objects.create(url='www.onet.pl')
        cls.site_2 = SiteUrlModel.objects.create(url='www.interia.pl')

    def test_should_return_status_code_200_when_homepage_class_based_view_request_method_get(self):
        response = self.client.get(reverse('home-class-based'))
        sites = response.context.get('sites')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('exercise_1/index.html')
        self.assertSetEqual(SiteUrlModel.objects.all(), sites)

    def test_should_return_status_code_200_when_homepage_class_based_view_request_method_post(self):
        response = self.client.post(reverse('home-class-based'))

        self.assertEqual(response.status_code, 405)
