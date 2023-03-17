from django import forms


class PokemonFormulario(forms.Form):
    id = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=2)
    tipo1 = forms.CharField(min_length=3)
    tipo2 = forms.CharField()
    url_img = forms.URLField(max_length=200)

class EntrenadorFormulario(forms.Form):
    nombre = forms.CharField(min_length=2)
    genero = forms.CharField(min_length=2)
    region = forms.CharField(min_length=2)
    clase = forms.CharField(min_length=2)
    url_img = forms.URLField(max_length=200)

class RegionFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)
    profesor = forms.CharField(min_length=3)
    villanos = forms.CharField(min_length=3)
    capital = forms.CharField(min_length=3)
    liga_pokemon = forms.CharField(min_length=4)
    url_img = forms.URLField(max_length=200)

class BusquedaPokemonFormulario(forms.Form):

    nombre = forms.CharField(min_length=3)


class BusquedaEntrenadorFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)

class BusquedaRegionFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)

