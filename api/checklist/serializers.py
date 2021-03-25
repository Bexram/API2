from rest_framework import serializers
from .models import Task

class ChTaskGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class ChTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')