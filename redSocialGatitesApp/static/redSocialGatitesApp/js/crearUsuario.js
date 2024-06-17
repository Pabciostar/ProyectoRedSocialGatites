$(document).ready(function () {
    //Se crea un array para almacenar a los usuarios
    const usuarios = []

    // Al apretar en el botón enviar ...
    $("#enviarInformacion").click(function (event) {
        event.preventDefault();
        //Crea un array para almacenar la informacion de los usuarios
        const usuario = [];

        //Obtengo los valores ingresados por el usuario
        const correo = $("#inputEmail").val();
        const nombre = $("#inputNombre").val();
        const contraseña = $("#inputPass").val();
        const edad = $("#inputEdad").val();

        //Validacion campo vacio
        if (correo.trim() === '' || nombre.trim() === '' || contraseña.trim() === '' || edad.trim() === '') {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Por favor, complete todos los campos.",
            });
            return;
        }


        console.log(correo);
        //Validaciones que no se repita el nombre
        let nombreRepetido = false;

        usuarios.forEach(function (elementoUsuarios) {
            if (elementoUsuarios[1] === nombre) {
                nombreRepetido = true;
            }
        });

        if (nombreRepetido) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "El nombre de usuario ya está en uso. Por favor, elija otro."
            });
            return;
        }

        //Validaciones que no se repita el correo
        let correoRepetido = false;
        usuarios.forEach(function (usuario) {
            if (usuario[0] === correo) {
                correoRepetido = true;
            }
        });

        if (correoRepetido) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "El correo electrónico ya está registrado"
            });
            return;
        }


        //Si cumple con las validaciones ingresa a la base de datos
        if (correoRepetido === false && nombreRepetido === false) {
            //Ingreso los datos del usuario en el array usuario
            usuario.push(correo, nombre, contraseña, edad);
            console.log(usuario);
            //Ingreso al usuario en el array usuarios
            usuarios.push(usuario);
            //lo muestro en consola
            console.log(usuarios);
            Swal.fire({
                icon: "success",
                title: "¡¡Bienvenidx!!",
                text: "Michi registrado correctamente"
            });
            return;
        }
    });




});
