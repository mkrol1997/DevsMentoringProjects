from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.genre}'


class Book(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    authors = models.ManyToManyField(Author, blank=True)
    published_date = models.CharField(max_length=5, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    average_rating = models.FloatField(null=True, blank=True, default='')
    ratings_count = models.IntegerField(null=True, blank=True, default='')
    thumbnail = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} / {self.published_date}'
