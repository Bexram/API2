from rest_framework import serializers
from .models import Task, Stask,Stask_foto,Reglament,Reglament_cat
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


class StaskFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stask_foto
        fields = ('__all__')

class ReglamCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglament_cat
        fields = ('__all__')

class ReglamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglament
        fields = ('__all__')