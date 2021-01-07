from rest_framework import serializers
from . models import clients,clientobj,contact_man,object_contracts
from users.serializers import authSerializer


class ClientGetProfileSerializer(serializers.ModelSerializer):
    auth=authSerializer()
    class Meta:
        model = clients
        fields = ('id','auth','client_name','client_fullname','client_inn','client_ogrn','client_kpp','client_factaddr','client_juraddr','client_telephone','client_mail','client_site')

class ClientGetContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('id','client_name')

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('id','auth','client_name','client_fullname','client_inn','client_ogrn','client_kpp','client_factaddr','client_juraddr','client_telephone','client_mail','client_site')

class ObjectSerializer(serializers.ModelSerializer):
    client=ClientGetContractsSerializer()
    class Meta:
        model = clientobj
        fields = ('id','client','object_name','object_adress','object_telephone','object_email','object_site')

class ObjectGetSerializer(serializers.ModelSerializer):
    client=ClientGetProfileSerializer()
    class Meta:
        model = clientobj
        fields = ('id','client','object_name','object_adress','object_telephone','object_email','object_site')


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = object_contracts
        #fields = ('id','clientobj','object_contracts','contracts_name','contracts_description')
        fields = ('__all__')

class ContractGetSerializer(serializers.ModelSerializer):
    clientobj = ObjectSerializer()
    class Meta:
        model = object_contracts
        fields = ('id','clientobj','object_contracts','contracts_name','contracts_description')

class ContactManSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_man
        fields = ('__all__')