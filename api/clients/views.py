from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models


class ClientGetList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientGetProfileSerializer


class ClientList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientProfileSerializer


class ClientDetailList(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientProfileSerializer


class ObjectList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.clientobj.objects.all()
    serializer_class = serializers.ObjectSerializer


class ObjectDetailList(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.clientobj.objects.all()
    serializer_class = serializers.ObjectSerializer


class ContactManList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.contact_man.objects.all()
    serializer_class = serializers.ContactManSerializer


class ContactManDetailList(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.contact_man.objects.all()
    serializer_class = serializers.ContactManSerializer


class ContractList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.object_contracts.objects.all()
    serializer_class = serializers.ContractSerializer


class ContractDetailList(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.object_contracts.objects.all()
    serializer_class = serializers.ContractSerializer


class GetObjectList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.clientobj.objects.filter(client=pk)
        serializer = serializers.ObjectSerializer(queryset, many=True)
        return Response(serializer.data)


class GetContractList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.clientobj.object_contracts.filter(clientobj=pk)
        serializer = serializers.ContractSerializer(queryset, many=True)
        return Response(serializer.data)
