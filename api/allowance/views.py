
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class AllowanceList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.allowance.objects.all()
    serializer_class = serializers.AllowanceSerializer

class GetAllowanceList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.allowance.objects.all()
    serializer_class = serializers.GetAllowanceSerializer

class UserprofGetAllowanceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(request, self, pk, format=None):
        queryset = models.allowance.objects.filter(userprof=pk)
        serializer_class = serializers.GetAllowanceSerializer(queryset,many=True)
        return Response(serializer_class.data)

class AllowanceDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.allowance.objects.all()
    serializer_class = serializers.AllowanceSerializer

class VerificationsList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.itemverification.objects.all()
    serializer_class = serializers.VerificationsSerializer


class VerificationsDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.itemverification.objects.all()
    serializer_class = serializers.VerificationsSerializer

class InsuranceList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.insurance.objects.all()
    serializer_class = serializers.InsuranceSerializer

class GetInsuranceList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.insurance.objects.all()
    serializer_class = serializers.GetInsuranceSerializer

class InsuranceDetailList(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.insurance.objects.all()
    serializer_class = serializers.InsuranceSerializer