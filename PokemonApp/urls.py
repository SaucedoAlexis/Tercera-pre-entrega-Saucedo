
from django.urls import path
from PokemonApp.views import *

urlpatterns = [
    path('', buscar, name='Buscar'),
    #Pokemons
    path('buscar_pokemon', busqueda_pokemon ,name='BuscarPokemon'),
    path('busqueda_pokemon', encontrar_pokemon, name='EncontrarPokemon'),
    path('Mostrar_Pokemons', mostrar_pokemons,name='MostrarPokemons'),
    path('pokemon', ingresar_pokemon, name='Pokemon'),
    #Entrenadores
    path('buscar_entrenador', busqueda_entrenador,name='BuscarEntrenador'),
    path('busqueda_entrenador', encontrar_entrenador, name='EncontrarEntrenador'),
    path('ingresar_entrenador', ingresar_entrenador, name='IngresarEntrenador'),
    path('mostrar_entrenadores', mostrar_entrenadores, name='MostrarEntrenadores'),
    #Region
    path('buscar_region', busqueda_region,name='BuscarRegion'),
    path('busqueda_region', encontrar_region, name='EncontrarRegion'),
    path('mostrar_regiones',mostrar_regiones , name='MostrarRegiones'),
    path('registrar_region', ingresar_region, name='IngresarRegion')
    
]