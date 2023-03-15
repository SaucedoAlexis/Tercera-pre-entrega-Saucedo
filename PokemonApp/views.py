from django.shortcuts import render
from PokemonApp.forms import PokemonFormulario, EntrenadorFormulario
from PokemonApp.models import Pokemon, Entrenador

# Create your views here.

def buscar(request):
    return render(request,'base.html')

def ingresar_pokemon(request):

    if request.method == 'POST':
        formulario = PokemonFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            pokemon = Pokemon(id=int(data['id']), nombre=data['nombre'], tipo1=data['tipo1'],
                              tipo2=data['tipo2'], url_img=data['url_img']
                              )
            pokemon.save()

    all_pokemons = Pokemon.objects.all()

    context = {
        'pokemons': all_pokemons,
        'form': PokemonFormulario()
    }


    return render(request, 'PokemonApp/Formulario_Pokemon.html', context=context)






def ingresar_entrenador(request):

    if request.method == 'POST':
        formulario = EntrenadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            entrenador = Entrenador(nombre=data['nombre'], genero=data['genero'],
                                    region=data['region'], clase=data['clase'],
                                    url_img=data['url_img']
                                    )
            entrenador.save()


    all_trainers = Entrenador.objects.all()
    context = {
        'entrenadores': all_trainers,
        'form': EntrenadorFormulario(),
    }
    return render(request, 'PokemonApp/Formulario_Entrenador.html', context=context)

def ingresar_region(request):
    return render(request, 'PokemonApp/Formulario_Region.html')