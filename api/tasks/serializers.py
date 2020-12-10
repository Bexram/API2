from rest_framework import serializers
from .models import Task, Stask
from clients.serializers import ContractSerializer
from users.serializers import UserProfileSerializer


class TaskGetSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()
    userprof = UserProfileSerializer()

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
