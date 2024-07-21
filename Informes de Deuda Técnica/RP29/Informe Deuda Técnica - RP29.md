# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `GameManager`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `GameManager` maneja múltiples responsabilidades, incluyendo la gestión de turnos, la validación del estado del juego, la configuración de la UI y la selección de jugadores. Debería dividirse en clases más pequeñas y especializadas.

##### Dispensables

- **Comentarios (+2):**
  - Hay pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `GameManager` viola este principio al manejar tanto la lógica del juego como la lógica de la interfaz gráfica. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+25):**
  - La clase depende directamente de implementaciones concretas, como `GridButton`, `GameControls`, y otros componentes específicos, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de los botones de la cuadrícula y otros elementos de la interfaz de usuario, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de elementos gráficos y controladores.

#### Estructurales

- **Facade (+25):**
  - Podría implementarse para simplificar la interacción entre la interfaz de usuario y la lógica del juego.

    **Consejo:** Implementar un patrón Facade para simplificar y unificar la interacción entre la interfaz de usuario y la lógica del juego.

#### De comportamiento

- **Observer (+30):**
  - Podría utilizarse para notificar a otros componentes sobre cambios en el estado del juego, como el cambio de turnos o la detección de un ganador.

    **Consejo:** Utilizar el patrón Observer para notificar a otros componentes sobre cambios en el estado del juego.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 0) = (6 + 2 + 2) + (30 + 25) + (20 + 25 + 30) = 140
\]

La clase `GameManager` presenta varios malos olores de código, como clase grande y métodos getter y setter sin lógica adicional. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 140 puntos.

### Clase Analizada: `Table`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `Table` maneja múltiples responsabilidades, incluyendo la gestión de la tabla del juego, la evaluación de la utilidad y la inserción de valores. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `generateUtility`: Este método realiza múltiples operaciones de cálculo de utilidad, haciéndolo largo y difícil de mantener.

##### Dispensables

- **Código duplicado (+5):**
  - Métodos como `utilityByRows`, `utilityByColumns` y `utilityByDiagonals` tienen lógica similar que podría ser refactorizada para eliminar duplicación.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Table` viola este principio al manejar tanto la estructura de la tabla como la lógica de utilidad. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Builder (+20):**
  - Podría usarse para construir instancias de `Table` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Builder para la creación de objetos `Table` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de la tabla del juego, permitiendo tratar tanto a los nodos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de la tabla del juego de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los diferentes algoritmos de cálculo de utilidad, permitiendo cambiar fácilmente la estrategia de evaluación.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de cálculo de utilidad y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 5 + 2) + 30 + (20 + 25 + 30) = 123
\]

La clase `Table` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 123 puntos.

### Clase Analizada: `GameViewController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `GameViewController` maneja múltiples responsabilidades, incluyendo la inicialización de la interfaz de usuario, la lógica del juego y la gestión de eventos. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `initialize`: Este método realiza múltiples operaciones de configuración y debería dividirse en métodos más pequeños y manejables.

##### Dispensables

- **Comentarios y código redundante (+3):**
  - Hay fragmentos de código comentados y redundantes que podrían eliminarse para mejorar la claridad del código.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `GameViewController` viola este principio al manejar tanto la interfaz de usuario como la lógica del juego. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Builder (+20):**
  - Podría usarse para construir instancias de `GameViewController` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Builder para la creación de objetos `GameViewController` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de la interfaz de usuario, permitiendo tratar tanto a los nodos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de la interfaz de usuario de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los diferentes algoritmos de inicialización y configuración, permitiendo cambiar fácilmente la estrategia de inicialización.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de inicialización y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 3 + 2) + 30 + (20 + 25 + 30) = 121
\]

La clase `GameViewController` presenta varios malos olores de código, como métodos largos y código redundante. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 121 puntos.

### Clase Analizada: `MainViewController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `MainViewController` maneja múltiples responsabilidades, incluyendo la inicialización de la interfaz de usuario, la gestión de eventos de juego y la configuración de símbolos. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `ComenzarJuego`: Este método realiza múltiples operaciones de configuración y debería dividirse en métodos más pequeños y manejables.

##### Dispensables

- **Comentarios y código redundante (+3):**
  - Hay fragmentos de código redundante que podrían eliminarse para mejorar la claridad del código.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `MainViewController` viola este principio al manejar tanto la interfaz de usuario como la lógica del juego. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Builder (+20):**
  - Podría usarse para construir instancias de `MainViewController` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Builder para la creación de objetos `MainViewController` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de la interfaz de usuario, permitiendo tratar tanto a los nodos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de la interfaz de usuario de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los diferentes algoritmos de inicialización y configuración, permitiendo cambiar fácilmente la estrategia de inicialización.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de inicialización y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 3 + 2) + 30 + (20 + 25 + 30) = 121
\]

La clase `MainViewController` presenta varios malos olores de código, como métodos largos y código redundante. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 121 puntos.

Este repositorio fue obtenido de: https://github.com/Neoterux/Proyecto_EDD_2P
