from django.urls import path
from .View.PokemonGetAndPost import GetAndPost
from .View.PokemonGetAndPost import CreatePokemon
from .View.PokemonGetAndPost import testPokemon
from .View.PokemonPutAndDelete import PutAndDelte

urlpatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
    path('create/', CreatePokemon.as_view(), name="create_pokemon"),
    path('<id>/', PutAndDelte.as_view(), name="put_and_delete"),
    path('test/', testPokemon.as_view(), name="test_pokemon"),
]
