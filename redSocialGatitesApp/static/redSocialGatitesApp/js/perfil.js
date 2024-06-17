document.addEventListener('DOMContentLoaded', function () {
    var btnAbrirModal = document.getElementById('btnAbrirModal');
    var miModal = new bootstrap.Modal(document.getElementById('modalPerfil'));

    btnAbrirModal.addEventListener('click', function () {
        miModal.show();
    });
});



$(document).ready(function () {
    //Código para cambiar imagen de perfil
    $("#btnCambiarImgPerfil").click(function (event) {
        //Se captura la nueva imagen de perfil
        var nuevaImg = $("#inputNuevaImg").val();

        //A continuación se realiza un prototipo incompleto pero es la idea general
        //URL nueva imagen
        var nuevaImg = '../images/imgGatoPerfilNuevo.jpg'

        //Se vacía el contendero de la imagen
        $('#imgPerfilContainerModal').empty();
        $('#imgPerfilContainer').empty();

        //Creo una etiqueta img con el id correspondiente
        var imagen = $('<img>').attr('id', 'img-perfil');

        //Le cambio el src
        imagen.attr('src', nuevaImg);

        //Lo agrego al DOM
        $('#imgPerfilContainerModal').append(imagen);
        $('#imgPerfilContainer').append(imagen);



    });


    //Código para cambiar descripción
    $("#btnCambiarDesc").click(function (event) {
        //Se captura la nueva descripcion
        const nuevaDesc = $("#inputNuevaDesc").val();
        console.log(nuevaDesc);

        $('#descripcion').empty();

        $('#descripcionModal').text(nuevaDesc);
        $('#descripcionPerfil').text(nuevaDesc);


    });

});