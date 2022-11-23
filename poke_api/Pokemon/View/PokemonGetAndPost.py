from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from ..Model.ModelPokemon import Pokemon
from ..Serializer.SerializerPokemon import PokemonSerializer


class GetAndPost(APIView):

    def get(self, request: Request):
        pokemons = Pokemon.objects.filter(state=1)
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatePokemon(GenericAPIView):
    serializer_class = PokemonSerializer

    def post(self, request) -> Response:
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'pokemon': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.Http_400)
