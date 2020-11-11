from rest_framework import serializers
from .models import Task,Stask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class StaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stask
        fields = ('__all__')