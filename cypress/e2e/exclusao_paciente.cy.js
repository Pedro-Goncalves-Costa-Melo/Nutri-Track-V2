describe("Teste de Exclusão de Paciente", () => {
  
    let nomePaciente;
  
    beforeEach(() => {
      cy.visit("/pacientes"); // Acessa a página de listagem de pacientes
    });
  
    it("Deve cadastrar um novo paciente para ser excluído", () => {
      nomePaciente = "Teste Cypress " + Date.now(); // Nome único para evitar conflitos
      const idade = "40";
      const altura = "1.80";
      const peso = "90";
      const dieta = "Dieta Mediterrânea";
  
      // Criar um novo paciente
      cy.contains("Adicionar Paciente").click();
      cy.get('input[name="nome"]').type(nomePaciente);
      cy.get('input[name="idade"]').type(idade);
      cy.get('input[name="altura"]').type(altura);
      cy.get('input[name="peso"]').type(peso);
      cy.get('select[name="dieta_id"]').select(dieta);
      cy.contains("Salvar").click();
    });
  
    it("Deve verificar se o paciente foi adicionado à tabela", () => {
      cy.get("table tbody tr").last().within(() => {
        cy.contains(nomePaciente).should("be.visible");
      });
    });
  
    it("Deve excluir o paciente corretamente", () => {
      cy.get("table tbody tr").last().within(() => {
        cy.contains("Excluir").click();
      });
  
      // Confirmação do alerta/modal se necessário
      cy.on("window:confirm", () => true);
    });
  
    it("Deve garantir que o paciente foi removido da tabela", () => {
      cy.get("table tbody").should("not.contain", nomePaciente);
    });
  
  });
  