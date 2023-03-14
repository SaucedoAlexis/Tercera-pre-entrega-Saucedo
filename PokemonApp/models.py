
from django.db.models import Model
from django.db.models import CharField, PositiveIntegerField, URLField


# Create your models here.
class Pokemon(Model):
    id = PositiveIntegerField(primary_key=True)
    nombre = CharField(max_length=40)
    tipo1 = CharField(max_length=40)
    tipo2 = CharField(max_length=40)
    url_img = URLField(max_length=200)


class Entrenador(Model):
    nombre = CharField(max_length=40)
    genero = CharField(max_length=10)
    region = CharField(max_length=40)
    clase = CharField(max_length=40)
    url_img = URLField(max_length=200)


class Region(Model):
    profesor = CharField(max_length=40)
    villanos = CharField(max_length=40)
    capital = CharField(max_length=40)
    liga_pokemon = CharField(max_length=40)
