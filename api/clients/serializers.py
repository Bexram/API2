from rest_framework import serializers
from . models import clients,clientobj,contact_man,object_contracts
from users.serializers import authSerializer,GetUserProfileSerializer


class ClientGetProfileSerializer(serializers.ModelSerializer):
    userprof=GetUserProfileSerializer()
    auth=authSerializer()
    class Meta:
        model = clients
        #fields = ('id','auth','userprof','client_name','client_fullname','client_inn','client_ogrn','client_kpp','client_factaddr','client_juraddr','client_telephone','client_site')
        fields = ('__all__')

class ClientGetContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('__all__')

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('__all__')

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientobj
        fields = ('__all__')

class ObjectGetSerializer(serializers.ModelSerializer):
    client=ClientGetProfileSerializer()
    class Meta:
        model = clientobj
        fields = ('__all__')


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = object_contracts
        #fields = ('id','clientobj','object_contracts','contracts_name','contracts_description')
        fields = ('__all__')

class ContractGetSerializer(serializers.ModelSerializer):
    clientobj = ObjectGetSerializer()
    class Meta:
        model = object_contracts
        fields = ('__all__')

class ContactManSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_man
        fields = ('__all__')

class ContactManGetSerializer(serializers.ModelSerializer):
    client=ClientProfileSerializer()
    class Meta:
        model = contact_man
        fields = ('__all__')