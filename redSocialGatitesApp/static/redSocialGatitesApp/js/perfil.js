document.addEventListener('DOMContentLoaded', function () {
    var btnAbrirModal = document.getElementById('btnAbrirModal');
    var miModal = new bootstrap.Modal(document.getElementById('modalPerfil'));

    btnAbrirModal.addEventListener('click', function () {
        miModal.show();
    });
    
});