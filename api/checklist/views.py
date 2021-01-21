from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView

from . import models, serializers

class CompanyGetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class TaskGetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.Task.objects.filter(company=pk)
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
