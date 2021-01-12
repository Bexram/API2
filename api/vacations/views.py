from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models

class VacationGetAllList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,format=None):
        queryset = models.Vacations.objects.all()
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)

class VacationGetList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = models.Task.objects.filter(userprof=request.user)
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)