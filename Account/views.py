from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from Account.forms import UserRegistrerForm
# Create your views here.

def login_account(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data['username'],
                                password=data['password'])
            
            if user:
                login(request, user)

                context = {
                    'user': data['username']
                }
                return redirect("Inicio")
            else:
                return redirect('MostrarPokemons')
            
        
    
    context = {
        "form":AuthenticationForm()
    }

    return render(request, "account/login.html", context=context)

def register_account(request):
    if request.method == 'POST':
        
        # form = UserCreationForm(request.POST)

        form = UserRegistrerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accountLogin')
    # UserCreationForm()
    form = UserRegistrerForm()
    context ={
        'form':form
    }

    return render(request, 'account/login.html', context=context)