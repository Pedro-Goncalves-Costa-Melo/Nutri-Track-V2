// describe("Teste de Cadastro de Paciente", () => {
  
//     beforeEach(() => {
//       cy.visit("/pacientes"); // Acessa a página de listagem de pacientes
//     });
  
//     it("Deve cadastrar um novo paciente corretamente", () => {
//       cy.contains("Adicionar Paciente").click(); // Clica no botão para adicionar paciente
  
//       // Preenche os campos do formulário
//       cy.get('input[name="nome"]').type("João Silva");
//       cy.get('input[name="idade"]').type("30");
//       cy.get('input[name="altura"]').type("1.75");
//       cy.get('input[name="peso"]').type("80");
//       cy.get('select[name="dieta_id"]').select("Dieta Cetogênica"); // Seleciona uma dieta
  
//       // Submete o formulário
//       cy.contains("Salvar").click();
  
//       // Verifica se o paciente foi cadastrado com sucesso
//       cy.contains("João Silva").should("be.visible");
//       cy.contains("30").should("be.visible");
//       cy.contains("1.75").should("be.visible");
//       cy.contains("80").should("be.visible");
//       cy.contains("Dieta Cetogênica").should("be.visible");
//     });
//   });
describe("Teste de Cadastro de Paciente", () => {
  
    beforeEach(() => {
      cy.visit("/pacientes"); // Acessa a página de listagem de pacientes
    });
  
    it("Deve cadastrar um novo paciente corretamente", () => {
      cy.contains("Adicionar Paciente").click(); // Clica no botão para adicionar paciente
  
      // Definição de dados únicos para o teste
      const nomePaciente = "Teste Cypress " + Date.now(); // Gera um nome único
      const idadePaciente = "25";
      const alturaPaciente = "2.00";
      const pesoPaciente = "75";
      const dietaEscolhida = "Dieta Cetogênica"; // Certifique-se de que existe essa dieta no banco
  
      // Preenche os campos do formulário
      cy.get('input[name="nome"]').type(nomePaciente);
      cy.get('input[name="idade"]').type(idadePaciente);
      cy.get('input[name="altura"]').type(alturaPaciente);
      cy.get('input[name="peso"]').type(pesoPaciente);
      cy.get('select[name="dieta_id"]').select(dietaEscolhida); // Seleciona uma dieta específica
  
      // Submete o formulário
      cy.contains("Salvar").click();
  
      // Validação aprimorada: Encontra a linha específica do novo paciente
      cy.get("table tbody tr").last().within(() => {
        cy.contains(nomePaciente).should("be.visible");
        cy.contains(idadePaciente).should("be.visible");
        cy.contains(alturaPaciente).should("be.visible");
        cy.contains(pesoPaciente).should("be.visible");
        cy.contains(dietaEscolhida).should("be.visible");
      });
    });
  });
  