from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('index', views.index, name='index'),
    path('perfil', views.perfil, name='perfil'),
    path('amichis', views.amichis, name='amichis'),
    path('crearUsuario', views.crearUsuario, name='crearUsuario'),
    path('muro', views.muro, name='muro'),
    path('login', views.login_user, name='login'),
    path('crear_perfil', views.crear_perfil, name='crear_perfil'),
    path('crearPublicacion', views.crear_publicacion, name='crearPublicacion'),
    path('editarPublicacion/<int:id>', views.editarPublicacion, name='editarPublicacion'),
    path('editarPublicacionPOST', views.editarPublicacionPOST, name='editarPublicacionPOST'),
    path('eliminarPublicacion/<int:id>', views.eliminarPublicacion, name='eliminarPublicacion'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]