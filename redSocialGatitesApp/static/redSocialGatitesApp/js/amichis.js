$(document).ready(function() {
    // Obtener el contenedor donde se agregarán las imágenes
    const contenedorGatos = $("#contenedorGatos");

    // Array de URLs de imágenes
    const imagenes = [
        "https://cdn2.thecatapi.com/images/25.gif",
        "https://cdn2.thecatapi.com/images/10h.jpg",
        "https://cdn2.thecatapi.com/images/1ms.jpg",
        "https://cdn2.thecatapi.com/images/baf.jpg",
        "https://cdn2.thecatapi.com/images/bjp.jpg",
        "https://cdn2.thecatapi.com/images/bpk.jpg",
        "https://cdn2.thecatapi.com/images/brh.jpg",
        "https://cdn2.thecatapi.com/images/c78.jpg",
        "https://cdn2.thecatapi.com/images/e03.jpg",
        "https://cdn2.thecatapi.com/images/MTU1MTM1Mg.jpg"
    ];

    const imagenesBuscar = [
        // URLs de imágenes para buscar
    ];

    // Función para agregar las imágenes al contenedor
    function agregarImagenes() {
        // Variable para almacenar el HTML generado dinámicamente
        let html = '';

        // Iterar sobre el array de imágenes
        for (let i = 0; i < imagenes.length; i++) {
            // Agregar la etiqueta de imagen al HTML
            html += 
            `<div class="row">
                <div class="card">
                    <img src="${imagenes[i]}" class="card-img-top" alt="Gato">
                    <div class="card-body">
                        <h5 class="card-title">Nombre Usuario</h5>
                        <p class="card-text">Descripción</p>
                    </div>
                </div>
            </div>`;
        }

        // Agregar el HTML al contenedor
        contenedorGatos.html(html);
    }

    // Llamar a la función para agregar las imágenes al cargar la página
    agregarImagenes();
})