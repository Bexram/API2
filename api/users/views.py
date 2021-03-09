from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .serializers import GetUserSerializer, authSerializer, UserProfileSerializer, AutoSerializer, UnitSerializer, GetAutoSerializer
from .models import UserProfile, auth, Auto, Units


class AuthList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = auth.objects.all()
    serializer_class = authSerializer


class AuthDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = auth.objects.all()
    serializer_class = authSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class GetUserList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = auth.objects.filter(status=1).order_by('-is_active','userprofile__last_name')
    serializer_class = GetUserSerializer

class AutoList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class AutoDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class GetAutoList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Auto.objects.all()
    serializer_class = GetAutoSerializer

class UnitList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Units.objects.all()
    serializer_class = UnitSerializer


class UnitDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Units.objects.all()
    serializer_class = UnitSerializer