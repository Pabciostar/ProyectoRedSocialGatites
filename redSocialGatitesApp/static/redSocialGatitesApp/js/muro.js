$(document).ready(function () {
    $("#btnSubirPublicacion").click(function (event) {
        //Primero se guardan el valor de la descripcion y la imagen en variables
        var descVal = $('#textPublicacion').val();
        var imgVal = $('#imgPublicacion').val();
        console.log(descVal);
        //La imagen está previamente seleccionada mientras tanto
        var imgVal = '../images/publicacion0.jp';

        //Se colocan dentro de una card

        var cardPublicacion = `
        <div class="row">
            <div class="card"">
            <img src=${imgVal} class="card-img-top img.fluid"
                alt="...">
            <div class="card-body">
                <h5 class="card-title">mishifus</h5>
                <p class="card-text">${descVal}</p>

            </div>
            </div>
        </div>
  `;

        //Se agrega la card al DOM
        $('#publicationsZone').prepend(cardPublicacion);
    });
});
