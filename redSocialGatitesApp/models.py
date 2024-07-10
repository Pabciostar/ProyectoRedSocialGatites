from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publicacion(models.Model):
    texto = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200, default='titulo por defecto')
    fecha = models.DateTimeField("date published")
    fecha_actualizacion = models.DateTimeField(null = True)
    url_imagen = models.TextField(null=True, blank=True)
    nombre_imagen = models.TextField(null=True, blank=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.titulo}' 


class Perfil_usuario(models.Model):
    id_usuario= models.OneToOneField(User, on_delete=models.CASCADE)
    url_imagen = models.TextField(null=True, blank=True)
    nombre_imagen = models.TextField(null=True, blank=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'perfil del usuario {self.id_usuario}' 

class Corazon(models.Model):
    id_usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    id_publicacion= models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'corazon del usuario {self.id_usuario}' 

class Comentario(models.Model):
    id_usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    id_publicacion= models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'comentario del usuario {self.id_usuario}' 
    
class Imagen(models.Model):
    archivo = models.CharField(max_length=100)
