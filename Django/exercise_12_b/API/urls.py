from .views import BooksView, DetailedBookView
from django.urls import path


urlpatterns = [
    path('books/', BooksView.as_view()),
    path('books/<int:pk>', DetailedBookView.as_view())
]
