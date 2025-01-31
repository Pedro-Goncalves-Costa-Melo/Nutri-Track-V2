describe("Teste de Visualização do Dashboard", () => {

    beforeEach(() => {
      cy.visit("/dashboard");
    });
  
    it("Deve carregar os cards de informações corretamente", () => {
      cy.contains("Total de Pacientes").should("be.visible");
      cy.contains("Total de Dietas").should("be.visible");
      cy.contains("Média de Idade").should("be.visible");
      cy.contains("Média de Altura").should("be.visible");
      cy.contains("Média de Peso").should("be.visible");
    });
  
    it("Deve carregar a lista de pacientes corretamente", () => {
      cy.get("table").should("be.visible"); // Garante que a tabela existe
  
      // Verifica se pelo menos uma linha de paciente foi carregada corretamente
      cy.get("tbody tr").its("length").should("be.greaterThan", 0);
    });
  
    it("Deve carregar e exibir o gráfico de distribuição de dietas", () => {
      cy.get("#graficoDietas").should("be.visible"); // Confirma que o elemento existe
  
      // Verifica se o gráfico foi renderizado com labels corretos (assumindo que temos dietas cadastradas)
      cy.window().then((win) => {
        const chart = win.Chart.instances[0]; // Obtendo a instância do gráfico do Chart.js
        expect(chart.data.labels.length).to.be.greaterThan(0); // Deve ter pelo menos uma dieta listada
      });
    });
  
  });
  