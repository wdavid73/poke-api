from rest_framework import serializers

from poke_api.Type.Serializer.SerializerType import TypeSerializer
from poke_api.Type.Model.ModelType import Type
from ..Model.ModelPokemon import Pokemon, Pokemon_Type


class PokemonSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True, many=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name',
            'description',
            'type',
            'skill',
            'image',
            'state'
        ]
