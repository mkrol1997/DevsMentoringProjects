from django.urls import path
from .views import sites_view, SitesListView


urlpatterns = [
    path('', sites_view, name='home-default'),
    path('class-based/', SitesListView.as_view(), name='home-class-based')
]
