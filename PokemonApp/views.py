from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from PokemonApp.forms import PokemonFormulario, EntrenadorFormulario, PokemonRegistrar, RegionFormulario, \
    BusquedaPokemonFormulario, BusquedaEntrenadorFormulario, BusquedaRegionFormulario
from PokemonApp.models import Pokemon, Entrenador, Region


# Create your views here.
# Pokemons
def eliminar_Pokemon(request,nombre):
    get_pokemon = Pokemon.objects.get(nombre=nombre)
    get_pokemon.delete()
    return redirect('MostrarPokemons')

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
            'objects': pokemon_filtrado,
            'clase': 'Pokemon'
        }
        return render(request, 'PokemonApp\Pokemon\Resultado_Busqueda_Pokemon.html', context=context)
    
def busqueda_pokemon(request):
    return render(request,'PokemonApp\Pokemon\Busqueda_Pokemon.html',{'busqueda':BusquedaPokemonFormulario()})

def ingresar_pokemon(request):

    if request.method == 'POST': #condicional del método usado
        formulario = PokemonRegistrar(request.POST) #obtención de datos del request
        if formulario.is_valid(): #validación de los datos
            data = formulario.cleaned_data #limpieza y transformación a dict
            pokemon = Pokemon(id=int(data['id']), nombre=data['nombre'], tipo1=data['tipo1'],
                              tipo2=data['tipo2'], url_img=data['url_img']
                              )#creación del objeto
            pokemon.save()#guardado en la base de datos



        context = {
            'form': PokemonRegistrar(),
            'msg': 'Ok',
            'clase': 'Pokémon'
        } # variables y asignación de datos para el uso en el template


        return render(request, 'PokemonApp/Pokemon/Formulario_Pokemon.html', context=context)

    return render(request, 'PokemonApp/Pokemon/Formulario_Pokemon.html', context={'form':PokemonRegistrar(),
                                                                                  'clase': 'Pokémon'})

def mostrar_pokemons(request):
    all_pokemons = Pokemon.objects.all()
    context = {
        'objects': all_pokemons,
        'titles': ['Id','Nombre','Tipo 1', 'Tipo 2',
                    'Imagen','Acciones'],
        'clase': 'Pokémon'
        
    }
    return render(request,'PokemonApp/Pokemon/Mostrar_Pokemons.html', context)

def editar_pokemon(request,nombre):
    get_pokemon = Pokemon.objects.get(nombre=nombre) #Cuando no entra por el post, este get captura todos los datos
    if request.method == 'POST':#si entra por post cuando completamos la edición se valida y se modifica
        formulario = PokemonFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            
            get_pokemon.nombre = data['nombre']
            get_pokemon.tipo1 = data['tipo1']
            get_pokemon.tipo2 = data['tipo2']
            get_pokemon.url_img = data['url_img']
            
                                    
            get_pokemon.save()
        
        return redirect('MostrarPokemons')
    
    context = {
        'nombre': get_pokemon.nombre,#Parámetro del view para ir a la URL
        'form':PokemonFormulario(initial={#form para precargar los datos
        "nombre": get_pokemon.nombre,
        "tipo1": get_pokemon.tipo1,
        "tipo2": get_pokemon.tipo2,        
        "url_img": get_pokemon.url_img
        })
    }
    return render(request, 'PokemonApp/Pokemon/Editar_Pokemon.html', context=context)
#Fin Pokemons

#Comienzo Entrenadores

def eliminar_entrenador(request,nombre):
    get_entrenador = Entrenador.objects.get(nombre=nombre)
    get_entrenador.delete()
    return redirect('MostrarEntrenadores')

def mostrar_entrenadores(request):
   
    context = {
        'objects': Entrenador.objects.all(),
        'titles': ['Nombre', 'Genero', 'Región',
                   'Clase','Imagen','Acciones'],
        'clase': 'Entrenadores',
        'eliminarobject': 'EliminarEntrenador'
    }
    return render(request,
                   'PokemonApp/Entrenador/Mostrar_Entrenadores.html',
                    context=context)

