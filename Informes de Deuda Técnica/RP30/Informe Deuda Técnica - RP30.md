# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `Board`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `Board` maneja múltiples responsabilidades, incluyendo la gestión del tablero, la verificación de estados de victoria y la generación de alternativas. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `winPossibilities`: Este método realiza múltiples operaciones de configuración y debería dividirse en métodos más pequeños y manejables.

##### Dispensables

- **Comentarios y código redundante (+3):**
  - Hay fragmentos de código redundante, especialmente en la creación de las posibilidades de victoria, que podrían eliminarse para mejorar la claridad del código.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Board` viola este principio al manejar tanto la estructura del tablero como la lógica del juego. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Builder (+20):**
  - Podría usarse para construir instancias de `Board` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Builder para la creación de objetos `Board` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura del tablero, permitiendo tratar tanto a las celdas individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura del tablero de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los diferentes algoritmos de verificación de estados y generación de alternativas, permitiendo cambiar fácilmente la estrategia de inicialización.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de verificación y generación de alternativas y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 3 + 2) + 30 + (20 + 25 + 30) = 121
\]

La clase `Board` presenta varios malos olores de código, como métodos largos y código redundante. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 121 puntos.

### Clase Analizada: `Game`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `Game` maneja múltiples responsabilidades, incluyendo la gestión del árbol del tablero, la lógica del juego, y la implementación del algoritmo minimax. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `generateMinimax`: Este método realiza múltiples operaciones de generación y evaluación de tableros, haciéndolo largo y difícil de mantener.
  - `minimax`: Similar al método anterior, maneja múltiples responsabilidades y debería ser dividido en métodos más pequeños.

##### Dispensables

- **Comentarios y código redundante (+2):**
  - Hay fragmentos de código que podrían ser refactorizados para mejorar la claridad del código, como la repetición de búsqueda de árboles y la evaluación de utilidades.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Game` viola este principio al manejar tanto la lógica del juego como el algoritmo minimax y la gestión del árbol de tableros. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Builder (+20):**
  - Podría usarse para construir instancias de `Game` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Builder para la creación de objetos `Game` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura del árbol de tableros, permitiendo tratar tanto a los nodos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura del árbol de tableros de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los diferentes algoritmos de generación de alternativas y evaluación de utilidades, permitiendo cambiar fácilmente la estrategia de inicialización.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de generación de alternativas y evaluación de utilidades y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 2 + 2) + 30 + (20 + 25 + 30) = 120
\]

La clase `Game` presenta varios malos olores de código, como métodos largos y código redundante. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 120 puntos.

### Clase Analizada: `PlayboardController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `PlayboardController` maneja múltiples responsabilidades, incluyendo la lógica del juego, la interfaz de usuario, y la gestión de eventos. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `insert`: Este método realiza múltiples operaciones de inserción de caracteres, actualización de turnos, y evaluación de resultados, haciéndolo largo y difícil de mantener.
  - `pcInsert`: Similar al método anterior, maneja múltiples responsabilidades y debería ser dividido en métodos más pequeños.

##### Dispensables

- **Código duplicado (+4):**
  - Los métodos `insertCharOnLabel` y los eventos de clic para los distintos botones de las celdas tienen código repetido para actualizar el estado de las celdas del tablero.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `PlayboardController` viola este principio al manejar tanto la lógica del juego como la interfaz de usuario y la gestión de eventos. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Builder (+20):**
  - Podría usarse para construir instancias de `PlayboardController` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Builder para la creación de objetos `PlayboardController` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura del tablero, permitiendo tratar tanto a las celdas individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura del tablero de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de juego, como la inserción de caracteres y la evaluación de resultados, permitiendo cambiar fácilmente la estrategia de juego.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de juego y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + 30 + (20 + 25 + 30) = 122
\]

La clase `PlayboardController` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 122 puntos.

### Clase Analizada: `SettingGameModeController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `SettingGameModeController` maneja múltiples responsabilidades, incluyendo la lógica de selección de modos de juego y la navegación entre menús. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `PVP`, `PVE`, y `PCvsPC`: Estos métodos realizan múltiples operaciones, incluyendo la configuración del modo de juego y la actualización del estado de los jugadores. Deberían ser divididos en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - Los métodos `PVP`, `PVE`, y `PCvsPC` tienen estructuras similares y repiten código para habilitar o deshabilitar el botón `btSettingChar` y configurar el estado de los jugadores.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase utiliza métodos *getter* y *setter* para acceder a los modos de juego y a los estados de los jugadores, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `SettingGameModeController` viola este principio al manejar tanto la lógica de selección de modos de juego como la navegación entre menús. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de `SettingGameModeController` con diferentes configuraciones de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de objetos `SettingGameModeController` con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los menús y botones, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los menús y botones de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de configuración de modos de juego, permitiendo cambiar fácilmente la configuración del juego.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de configuración de modos de juego y permitir cambiar la configuración fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + 30 + (20 + 25 + 30) = 122
\]

La clase `SettingGameModeController` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 122 puntos.

Este repositorio fue obtenido de: https://github.com/josamaci/Proyecto_segunda_evaluacion_grupo_9
