describe("Teste de Exclusão de Dieta", () => {
  
    beforeEach(() => {
      cy.visit("/dietas");
    });
  
    it("Deve excluir uma dieta com sucesso", () => {
      // Criando uma nova dieta para garantir que temos algo para excluir
      const nomeDieta = `Dieta Teste ${Date.now()}`;
      cy.visit("/dietas/nova");
      cy.get("input[name='nome']").type(nomeDieta);
      cy.get("textarea[name='descricao']").type("Dieta para testes de exclusão");
      cy.get("input[name='idade_minima']").type("18");
      cy.get("input[name='idade_maxima']").type("65");
      cy.get("button[type='submit']").click();
      
      // Voltando para a lista de dietas
      cy.visit("/dietas");
  
      // Encontrando a dieta recém criada na tabela e pegando a linha correta
      cy.contains("td", nomeDieta).parent().within(() => {
        cy.get(".delete-btn").click(); // Clicar no botão de excluir
      });
  
      // Confirmando o alerta/modal de exclusão
      cy.on("window:confirm", () => true);
  
      // Garantindo que a dieta foi removida da lista
      cy.visit("/dietas");
      cy.contains(nomeDieta).should("not.exist");
    });
  
  });
  