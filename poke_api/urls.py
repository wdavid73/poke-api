from django.urls import path , include

urlpatterns = [
  path('pokemon/', include('poke_api.Pokemon.urls')),
  path('types/', include('poke_api.Type.urls')),
]