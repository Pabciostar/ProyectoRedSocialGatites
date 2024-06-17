from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'redSocialGatitesApp/index.html', context)

def muro(request):
    context={}
    return render(request, 'redSocialGatitesApp/muro.html', context)

def amichis(request):
    context={}
    return render(request, 'redSocialGatitesApp/amichis.html', context)

def perfil(request):
    context={}
    return render(request, 'redSocialGatitesApp/perfil.html', context)

def crearUsuario(request):
    context={}
    return render(request, 'redSocialGatitesApp/crearUsuario.html', context)

def base(request):
    context={}
    return render(request, 'redSocialGatitesApp/base.html', context)