def busqueda_entrenador(request):
    return render(request, 
                  'PokemonApp/Entrenador/Busqueda_entrenador.html',
                  {'form_busqueda':BusquedaEntrenadorFormulario(),
                   }
                  
                  )

def encontrar_entrenador(request):
    formulario = BusquedaEntrenadorFormulario(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        entrenador_filtrado = Entrenador.objects.filter(nombre__icontains=data['nombre'])
        context = {
            'objects': entrenador_filtrado,
            'clase': 'Entrenador'
        }
        return render(request, 'PokemonApp/Entrenador/Resultado_Busqueda_Entrenador.html', context=context)
@login_required
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
            'clase': 'Entrenador'
        }
        return render(request, 'PokemonApp/Entrenador/Formulario_Entrenador.html', context=context)
    return render(request, 'PokemonApp/Entrenador/Formulario_Entrenador.html', 
                  {'form':EntrenadorFormulario(), 'clase': 'Entrenador'})

def editar_entrenador(request,nombre):
    get_entrenador = Entrenador.objects.get(nombre=nombre) #Cuando no entra por el post, este get captura todos los datos
    if request.method == 'POST':#si entra por post cuando completamos la edición se valida y se modifica
        formulario = EntrenadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            get_entrenador.nombre=data['nombre']
            get_entrenador.genero=data['genero']
            get_entrenador.region=data['region']
            get_entrenador.clase=data['clase']
            
            get_entrenador.url_img=data['url_img']
                                    
            get_entrenador.save()
        
        return redirect('MostrarEntrenadores')
    
    context = {
        'nombre': get_entrenador.nombre,#Parámetro del view para ir a la URL
        'form':EntrenadorFormulario(initial={#form para precargar los datos
        "nombre": get_entrenador.nombre,
        "genero": get_entrenador.genero,
        "region": get_entrenador.region,
        "clase": get_entrenador.clase,
        "url_img": get_entrenador.url_img
        })
    }
    return render(request, 'PokemonApp/Entrenador/Editar_entrenador.html', context=context)
#Fin Entrenadores

#Comienzo Regiones

def editar_region(request,nombre):
    get_region = Region.objects.get(nombre=nombre)
    if request.method == 'POST':
        form = RegionFormulario(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            get_region.nombre = data['nombre']
            get_region.profesor = data['profesor']
            get_region.villanos = data['villanos']
            get_region.capital = data['capital']
            get_region.liga_pokemon = data['liga_pokemon']
            get_region.url_img = data['url_img']
            
            get_region.save()

            return redirect('MostrarRegiones')

    
    context = {
        'nombre': get_region.nombre,#Parámetro del view para ir a la URL

        'form':RegionFormulario(initial={#form para precargar los datos
        "nombre": get_region.nombre,
        "profesor": get_region.profesor,
        "villanos": get_region.villanos,
        "capital": get_region.capital,
        "liga_pokemon": get_region.liga_pokemon,
        "url_img": get_region.url_img
        }),



    }
    return render(request, 'PokemonApp/Region/Editar_Region.html', context=context)

def eliminar_region(request,nombre):
    get_region = Region.objects.get(nombre=nombre)
    get_region.delete()
    return redirect('MostrarRegiones')

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
            'objects': region_filtrada,
            'clase': 'Región'
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
            'msg': 'Ok',
            'clase': 'Región'
        }
        return render(request, 'PokemonApp/Region/Formulario_Region.html',context=context)
    
    return render(request, 'PokemonApp/Region/Formulario_Region.html',
                  {'form':RegionFormulario(), 'clase': 'Región'}
                 )

def mostrar_regiones(request):
    
    context = {
        'objects': Region.objects.all(),
        'titles': ['Nombre','Profesor','Villanos','Capital',
                   'Liga Pokémon','Imagen','Acciones'],
        'clase': 'Region'
    }
    return render(request,
                  'PokemonApp/Region/Mostrar_Regiones.html',
                  context = context)
#Fin regiones
def buscar(request):
    context = {
        'form_busqueda_pokemon' : BusquedaPokemonFormulario(),
        'form_busqueda_entrenador': BusquedaEntrenadorFormulario(),
        'form_busqueda_region': BusquedaRegionFormulario()
    }

    return render(request,'base.html', context=context)













