from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models

class TaskList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer



class STaskList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Stask.objects.all()
    serializer_class = serializers.StaskSerializer


class STaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.Stask.objects.all()
    serializer_class = serializers.StaskSerializer