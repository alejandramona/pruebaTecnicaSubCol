Feature: Prueba de login en la API de autenticación
  Scenario: Login exitoso
    Given que tengo datos de login válidos
    When envío una solicitud de login con esos datos
    Then debería recibir una respuesta indicando "success"

  Scenario: Login fallido
    Given que tengo datos de login inválidos
    When envío una solicitud de login con esos datos
    Then debería recibir una respuesta indicando "failure"
