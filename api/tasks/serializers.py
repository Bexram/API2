from rest_framework import serializers
from .models import Task, Stask
from clients.serializers import ContractGetSerializer
from users.serializers import GetUserSerializer


class TaskGetSerializer(serializers.ModelSerializer):
    contract = ContractGetSerializer()
    userprof = GetUserSerializer()

    class Meta:
        model = Task
        fields = (
        'id', 'contract', 'userprof', 'Task_name', 'Task_other', 'task_published', 'task_compl','task_start', 'task_status')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')


class StaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stask
        fields = ('__all__')
