from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
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


@login_required(login_url="index", redirect_field_name = "")
def perfil(request):
    if request.user.is_authenticated:
        # Obtener usuario logeado
        first_name = request.user.first_name
        last_name = request.user.last_name
        username = request.user.username 
        email = request.user.email
        context={
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'descripcion': None,
            'url_imagen': None
            }
        
        # Agrega la descripcion y la imagen al context solo si el usuario ya tiene un perfil creado
        try:
            perfil = request.user.perfil_usuario # Si no tiene perfil usuario explotara y el codigo pasara por el except.
            context['descripcion'] = perfil.descripcion # Si aun no tiene imagen esto sera None.

            # Comprueba que exista la imagen en la ruta de url_imagen
            fs = FileSystemStorage() # fs = Objeto que maneja los archivos (File System)
            if (perfil.url_imagen and fs.exists(perfil.nombre_imagen)):
                context['url_imagen'] = perfil.url_imagen

        except User.perfil_usuario.RelatedObjectDoesNotExist as error:
            pass # Si no tiene un perfil creado simplemente pass
        except Exception as error:
            print(f"Problemas con el perfil del usuario 😒 : {error}")
            return redirect('index')

        return render(request, 'redSocialGatitesApp/perfil.html', context)
    else:
        return redirect('index')
    

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
    

def crear_perfil(request):
    if request.method == 'POST':
        
        perfil = None

        # Actualiza perfil si existe, si no entonces se crea.
        try:
            #Intenta obtener el perfil del usuario segun el id del usuario autentificado
            perfil = Perfil_usuario.objects.get(id_usuario=request.user.id)
        except Perfil_usuario.DoesNotExist as error:
            # Crea un nuevo objeto basado en la clase Perfil_usuario en models.py
            perfil = Perfil_usuario(id_usuario = request.user)
        except Exception as error:
            print(f"Problemas con el crear_perfil 😒 : {error}")
            return redirect('index')

        descripcion = request.POST['descripcion'] if 'descripcion' in request.POST else None
        imagen = request.FILES['imagen'] if 'imagen' in request.FILES else None
        
        # if (descripcion):
        perfil.descripcion = descripcion
        
        # Guarda la imagen si viene en la request
        if (imagen):
            
            fs = FileSystemStorage() # fs = Objeto que maneja los archivos (File System)

            # Elimina la imagen del usuario si ya tiene una:
            if(perfil.url_imagen):
                fs.delete(perfil.nombre_imagen)

            nombre_imagen = fs.save(imagen.name, imagen)
            perfil.nombre_imagen = nombre_imagen
            perfil.url_imagen = fs.url(nombre_imagen)
                
        perfil.save()

        return redirect('perfil')
    return redirect('index')

