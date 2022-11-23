from django.urls import path
from .View.TypeGetandPost import GetAndPost
from .View.TypeGetandPost import CreateTypePokemon

urlpatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
    path("create/", CreateTypePokemon.as_view(), name="create_type_pokemon")
]
