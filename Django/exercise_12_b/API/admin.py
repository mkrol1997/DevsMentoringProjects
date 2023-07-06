from .models import Author, Book, Category
from django.contrib import admin


admin.site.register([Author, Book, Category])
