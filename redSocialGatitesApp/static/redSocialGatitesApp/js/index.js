// Controlador del Modal
$(document).ready(function() {
  var btnAbrirModal = $('#btnAbrirModal');
  var miModal = new bootstrap.Modal(document.getElementById('miModal'));
  
  btnAbrirModal.on('click', function() {
      miModal.show();
  });
});

