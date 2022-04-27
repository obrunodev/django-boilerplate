$(document).ready(() => {

  $('#delete').click((e) => {
    if (!confirm('Tem certeza que deseja deletar?')) {
      e.preventDefault();
    }
  });

});