
from django.urls import path
from PokemonApp.views import *

urlpatterns = [
    path('', buscar, name='Buscar'),
    path('buscar_pokemon', buscar_pokemon,name='BuscarPokemon'),
    path('buscar_region', buscar_region,name='BuscarRegion'),
    path('buscar_entrenador', buscar_entrenador,name='BuscarEntrenador'),
    path('pokemon', ingresar_pokemon, name='Pokemon'),
    path('entrenador', ingresar_entrenador, name='Entrenador'),
    path('region', ingresar_region, name='Region')
]