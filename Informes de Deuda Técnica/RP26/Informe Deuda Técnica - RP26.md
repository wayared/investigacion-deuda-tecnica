
# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `Tablero`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `Tablero` maneja múltiples responsabilidades, incluyendo la lógica del juego, la actualización de la interfaz gráfica y la gestión de utilidades del juego. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `createTree`: Este método realiza múltiples operaciones complejas y podría beneficiarse de ser dividido en métodos más pequeños y manejables.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

- **Código duplicado (+4):**
  - Hay lógica repetida en métodos como `comprobarFilas`, `comprobarColumnas` y `comprobarDiagonales` que podrían ser refactorizados en métodos reutilizables.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Tablero` viola este principio al manejar tanto la lógica del juego como la lógica de la interfaz gráfica. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+15):**
  - La clase depende directamente de implementaciones concretas, como `GridPane`, `ImageView` y `ObservableList`, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de los elementos gráficos, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de elementos gráficos.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura del tablero de manera más uniforme y flexible.

    **Consejo:** Implementar un patrón Composite para manejar la estructura del tablero.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los algoritmos de cálculo de utilidades y elección de mejores celdas.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de cálculo de utilidades y elección de mejores celdas.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(6, 2, 0) = (6 + 5 + 2 + 4) + (30 + 15) + (20 + 25 + 30) = 137
\]

La clase `Tablero` presenta varios malos olores de código, como clase grande y métodos largos. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 137 puntos.


### Clase Analizada: `TableroPCVPC`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `TableroPCVPC` maneja múltiples responsabilidades, incluyendo la lógica del juego, la actualización de la interfaz gráfica y la gestión de utilidades del juego. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `createTree`: Este método realiza múltiples operaciones complejas y podría beneficiarse de ser dividido en métodos más pequeños y manejables.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

- **Código duplicado (+4):**
  - Hay lógica repetida en métodos como `comprobarFilas`, `comprobarColumnas` y `comprobarDiagonales` que podrían ser refactorizados en métodos reutilizables.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `TableroPCVPC` viola este principio al manejar tanto la lógica del juego como la lógica de la interfaz gráfica. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+15):**
  - La clase depende directamente de implementaciones concretas, como `GridPane`, `ImageView` y `ObservableList`, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de los elementos gráficos, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de elementos gráficos.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura del tablero de manera más uniforme y flexible.

    **Consejo:** Implementar un patrón Composite para manejar la estructura del tablero.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular los algoritmos de cálculo de utilidades y elección de mejores celdas.

    **Consejo:** Utilizar el patrón Strategy para encapsular los algoritmos de cálculo de utilidades y elección de mejores celdas.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(6, 2, 0) = (6 + 5 + 2 + 4) + (30 + 15) + (20 + 25 + 30) = 137
\]

La clase `TableroPCVPC` presenta varios malos olores de código, como clase grande y métodos largos. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 137 puntos.

### Clase Analizada: `MenuController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `MenuController` maneja múltiples responsabilidades, incluyendo la gestión de la interfaz gráfica, la inicialización del juego en diferentes modos, y la selección de figuras y jugadores. Debería dividirse en clases más pequeñas y especializadas.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

- **Código muerto (+3):**
  - El método `changeStyle` contiene líneas de código comentadas que no están en uso.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `MenuController` viola este principio al manejar tanto la lógica del juego como la lógica de la interfaz gráfica. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+15):**
  - La clase depende directamente de implementaciones concretas, como `Pane`, `ImageView`, `FXMLLoader`, `Alert`, y `util`, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de los elementos gráficos y los controladores de los diferentes modos de juego, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de elementos gráficos y controladores.

#### Estructurales

- **Facade (+25):**
  - Podría implementarse para simplificar la interacción entre la interfaz de usuario y la lógica del juego.

    **Consejo:** Implementar un patrón Facade para simplificar y unificar la interacción entre la interfaz de usuario y la lógica del juego.

#### De comportamiento

- **Command (+30):**
  - Podría utilizarse para encapsular todas las acciones que los usuarios pueden realizar en la interfaz gráfica, como la selección de figuras y jugadores, y el cambio de estilo.

    **Consejo:** Utilizar el patrón Command para encapsular las acciones del usuario.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 0) = (6 + 2 + 3 + 2) + (30 + 15) + (20 + 25 + 30) = 133
\]

La clase `MenuController` presenta varios malos olores de código, como clase grande y código muerto. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 133 puntos.

### Clase Analizada: `ResultadoController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `ResultadoController` maneja múltiples responsabilidades, incluyendo la actualización de la interfaz gráfica del resultado del juego, la determinación del ganador y la configuración de líneas de victoria. Debería dividirse en clases más pequeñas y especializadas.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `ResultadoController` viola este principio al manejar tanto la lógica del juego como la lógica de la interfaz gráfica. Debería dividirse en diferentes clases con responsabilidades únicas.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de los elementos gráficos y los controladores de los diferentes modos de juego, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de elementos gráficos y controladores.

#### Estructurales

- **Facade (+25):**
  - Podría implementarse para simplificar la interacción entre la interfaz de usuario y la lógica del juego.

    **Consejo:** Implementar un patrón Facade para simplificar y unificar la interacción entre la interfaz de usuario y la lógica del juego.

#### De comportamiento

- **Command (+30):**
  - Podría utilizarse para encapsular todas las acciones que los usuarios pueden realizar en la interfaz gráfica, como la selección de figuras y jugadores, y el cambio de estilo.

    **Consejo:** Utilizar el patrón Command para encapsular las acciones del usuario.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 0) = (6 + 2 + 2) + (30) + (20 + 25 + 30) = 115
\]

La clase `ResultadoController` presenta varios malos olores de código, como clase grande y métodos getter y setter sin lógica adicional. También viola el Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 115 puntos.

Este repositorio fue obtenido de: https://github.com/BurneoDanny/Grupo_07
