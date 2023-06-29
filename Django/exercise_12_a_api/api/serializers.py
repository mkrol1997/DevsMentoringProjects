from .models import BugModel
from rest_framework import serializers


class BugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugModel
        fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['description'] = instance.description
        representation['username'] = instance.user.username
        representation['project'] = instance.project.name

        return representation
