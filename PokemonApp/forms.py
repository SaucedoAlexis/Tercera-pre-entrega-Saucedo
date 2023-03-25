from django import forms

from PokemonApp.models import Entrenador, Pokemon, Region


class PokemonFormulario(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nombre','tipo1','tipo2','url_img']

class EntrenadorFormulario(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = "__all__"

class RegionFormulario(forms.ModelForm):
    
    class Meta:
        model = Region
        fields = '__all__'

class BusquedaPokemonFormulario(forms.Form):

    nombre = forms.CharField(min_length=3)


class BusquedaEntrenadorFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)

class BusquedaRegionFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)

