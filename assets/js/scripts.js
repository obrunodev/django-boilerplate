$(document).ready( function () {

  $('#productTable').DataTable({
    // "processing": true,
    // "serverSide": true,
    // "ajax": "/api/v1/accessories",
    "stateSave": true,
    "language": {
      "lengthMenu": "Mostrar _MENU_ itens por página",
      "zeroRecords": "Nenhum registro encontrado",
      "info": "Mostrando _PAGE_ de _PAGES_",
      "infoEmpty": "Nenhum registro encontrado",
      "infoFiltered": "(Total de _MAX_ registros)",
      "search": "Buscar:",
      "paginate": {
        "first":      "Primeiro",
        "last":       "Último",
        "next":       "Próximo",
        "previous":   "Anterior"
      },
    }
  });

  $(document).on('click', '#deleteForm', () => {
    return confirm("Tem certeza que deseja remover este item?");
  });

});