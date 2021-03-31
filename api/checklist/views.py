import datetime

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView

from . import models, serializers



class TaskGetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, format=None):
        queryset = models.Task.objects.all()
        serializer = serializers.ChTaskGetSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskAddYear(APIView):
    permission_classes = [IsAuthenticated]

    def post(request, self, format=None):
        year=datetime.datetime.now().year
        queryset = models.Task.objects.filter(task_compl__lte=str(year)+'-12-31').filter(task_compl__gte=str(year)+'-01-01')
        for task in enumerate(queryset):
            new=models.Task(
                Task_name=task[1].Task_name,
                Task_other=task[1].Task_other,
                task_compl=task[1].task_compl.replace(year=task[1].task_compl.year+1),
                task_status=0
            )
            new.save()
        return HttpResponse(status=201)

class TaskDeleteYear(APIView):
    permission_classes = [IsAuthenticated]

    def post(request, self, year,format=None):
        queryset = models.Task.objects.filter(task_compl__lte=str(year)+'-12-31').filter(task_compl__gte=str(year)+'-01-01').delete()
        return HttpResponse(status=200)

class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.ChTaskSerializer


class TaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.ChTaskSerializer

