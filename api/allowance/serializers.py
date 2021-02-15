from rest_framework import serializers
from . import models
from users.serializers import UserProfileSerializer

class AllowanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.allowance
        fields = ('__all__')

class VerificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.itemverification
        fields = ('__all__')

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.insurance
        fields = ('__all__')

class GetAllowanceSerializer(serializers.ModelSerializer):
    userprof=UserProfileSerializer()
    class Meta:
        model = models.allowance
        fields = ('__all__')


class GetInsuranceSerializer(serializers.ModelSerializer):
    userprof = UserProfileSerializer()
    class Meta:
        model = models.insurance
        fields = ('__all__')