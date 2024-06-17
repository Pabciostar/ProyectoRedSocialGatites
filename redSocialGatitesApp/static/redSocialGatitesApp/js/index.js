// Controlador del Modal
document.addEventListener('DOMContentLoaded', function() {
    var btnAbrirModal = document.getElementById('btnAbrirModal');
    var miModal = new bootstrap.Modal(document.getElementById('miModal'));
    
    btnAbrirModal.addEventListener('click', function() {
      miModal.show();
    });
  });

//Código para iniciar sesion
    $(document).ready(function () {
    //Este array representa la información en la base de datos. No considera encriptacion
    const usuarios = [['ferrata@gmail.com', 'michi_ferrata', 'ferrata123', 3], ['pabcio@gmail.com', 'michi_pabcio', 'pabcio123', 2], ['uwu@gmail.com', 'michi_uwu', 'uwu123', 1]]

    // Al apretar en el botón enviar ...
    $("#btnVerificar").click(function (event) {
        event.preventDefault();

    //     //Obtengo los valores ingresados por el usuario
        const correo = $("#inputEmail").val();
        const contraseña = $("#inputPass").val();

    //     //Valido que coincidan con alguno de la base de datos
        let usuarioEncontrado = false;
        let contrasenaCorrecta = false;
        usuarios.forEach(function(usuario) {
            if(usuario[0].toLowerCase === correo.toLowerCase){
                usuarioEncontrado = true;
            }

            if(usuario[2] === contraseña){
                contrasenaCorrecta = true;
            }
        })
        
        if(usuarioEncontrado === true && contrasenaCorrecta === true) {
            window.location.href = "../muro/muro.html";
        } else{
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "Los datos ingresados no son correctos",
            });
        }

    });

});