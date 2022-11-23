from rest_framework import serializers

from poke_api.Type.Serializer.SerializerType import TypeSerializer
from poke_api.Type.Model.ModelType import Type
from ..Model.ModelPokemon import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Type.objects.filter(state=1),
        source='type',
    )

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name',
            'description',
            'type',
            'type_id',
            'skill',
            'image',
            'state'
        ]
