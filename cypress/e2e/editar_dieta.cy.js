describe("Teste de Edição de Dieta", () => {
    beforeEach(() => {
        cy.visit("/dietas"); // Acessa a página de listagem de dietas antes de cada teste
    });

    it("Deve acessar a página de edição de uma dieta existente", () => {
        cy.get("table tbody tr").first().find(".btn-warning").click(); // Clica no botão "Editar" da primeira dieta
        cy.url().should("include", "/dietas/editar");
    });

    it("Deve modificar os dados da dieta e salvar", () => {
        cy.get("table tbody tr").first().find(".btn-warning").click(); // Entra na edição da primeira dieta

        // Gera valores novos para edição
        const novoNome = "Dieta Atualizada " + Date.now();
        const novaDescricao = "Descrição editada " + Date.now();
        const novaIdadeMin = 20;
        const novaIdadeMax = 50;

        // Preenche o formulário com novos valores
        cy.get("input[name='nome']").clear().type(novoNome);
        cy.get("textarea[name='descricao']").clear().type(novaDescricao);
        cy.get("input[name='idade_minima']").clear().type(novaIdadeMin);
        cy.get("input[name='idade_maxima']").clear().type(novaIdadeMax);

        cy.get("button[type='submit']").click(); // Salva a edição

        // Verifica se foi redirecionado para a lista de dietas
        cy.url().should("include", "/dietas");

        // Confirma se os novos dados aparecem na tabela
        cy.contains(novoNome).should("be.visible");
        cy.contains(novaDescricao).should("be.visible");
        cy.contains(novaIdadeMin).should("be.visible");
        cy.contains(novaIdadeMax).should("be.visible");
    });
});
