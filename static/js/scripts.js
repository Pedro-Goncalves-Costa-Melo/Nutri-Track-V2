document.addEventListener("DOMContentLoaded", function () {
    let deleteButtons = document.querySelectorAll(".btn-danger");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            let confirmacao = confirm("Tem certeza que deseja excluir este paciente?");
            if (!confirmacao) {
                event.preventDefault();
            }
        });
    });
});
