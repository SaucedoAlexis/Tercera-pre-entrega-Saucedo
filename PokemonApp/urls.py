
from django.urls import path
from PokemonApp.views import *

urlpatterns = [
    path('', buscar, name='Buscar'),
    path('pokemon', ingresar_pokemon, name='Pokemon'),
    path('entrenador', ingresar_entrenador, name='Entrenador'),
    path('region', ingresar_region, name='Region')
]