from django.shortcuts import render

from PokemonApp.forms import PokemonFormulario, EntrenadorFormulario, RegionFormulario, \
    BusquedaPokemonFormulario, BusquedaEntrenadorFormulario, BusquedaRegionFormulario
from PokemonApp.models import Pokemon, Entrenador, Region


# Create your views here.
# Pokemons
def encontrar_pokemon(request):
    
    formulario = BusquedaPokemonFormulario(
        request.GET)  # obtención de datos del request
    if formulario.is_valid():  # validación
        data = formulario.cleaned_data  # limpieza y transformación a dict
        pokemon_filtrado = Pokemon.objects.filter(
            nombre__icontains=data['nombre'])  # aplicado de filtro
        context = {
            'form_busqueda_pokemon': BusquedaPokemonFormulario(),
            # variable para usar en el template y sus datos asignados
            'pokemons': pokemon_filtrado
        }
        return render(request, 'PokemonApp\Pokemon\Resultado_Busqueda_Pokemon.html', context=context)
    
def busqueda_pokemon(request):
    return render(request,'PokemonApp\Pokemon\Busqueda_Pokemon.html',{'busqueda':BusquedaPokemonFormulario()})

def ingresar_pokemon(request):

    if request.method == 'POST': #condicional del método usado
        formulario = PokemonFormulario(request.POST) #obtención de datos del request
        if formulario.is_valid(): #validación de los datos
            data = formulario.cleaned_data #limpieza y transformación a dict
            pokemon = Pokemon(id=int(data['id']), nombre=data['nombre'], tipo1=data['tipo1'],
                              tipo2=data['tipo2'], url_img=data['url_img']
                              )#creación del objeto
            pokemon.save()#guardado en la base de datos



        context = {
            'form': PokemonFormulario(),
            'msg': 'Ok'
        } # variables y asignación de datos para el uso en el template


        return render(request, 'PokemonApp/Pokemon/Formulario_Pokemon.html', context=context)

    return render(request, 'PokemonApp/Pokemon/Formulario_Pokemon.html', context={'form':PokemonFormulario()})

def mostrar_pokemons(request):
    all_pokemons = Pokemon.objects.all()
    return render(request,'PokemonApp/Pokemon/Mostrar_Pokemons.html', {'pokemons':all_pokemons})
#Fin Pokemons

#Comienzo Entrenadores
def mostrar_entrenadores(request):
    all_trainers = Entrenador.objects.all()
    return render(request,
                   'PokemonApp/Entrenador/Mostrar_Entrenadores.html',
                    {'entrenadores':all_trainers})

def busqueda_entrenador(request):
    return render(request, 
                  'PokemonApp/Entrenador/Busqueda_entrenador.html',
                  {'form_busqueda':BusquedaEntrenadorFormulario()})

def encontrar_entrenador(request):
    formulario = BusquedaEntrenadorFormulario(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        entrenador_filtrado = Entrenador.objects.filter(nombre__icontains=data['nombre'])
        context = {
            'entrenadores': entrenador_filtrado
        }
        return render(request, 'PokemonApp/Entrenador/Resultado_Busqueda_Entrenador.html', context=context)

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


    
        context = {
            'msg': 'Ok',
            'form': EntrenadorFormulario(),
        }
        return render(request, 'PokemonApp/Entrenador/Formulario_Entrenador.html', context=context)
    return render(request, 'PokemonApp/Entrenador/Formulario_Entrenador.html', {'form':EntrenadorFormulario()})
#Fin Entrenadores

#Comienzo Regiones
def busqueda_region(request):
    return render(request,
                  'PokemonApp/Region/Busqueda_Region.html',
                  {'form_region':BusquedaRegionFormulario()})

def encontrar_region(request):
    formulario = BusquedaRegionFormulario(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        region_filtrada = Region.objects.filter(nombre__icontains=data['nombre'])
        context = {
            'regiones': region_filtrada
        }
    return render(request, 'PokemonApp/Region/Resultado_Busqueda_Region.html', context=context)

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
            
            'form': RegionFormulario(),
            'msg': 'Ok'
        }
        return render(request, 'PokemonApp/Region/Formulario_Region.html',context=context)
    
    return render(request, 'PokemonApp/Region/Formulario_Region.html',
                  {'form':RegionFormulario()}
                 )

def mostrar_regiones(request):
    all_regions = Region.objects.all()
    return render(request,
                  'PokemonApp/Region/Mostrar_Regiones.html',
                  {'regiones':all_regions})
#Fin regiones
def buscar(request):
    context = {
        'form_busqueda_pokemon' : BusquedaPokemonFormulario(),
        'form_busqueda_entrenador': BusquedaEntrenadorFormulario(),
        'form_busqueda_region': BusquedaRegionFormulario()
    }

    return render(request,'base.html', context=context)













