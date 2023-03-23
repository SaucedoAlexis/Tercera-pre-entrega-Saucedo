
from django.urls import path
from PokemonApp.views import *

urlpatterns = [
    path('', buscar, name='Inicio'),
    #Pokemons
    path('buscar_pokemon', busqueda_pokemon ,name='BuscarPokemon'),
    path('busqueda_pokemon', encontrar_pokemon, name='EncontrarPokemon'),
    path('Mostrar_Pokemons', mostrar_pokemons,name='MostrarPokemons'),
    path('pokemon', ingresar_pokemon, name='Pokemon'),
    
    #Entrenadores
    path('mostrar_entrenadores/eliminar/<nombre>', eliminar_entrenador,name='EliminarEntrenador'),
    path('mostrar_entrenadores/editar/<nombre>', editar_entrenador,name='EditarEntrenador'),
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