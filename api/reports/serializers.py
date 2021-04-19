from rest_framework import serializers
from . import models
from clients.serializers import ObjectGetSerializer,ContactManSerializer
from users.serializers import UserProfileSerializer

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QReport
        fields = ('__all__')


class GetReportSerializer(serializers.ModelSerializer):
    userprof=UserProfileSerializer()
    clientobj=ObjectGetSerializer()
    contact_man=ContactManSerializer()
    class Meta:
        model = models.QReport
        fields = ('__all__')

class ReadyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReadyReport
        fields = ('__all__')


class GetReadyReportSerializer(serializers.ModelSerializer):
    userprof=UserProfileSerializer()
    clientobj=ObjectGetSerializer()
    contact_man=ContactManSerializer()
    class Meta:
        model = models.ReadyReport
        fields = ('__all__')