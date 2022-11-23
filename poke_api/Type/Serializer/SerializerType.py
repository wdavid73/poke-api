from rest_framework import serializers
from ..Model.ModelType import Type

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ['id', 'name', 'description', 'color', 'state']
