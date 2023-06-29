from django.urls import path
from .views import BugsView


urlpatterns = [
    path('bugs/', BugsView.as_view(), name='home'),
]
