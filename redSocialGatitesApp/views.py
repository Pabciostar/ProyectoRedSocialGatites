from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    context={}
    if request.method == 'POST':
        primerNombre = request.POST['primerNombre']
        apellido = request.POST['apellido']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        nuevoUsuario = User.objects.create_user(
            first_name = primerNombre, 
            last_name = apellido, 
            username = username, 
            email = email, 
            password = password
            )
        return render(request, 'redSocialGatitesApp/index.html')
    else:
        return render(request, 'redSocialGatitesApp/index.html', context)

def muro(request):
    context={}
    return render(request, 'redSocialGatitesApp/muro.html', context)

def amichis(request):
    context={}
    return render(request, 'redSocialGatitesApp/amichis.html', context)


# DOCS:
# https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator
@login_required(login_url="index", redirect_field_name = "")
def perfil(request):
    if request.user.is_authenticated:
        print("lalala")
        # Obtener usuario logeado
        first_name = request.user.first_name
        last_name = request.user.last_name
        username = request.user.username 
        email = request.user.email

        # Crear un context con los datos del usuario
        context={
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            }
        return render(request, 'redSocialGatitesApp/perfil.html', context)
        #Si no hay usuario logeado se cae la pagina, porque  o encuentra atributos que mostrar
    # else:
    #     return redirect('index')
    

def crearUsuario(request):
    context={}
    return render(request, 'redSocialGatitesApp/crearUsuario.html', context)

def base(request):
    context={}
    return render(request, 'redSocialGatitesApp/base.html', context)

def login_user(request):
    # Obtener valores del formulario
    username = request.POST['username']
    password = request.POST['password']

    # Autentificar al usuario
    usuario = authenticate(request, username = username, password = password)
    if usuario is not None:
        login(request, usuario) 
        return redirect('perfil')
    else:
        return redirect('index')
    

def craer_perfil(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        perfil = Perfil_usuario(id_usuario = request.user, descripcion=descripcion)
        perfil.save()
        # nuevoUsuario = User.objects.create_user(
        #     first_name = primerNombre, 
        #     last_name = apellido, 
        #     username = username, 
        #     email = email, 
        #     password = password
        #     )
        return redirect('perfil')
    return render(request, 'perfil')
