from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from . import models

class authSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.auth
        fields=('id','username','password','status','is_active','is_staff')

    def create(self, validated_data):
            user = models.auth(
                username=validated_data['username'],
                status=validated_data['status'],
                is_active=validated_data['is_active'],
                is_staff=validated_data['is_staff'],

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


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','auth','first_name','last_name','thirdname','position','telephone','passport','birthday')
        #fields = ('__all__')





