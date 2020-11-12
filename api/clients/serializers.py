from rest_framework import serializers
from . models import clients,clientobj,contact_man,object_contracts



class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('id','auth','client_name','client_fullname','client_inn','client_ogrn','client_kpp','client_factaddr','client_juraddr','client_telephone','client_mail','client_site')

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientobj
        fields = ('__all__')


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = object_contracts
        fields = ('__all__')

class ContactManSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_man
        fields = ('__all__')