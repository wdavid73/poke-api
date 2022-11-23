from django.urls import path
from .View.PokemonGetAndPost import GetAndPost
from .View.PokemonGetAndPost import CreatePokemon

urlpatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
    path('create/', CreatePokemon.as_view(), name="create_pokemon")
]
