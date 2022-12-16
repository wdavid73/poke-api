from django.http import HttpResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ParseError

from ..Model.ModelPokemon import Pokemon
from ..Serializer.SerializerPokemon import PokemonSerializer
from ..Serializer.SerializerPokemonType import Pokemon_Type_Serializer


class GetAndPost(APIView):

    def get(self, request: Request):
        pokemons = Pokemon.objects.filter(state=1)
        serializer = PokemonSerializer(pokemons, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class testPokemon(APIView):
    def get(self, request: Request):
        return HttpResponse('FUNCIONA ENDPOINT')


class CreatePokemon(GenericAPIView):
    serializer_class = PokemonSerializer

    def post(self, request) -> Response:
        try:
            pokemon = request.data.copy()
            type_ids = pokemon['type_id']
            del pokemon['type_id']
            
            serializer = PokemonSerializer(
                data=pokemon, context={'request': request}
            )
            
            if serializer.is_valid():    
                serializer.save()
                serializer_type_pokemon = save_type_pokemon(type_ids, serializer.data, request)
                return Response(
                    {
                        'pokemon': serializer.data,
                        'pokemon_types': serializer_type_pokemon,
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response({'error': serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            raise ParseError(f"an error ocurred with {e}")
        

def save_type_pokemon(types, pokemon, request: Request):
    items = []
    for type_id in types:
        data = {}
        data["pokemon_id"] = pokemon["id"]
        data["type_id"] = type_id
        serializer = Pokemon_Type_Serializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            items.append(serializer.data)
        else:
            return serializer.errors
    return items
