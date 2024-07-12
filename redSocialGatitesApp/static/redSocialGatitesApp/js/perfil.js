$(document).ready(function() {
    var btnAbrirModal = $('#btnAbrirModal');
    var miModal = new bootstrap.Modal(document.getElementById('modalPerfil'));
    
    btnAbrirModal.on('click', function() {
        miModal.show();
    });
});