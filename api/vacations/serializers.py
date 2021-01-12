from rest_framework import serializers
from . import models

class VacationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacations
        fields=('__all__')