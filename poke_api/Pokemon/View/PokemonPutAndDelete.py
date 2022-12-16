
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError

from ..Model.ModelPokemon import Pokemon
from ..Serializer.SerializerPokemon import PokemonSerializer

class PutAndDelte(APIView):

    def get_object(self, id: int) -> Pokemon:
        try:
            return Pokemon.objects.get(id=id)
        except Pokemon.DoesNotExist:
            raise Http404

    def put(self, request: Request, id: int):
        pokemon = self.get_object(id)
        serializer = PokemonSerializer(pokemon, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'pokemon': serializer.data}, status=status.HTTP_200_OK)
        return Response({ 'error': serializer.errors }, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request: Request, id: int):
        pokemon = self.get_object(id)
        pokemon.state = 0
        pokemon.save()
        return Response(status=status.HTTP_200_OK)
        


