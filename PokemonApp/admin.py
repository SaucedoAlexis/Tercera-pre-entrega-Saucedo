from django.contrib import admin

from PokemonApp.models import Entrenador, Pokemon, Region

# Register your models here.
admin.site.register(Pokemon)

admin.site.register(Entrenador)

admin.site.register(Region)
