from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from . import models,serializers

class TaskList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

class TaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer