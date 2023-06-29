from .views import BugsView
from django.urls import path


urlpatterns = [
    path('bugs/', BugsView.as_view(), name='home'),
]
