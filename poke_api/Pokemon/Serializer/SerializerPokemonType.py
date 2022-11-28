from rest_framework import serializers
from ..Model.ModelPokemon import Pokemon_Type, Pokemon
from ..Serializer.SerializerPokemon import PokemonSerializer
from ...Type.Serializer.SerializerType import TypeSerializer
from ...Type.Model.ModelType import Type

class Pokemon_Type_Serializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer(read_only=True)
    pokemon_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Pokemon.objects.filter(state=1),
        source="pokemon",
    )
    
    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Type.objects.filter(state=1),
        source="type"
    )
    
    class Meta:
        model = Pokemon_Type
        fields = ['id', 'pokemon', 'pokemon_id', 'type', 'type_id']