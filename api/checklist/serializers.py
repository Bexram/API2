from rest_framework import serializers
from .models import Task,Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')

class TaskGetSerializer(serializers.ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model = Task
        fields = ('__all__')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')