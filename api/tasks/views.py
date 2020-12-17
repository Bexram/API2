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
   permission_classes = [IsAuthenticated]
   def get(request,self,pk,format=None):
      queryset = models.Stask.objects.filter(Task=pk)
      serializer = serializers.StaskSerializer(queryset,many=True)
      return Response(serializer.data)


class GetFoto(APIView):
   permission_classes = [IsAuthenticated]
   def get(request,self,pk,format=None):
      queryset = models.Stask_foto.objects.filter(Stask=pk)
      serializer = serializers.StaskFotoSerializer(queryset,many=True)
      return Response(serializer.data)

class SFotoTaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask_foto.objects.all()
    serializer_class = serializers.StaskFotoSerializer


class STaskFotoDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask_foto.objects.all()
    serializer_class = serializers.StaskFotoSerializer