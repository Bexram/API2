from rest_framework import serializers

class ReportSerializer(serializers.Serializer):
    employer=serializers.IntegerField
    client=serializers.IntegerField
    object=serializers.IntegerField
    contact=serializers.IntegerField
    start=serializers.DateField
    end=serializers.DateField

