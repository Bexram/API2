from rest_framework import status, generics
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models


class ClientGetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientGetProfileSerializer

class UserprofClientGetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(request, self, pk, format=None):
        queryset = models.clients.objects.filter(userprof=pk)
        serializer_class = serializers.ClientGetProfileSerializer(queryset,many=True)
        return Response(serializer_class.data)



class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientProfileSerializer


class ClientDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.clients.objects.all()
    serializer_class = serializers.ClientProfileSerializer


class ObjectList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.clientobj.objects.all()
    serializer_class = serializers.ObjectSerializer


class ObjectDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.clientobj.objects.all()
    serializer_class = serializers.ObjectSerializer


class ContactManList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.contact_man.objects.all()
    serializer_class = serializers.ContactManSerializer


class ContactManDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.contact_man.objects.all()
    serializer_class = serializers.ContactManSerializer

class GetContactManList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.contact_man.objects.filter(client=pk)
        serializer = serializers.ContactManGetSerializer(queryset, many=True)
        return Response(serializer.data)


class ContractList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self,  format=None):
        queryset = models.object_contracts.objects.all()
        serializer = serializers.ContractSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        file_serializer = serializers.ContractSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.object_contracts.objects.all()
    serializer_class = serializers.ContractSerializer


class GetObjectList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.clientobj.objects.filter(client=pk)
        serializer = serializers.ObjectGetSerializer(queryset, many=True)
        return Response(serializer.data)


class GetContractList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.object_contracts.objects.filter(clientobj=pk)
        serializer = serializers.ContractGetSerializer(queryset, many=True)
        return Response(serializer.data)


