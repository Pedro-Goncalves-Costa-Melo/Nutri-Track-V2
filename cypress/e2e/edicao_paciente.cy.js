describe("Teste de Edição de Paciente", () => {
  
    beforeEach(() => {
      cy.visit("/pacientes"); // Acessa a página de listagem de pacientes
    });
  
    it("Deve editar um paciente corretamente", () => {
      // Definição de um paciente a ser editado
      const nomePaciente = "Teste Cypress " + Date.now(); // Nome único para evitar conflitos
      const idadeInicial = "30";
      const alturaInicial = "1.75";
      const pesoInicial = "80";
      const dietaInicial = "Dieta Cetogênica";
      
      const novaIdade = "35";
      const novoPeso = "85";
  
      // Criar um novo paciente para edição
      cy.contains("Adicionar Paciente").click();
      cy.get('input[name="nome"]').type(nomePaciente);
      cy.get('input[name="idade"]').type(idadeInicial);
      cy.get('input[name="altura"]').type(alturaInicial);
      cy.get('input[name="peso"]').type(pesoInicial);
      cy.get('select[name="dieta_id"]').select(dietaInicial);
      cy.contains("Salvar").click();
  
      // Localizar o paciente criado e clicar no botão de edição
      cy.get("table tbody tr").last().within(() => {
        cy.contains(nomePaciente).should("be.visible");
        cy.contains("Editar").click();
      });
  
      // Alterar os dados do paciente
      cy.get('input[name="idade"]').clear().type(novaIdade);
      cy.get('input[name="peso"]').clear().type(novoPeso);
      cy.contains("Salvar").click();
  
      // Validar se os dados foram alterados corretamente na listagem
      cy.get("table tbody tr").last().within(() => {
        cy.get("td").eq(2).should("contain", novaIdade); // Idade (coluna 2)
        cy.get("td").eq(4).should("contain", novoPeso);  // Peso (coluna 4)
        //cy.contains(novaIdade).should("be.visible");
        //cy.contains(novoPeso).should("be.visible");
      });
    });
  });
  