from .models import Author, Book, Category
from .serializers import BookSerializer, BookCreationSerializer
from .paginators import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView
)

from rest_framework.response import Response
from rest_framework import status
import requests


API_BASE_URL = "https://www.googleapis.com/"
API_ENDPOINT = "books/v1/volumes"


class BooksView(ListCreateAPIView):
    queryset = Book.objects.get_queryset().order_by('id')
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['authors', 'published_date']
    ordering_fields = ['id', 'published_date', 'average_rating', 'ratings_count']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreationSerializer
        return BookSerializer

    def get_paginated_response(self, data):
        return Response(data)

    def create(self, request, *args, **kwargs):
        params = {
            'q': request.data.get('title')
        }

        response = requests.get(API_BASE_URL+API_ENDPOINT, params=params).json()

        try:
            all_books_data = response['items']
        except KeyError:
            return Response(status=status.HTTP_204_NO_CONTENT)

        for book_data in all_books_data:
            book_object = Book.objects.update_or_create(
                defaults=
                {
                    "average_rating": book_data['volumeInfo'].get('averageRating'),
                    "ratings_count": book_data['volumeInfo'].get('ratingsCount'),
                    "thumbnail": book_data['volumeInfo'].get('imageLinks', {}).get('thumbnail'),
                },
                title=book_data['volumeInfo'].get('title'),
                published_date=book_data['volumeInfo'].get('publishedDate'))[0]

            categories = book_data['volumeInfo'].get('categories')
            authors = book_data['volumeInfo'].get('authors')

            if categories:
                [book_object.categories.add(Category.objects.get_or_create(genre=category)[0])
                 for category in categories]

            if authors:
                [book_object.authors.add(Author.objects.get_or_create(name=author)[0])
                 for author in authors]

        return Response(status=status.HTTP_201_CREATED)


class DetailedBookView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
