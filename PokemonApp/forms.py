from django import forms


class PokemonFormulario(forms.Form):
    id = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=2)
    tipo1 = forms.CharField(min_length=3)
    tipo2 = forms.CharField(min_length=3)
    url_img = forms.URLField(max_length=200)

class EntrenadorFormulario(forms.Form):
    nombre = forms.CharField(min_length=2)
    genero = forms.CharField(min_length=2)
    region = forms.CharField(min_length=2)
    clase = forms.CharField(min_length=2)
    url_img = forms.URLField(max_length=200)