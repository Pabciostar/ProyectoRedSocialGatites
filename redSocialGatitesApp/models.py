from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagen(models.Model):
    url_imagen = models.CharField(max_length=200)
    fecha = models.DateTimeField("date published")
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class Publicacion(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField("date published")
    id_imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class Perfil_usuario(models.Model):
    id_usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    id_imagen= models.ForeignKey(Imagen, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
