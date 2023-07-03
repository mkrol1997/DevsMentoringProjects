from .models import Book
from collections import OrderedDict
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return OrderedDict(
                [(key, representation[key])
                    for key in representation
                    if representation[key] is not None])


class BookCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
