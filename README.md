# GATITES DJANGO APP

## Cambios respecto a la rama MAIN
- Se ha dejado de rastrear por git los archivos .pyc (archivos compilados de python).
- Se ha dejado de rastrear por git la base de datos (archivo db.sqlite3).
- Se ha dejado de rastrear por git el entorno virtual (venv).
- Se ha agregado un "django decorator" en views.py perfil(). Ahora esta vista se podra ver solo si el usuario se encuentra autentificado.
- Se ha agregado una condicion en base.html donde, si el usuario no esta autentificado no mostrara el link a la ruta de perfil.
- Se ha modificado el modelo Perfil_usuario para que acepte descripcion null y agregado la propiedad nombre_imagen.
- En settings.py se ha agregado MEDIA_ROOT y MEDIA_URL para guardar/servir archivos.
- En urls.py del proyecto (no la app) se ha configurado MEDIA_ROOT y MEDIA_URL.
- En perfil.html se ha modificado para que ahora muestre la descripcion del usuario si tiene.
- En perfil.html se han modificado los formularios para cambiar descripcion e imagen, utilizando la misma vista.

## Installation
- Clona este repositorio a tu máquina local usando:
```sh
git clone
```
- Luego entra al repositorio y crea un nuevo entorno virtual:
```sh
python -m venv NOMBRE_ENTORNO_VIRTUAL
```
- Activa el entorno virtual usando:
```sh
\NOMBRE_ENTORNO_VIRTUAL\Scripts\activate
```
- Instala las dependencias del proyecto (Se instalará Django y todas las dependencias necesarias):
```sh
pip install -r requirements.txt
```
- Corre las migraciones de la app (Esto creará las tablas en un nuevo archivo db.sqlite3):
```sh
py .\manage.py makemigrations
py .\manage.py migrate
```
- Finalmente levanta el servidor :D
```sh
py .\manage.py runserver
```

## DOCUMENTACION
- [@login_required](https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator): Solo muestra la vista si el usuario esta autentificado
- [FyleSystem](https://docs.djangoproject.com/en/5.0/ref/files/storage/#the-filesystemstorage-class): Clase que nos ayuda a manejar archivos en django con una previa configuracion en settings.py

## Datos extra:
- Los archivos compilados y las bases de datos no se suelen reastrear en git, por eso los he eliminado, ya que los compilados se crean cada vez que levantas la app y la base de datos se crear al correr las migraciones del proyecto.
- Los entornos virtuales son solo locales, por eso no se deben reastrear en git. En cambio, se deben guardar las dependencias en un archivo requirements.txt (en el caso de Django). De esta manera al descargar el repositorio, solo se vuelve a crear el entorno virtual, se ejecuta el comando para instalar dependencias y listo.