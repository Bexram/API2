from rest_framework import serializers
from .models import Task,Stask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','userprof','contract','clientobj','Task_name','Task_other','task_published','task_compl','task_status')

class StaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stask
        fields = ('__all__')