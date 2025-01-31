const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://127.0.0.1:5000", // URL base do Flask
    supportFile: false,
    
    setupNodeEvents(on, config) {
      // Implementação de event listeners do Cypress, se necessário
    }
  }
});
