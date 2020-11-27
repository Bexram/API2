from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .serializers import GetUserSerializer, authSerializer, UserProfileSerializer
from .models import UserProfile, auth


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
    permission_classes = [IsAuthenticated]
    queryset = auth.objects.filter(status=1)
    serializer_class = GetUserSerializer
