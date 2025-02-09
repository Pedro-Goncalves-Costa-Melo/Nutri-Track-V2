describe("Teste de Cadastro de Dieta", () => {

let nomeDieta;
let descricaoDieta;
let idadeMinima;
let idadeMaxima;

    // / beforeEach(() => {
    //    cy.visit("/dietas"); // Acessa a página de listagem de dietas
    //  });

it("Deve acessar a página de listagem de dietas", () => {
cy.visit("/dietas"); // Acessa a página de listagem de dietas
cy.contains("Adicionar Dieta").click();
});

it("Deve preencher e cadastrar uma nova dieta corretamente", () => {
cy.visit("/dietas/nova"); // Agora, acessamos diretamente a página correta
nomeDieta = "Dieta Cypress " + Date.now(); // Nome único para evitar duplicatas
descricaoDieta = "Descrição Cypress " + new Date(Date.now() + 86400000).toLocaleDateString(); // Data +1 dia
idadeMinima = "18";
idadeMaxima = "45";

cy.get('input[name="nome"]').type(nomeDieta);
cy.get('textarea[name="descricao"]').type(descricaoDieta);
cy.get('input[name="idade_minima"]').type(idadeMinima);
cy.get('input[name="idade_maxima"]').type(idadeMaxima);
cy.contains("Salvar").click();
});

it("Deve verificar se a dieta foi adicionada à lista", () => {
cy.visit("/dietas"); // Garante que estamos na listagem
cy.url().should("include", "/dietas");
cy.get("table tbody tr").last().within(() => {
    cy.contains(nomeDieta).should("be.visible");
});
});

it("Deve validar os dados cadastrados da dieta", () => {
cy.visit("/dietas"); // Garante que estamos na listagem
cy.get("table tbody tr").last().within(() => {
    cy.get("td").eq(1).should("contain", nomeDieta);      // Nome (Coluna 2)
    cy.get("td").eq(2).should("contain", descricaoDieta); // Descrição (Coluna 3)
    cy.get("td").eq(3).should("contain", idadeMinima);    // Idade Mínima (Coluna 4)
    cy.get("td").eq(4).should("contain", idadeMaxima);    // Idade Máxima (Coluna 5)
});
});

});
