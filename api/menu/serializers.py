from rest_framework import serializers
from . import models
from users import serializers as userserializers

class MenuSerializer(serializers.ModelSerializer):
    #dacobjects=serializers.StringRelatedField(many=False)

    class Meta:
        depth=1
        model = models.dacmatrix
        fields = ('dacobjects','acceslevel')


