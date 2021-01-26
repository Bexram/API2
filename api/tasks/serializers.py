from rest_framework import serializers
from .models import Task, Stask,Stask_foto,Reglament,Reglament_cat,trasfer_task
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

class GetTranferSerializer(serializers.ModelSerializer):
    to_user=GetUserSerializer()
    Task=TaskGetSerializer()
    class Meta:
        model = trasfer_task
        fields = ('__all__')

class TranferSerializer(serializers.ModelSerializer):
    class Meta:
        model = trasfer_task
        fields = ('__all__')

class AddReglam(serializers.Serializer):
    reglamcat=serializers.IntegerField()
    userprof=serializers.IntegerField()
    contract=serializers.IntegerField()
    startdate=serializers.DateField()
