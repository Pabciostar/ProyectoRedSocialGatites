from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagen(models.Model):
    url_imagen = models.CharField(max_length=200)
    fecha = models.DateTimeField("date published")
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.url_imagen


class Publicacion(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField("date published")
    fecha_actualizacion = models.DateTimeField(null = True)
    id_imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'publicacion del usuario {self.id_usuario}' 


class Perfil_usuario(models.Model):
    id_usuario= models.OneToOneField(User, on_delete=models.CASCADE)
    id_imagen= models.ForeignKey(Imagen, on_delete=models.CASCADE)
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
    id_publicacion= models.ForeignKey(Imagen, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'comentario del usuario {self.id_usuario}' 
