from django.http import Http404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models

class TaskGetAllList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,format=None):
        queryset = models.Task.objects.all()
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)

class TaskGetList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = models.Task.objects.filter(userprof=request.user)
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)

class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer



class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer



class STaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask.objects.all()
    serializer_class = serializers.StaskSerializer


class STaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask.objects.all()
    serializer_class = serializers.StaskSerializer

class GetSTaskList(APIView):
   def get(idtask,self,format=None):
      permission_classes = [IsAuthenticated]
      queryset = models.Stask.objects.filter(Task=idtask)
      serializer_class = serializers.StaskSerializer

