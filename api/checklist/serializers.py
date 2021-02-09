from rest_framework import serializers
from .models import Task,Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')

class ChTaskGetSerializer(serializers.ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model = Task
        fields = ('__all__')

class ChTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')