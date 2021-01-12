from rest_framework import serializers
from . import models
from users.serializers import GetUserSerializer

class VacationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacations
        fields=('__all__')

class VacationsGetSerializer(serializers.ModelSerializer):
    #userprof = GetUserSerializer()
    class Meta:
        model = models.Vacations
        fields=('__all__')