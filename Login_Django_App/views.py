from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def index( request ):
    return render( request, 'index.html')

def home( request ):
    return render( request, 'home.html')

def signup( request ):
    if request.method == 'GET':
        return render( request, 'Manejo-Sesion/signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            
            except IntegrityError:
                return render( request, 'Manejo-Sesion/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
                
        return render( request, 'Manejo-Sesion/signup.html', {
            'form': UserCreationForm,
            'error': 'La contraseña no coincide'
        })
        
def sigin( request ):
    if request.method == 'GET':
        return render( request, 'Manejo-Sesion/signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render( request, 'Manejo-Sesion/signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
            
        else:
            login( request, user)
            return redirect('home')
        
    
def signout( request ):
    logout( request )
    return redirect('index')