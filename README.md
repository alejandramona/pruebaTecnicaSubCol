# Prueba Técnica 1: Desarrollo de un Script de Automatización en Python

Este proyecto automatiza pruebas de login usando el patrón Screenplay y Gherkin con Py.
Requisitos
# Para ejecutar este proyecto, se deben instalar los siguientes requisitos:

1. **Python** 3.6 o superior.
2. **requests:** Para realizar las solicitudes HTTP.
3. **unittest:** Para ejecutar las pruebas automatizadas.

## Enfoque utilizado

El enfoque utilizado en este proyecto se basa en el patrón de diseño **Screenplay**, que se utiliza ampliamente en la automatización de pruebas de interfaz de usuario y servicios web. El patrón Screenplay ayuda a estructurar las pruebas de una manera que sea fácil de entender y mantener, enfocándose en los **actores**, **habilidades** y **tareas** que componen la interacción con la aplicación.

### Componentes clave:
1. **Actor:** Representa al usuario o sistema que interactúa con el sistema de pruebas.
2. **Tareas:** Son las acciones que el Actor realiza en la aplicación, como hacer login, buscar elementos, etc.
3. **Habilidades:** Son las capacidades del Actor para interactuar con el sistema, como leer datos o realizar una petición HTTP.
4. **Interacciones:** Las interacciones entre el Actor y los componentes del sistema de prueba.

En este caso, el Actor realiza tareas como **iniciar sesión** en el sistema utilizando un servicio web que recibe credenciales como entrada. Utilizamos solicitudes HTTP para enviar datos y validar las respuestas.

### Estructura del Proyecto

La estructura del proyecto está organizada en varios módulos que implementan diferentes partes del patrón Screenplay. A continuación se muestra la estructura:


### Archivos principales:
1. **login.feature (en `features`)**: Este archivo contiene los escenarios de prueba escritos en el lenguaje Gherkin. Gherkin es un lenguaje basado en texto simple utilizado para definir escenarios de prueba en formato legible por humanos.
   ```gherkin
   Feature: Prueba de login en la API de autenticación
    Scenario: Login exitoso
    Given que tengo datos de login válidos
    When envío una solicitud de login con esos datos
    Then debería recibir una respuesta indicando "success"

    Scenario: Login fallido
    Given que tengo datos de login inválidos
    When envío una solicitud de login con esos datos
    Then debería recibir una respuesta indicando "failure"
## Investigación 
A modo de investigación, analicé el uso de Screenplay para Python porque solo lo había trabajado con Selenium y Robot Framework, para ver si la estructura era igual a Java, y es demasiado similar, solo que el enfoque en Java es mucho más sencillo.
## Ejecución
Para ejecutar las pruebas, usa:
```bash
python -m unittest tests/login_test.py

