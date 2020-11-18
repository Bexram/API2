from rest_framework import serializers
from .models import Task,Stask
from clients.serializers import ContractSerializer

class TaskSerializer(serializers.ModelSerializer):
    contract=ContractSerializer()
    class Meta:
        model = Task
        fields = ('id','contract','userprof','contract','clientobj','Task_name','Task_other','task_published','task_compl','task_status')

class StaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stask
        fields = ('__all__')