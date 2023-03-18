from django.shortcuts import render

from PokemonApp.forms import PokemonFormulario, EntrenadorFormulario, RegionFormulario, \
    BusquedaPokemonFormulario, BusquedaEntrenadorFormulario, BusquedaRegionFormulario
from PokemonApp.models import Pokemon, Entrenador, Region


# Create your views here.
def buscar_pokemon(request):
    formulario = BusquedaPokemonFormulario(request.GET) #obtención de datos del request
    if formulario.is_valid(): #validación
        data = formulario.cleaned_data #limpieza y transformación a dict
        pokemon_filtrado = Pokemon.objects.filter(nombre__icontains=data['nombre']) #aplicado de filtro
        context = {
            'pokemons': pokemon_filtrado #variable para usar en el template y sus datos asignados
        }
        return render(request,'PokemonApp/Busqueda_Pokemon.html', context=context)

def buscar_entrenador(request):
    formulario = BusquedaEntrenadorFormulario(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        entrenador_filtrado = Entrenador.objects.filter(nombre__icontains=data['nombre'])
        context = {
            'entrenadores': entrenador_filtrado
        }
        return render(request, 'PokemonApp/Busqueda_Entrenador.html', context=context)

def buscar_region(request):
    formulario = BusquedaRegionFormulario(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        region_filtrada = Region.objects.filter(nombre__icontains=data['nombre'])
        context = {
            'regiones': region_filtrada
        }
        return render(request, 'PokemonApp/Busqueda_Region.html', context=context)


def buscar(request):
    context = {
        'form_busqueda_pokemon' : BusquedaPokemonFormulario(),
        'form_busqueda_entrenador': BusquedaEntrenadorFormulario(),
        'form_busqueda_region': BusquedaRegionFormulario()
    }

    return render(request,'base.html', context=context)

def ingresar_pokemon(request):

    if request.method == 'POST': #condicional del método usado
        formulario = PokemonFormulario(request.POST) #obtención de datos del request
        if formulario.is_valid(): #validación de los datos
            data = formulario.cleaned_data #limpieza y transformación a dict
            pokemon = Pokemon(id=int(data['id']), nombre=data['nombre'], tipo1=data['tipo1'],
                              tipo2=data['tipo2'], url_img=data['url_img']
                              )#creación del objeto
            pokemon.save()#guardado en la base de datos

    all_pokemons = Pokemon.objects.all() #obtención de todos los objetos de la base de datos

    context = {
        'pokemons': all_pokemons,
        'form': PokemonFormulario()
    } # variables y asignación de datos para el uso en el template


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
    all_region = Region.objects.all()

    if request.method == 'POST':
        formulario = RegionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            region = Region(profesor=data['profesor'], villanos=data['villanos'],
                            capital=data['capital'], liga_pokemon=data['liga_pokemon'],
                            url_img=data['url_img'], nombre=data['nombre']
                            )
            region.save()

    context = {
        'regiones': all_region,
        'form': RegionFormulario()
    }
    return render(request, 'PokemonApp/Formulario_Region.html',context=context)

