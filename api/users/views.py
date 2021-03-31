from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from menu.models import dacmatrix,dacobj
from .serializers import GetUserSerializer, authSerializer, UserProfileSerializer, AutoSerializer, UnitSerializer, GetAutoSerializer
from .models import UserProfile, auth, Auto, Units


class AuthList(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        snippets = auth.objects.all()
        serializer = authSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = authSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['status'] is not None and serializer.data['status'] == 1:
                modules=[
                    {'m': 1, 'a': 1},
                    {'m': 6, 'a': 1},
                    {'m': 7, 'a': 2},
                    {'m': 12, 'a': 1},
                    {'m': 13, 'a': 1},
                    {'m': 9, 'a': 1},
                    {'m': 10, 'a': 1},
                         ]

                for mod in modules:
                    basedacces=dacmatrix(
                        subjects=auth.objects.get(username=serializer.data['username']),
                        dacobjects=dacobj.objects.get(id=mod['m']),
                        acceslevel=mod['a']
                    )
                    basedacces.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    queryset = auth.objects.filter(status=1).order_by('-is_active','userprofile__last_name')
    serializer_class = GetUserSerializer

class AutoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class AutoDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class GetAutoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(request, self, pk, format=None):
        queryset = Auto.objects.filter(userprof=pk)
        serializer = AutoSerializer(queryset, many=True)
        return Response(serializer.data)

class UnitList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Units.objects.all()
    serializer_class = UnitSerializer


class UnitDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Units.objects.all()
    serializer_class = UnitSerializer