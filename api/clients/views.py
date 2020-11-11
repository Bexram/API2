from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models

class ClientList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientProfileSerializer


class ClientDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientProfileSerializer


class ObjectList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.clientobj.objects.all()
    serializer_class = serializers.ObjectSerializer


class ObjectDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.clientobj.objects.all()
    serializer_class = serializers.ObjectSerializer


class ContactManList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.contact_man.objects.all()
    serializer_class = serializers.ContactManSerializer


class ContactManDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.contact_man.objects.all()
    serializer_class = serializers.ContactManSerializer


class ContractList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.object_contracts.objects.all()
    serializer_class = serializers.ContractSerializer


class ContractDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.object_contracts.objects.all()
    serializer_class = serializers.ContractSerializer