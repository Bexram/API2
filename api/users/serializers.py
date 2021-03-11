from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from . import models


class authSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.auth
        fields = ('id', 'username', 'password', 'status', 'is_active', 'is_staff','email')

    def create(self, validated_data):
        user = models.auth(
            username=validated_data['username'],
            status=validated_data['status'],
            is_active=validated_data['is_active'],
            is_staff=validated_data['is_staff'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Units
        fields = ('__all__')


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auto
        fields = ('__all__')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        # #fields = (
        #     'id', 'auth', 'first_name', 'last_name', 'thirdname', 'position', 'telephone', 'email', 'passport',
        #     'birthday',
        #     'foto','unit')
        fields = ('__all__')

class GetUserProfileSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    class Meta:
        model = models.UserProfile
        # #fields = (
        #     'id', 'auth', 'first_name', 'last_name', 'thirdname', 'position', 'telephone', 'email', 'passport',
        #     'birthday',
        #     'foto','unit')
        fields = ('__all__')

class GetUserSerializer(serializers.ModelSerializer):
    userprofile = GetUserProfileSerializer()

    class Meta:
        model = models.auth
        fields = ('id', 'username', 'status', 'is_active', 'userprofile','email')


class GetAutoSerializer(serializers.ModelSerializer):
    userprof = UserProfileSerializer()

    class Meta:
        model = models.Auto
        fields = ('__all__')
