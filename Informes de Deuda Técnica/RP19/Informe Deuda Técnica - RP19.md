# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `ArbolFiles`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `ArbolFiles` maneja múltiples responsabilidades, incluyendo la gestión de archivos y directorios, el cálculo del peso de archivos, y la organización de nodos hijos en un PriorityQueue. Debería dividirse en clases más pequeñas y especializadas.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `ArbolFiles` viola este principio al manejar tanto la estructura de archivos como la lógica de cálculo de peso y la gestión de nodos hijos. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Sustitución de Liskov (LSP) (+15):**
  - La implementación de `Comparator` en la `PriorityQueue` depende directamente del método `App.contarPeso`, lo que puede causar problemas si la implementación de `contarPeso` cambia. Debería usar una abstracción en lugar de una implementación concreta.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de objetos `ArbolFiles`, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de objetos `ArbolFiles`.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de archivos y directorios de manera más uniforme y flexible.

    **Consejo:** Implementar un patrón Composite para manejar la estructura de archivos y directorios.

#### De comportamiento

- **Iterator (+30):**
  - Podría utilizarse para proporcionar una forma de acceder secuencialmente a los elementos del árbol de archivos sin exponer su representación subyacente.

    **Consejo:** Utilizar el patrón Iterator para acceder secuencialmente a los elementos del árbol de archivos.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(6, 2, 0) = (6 + 2 + 4) + (30 + 15) + (20 + 25 + 30) = 132
\]

La clase `ArbolFiles` presenta varios malos olores de código, como clase grande y abuso de getters y setters. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Sustitución de Liskov (LSP). El esfuerzo estimado para refactorizar esta clase es de 132 puntos.

### Clase Analizada: `App`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `App` maneja múltiples responsabilidades, incluyendo la inicialización de la aplicación, la carga de escenas FXML y el cálculo del tamaño de archivos. Debería dividirse en clases más pequeñas y especializadas.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

- **Código duplicado (+4):**
  - El método `contarPeso` podría beneficiarse de la eliminación de código duplicado y la simplificación de la lógica.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene métodos estáticos como `contarPeso` y `setRoot` que no siguen un diseño orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `App` viola este principio al manejar tanto la lógica de la interfaz gráfica como la lógica de cálculo de archivos. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+15):**
  - La clase depende directamente de implementaciones concretas, como `File` y `FXMLLoader`, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de escenas y cargar archivos FXML, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de escenas y cargar archivos FXML.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de archivos y directorios de manera más uniforme y flexible.

    **Consejo:** Implementar un patrón Composite para manejar la estructura de archivos y directorios.

#### De comportamiento

- **Iterator (+30):**
  - Podría utilizarse para proporcionar una forma de acceder secuencialmente a los elementos de los directorios sin exponer su representación subyacente.

    **Consejo:** Utilizar el patrón Iterator para acceder secuencialmente a los elementos de los directorios.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(6, 2, 0) = (6 + 2 + 4) + (30 + 15) + (20 + 25 + 30) = 132
\]

La clase `App` presenta varios malos olores de código, como clase grande y abuso de getters y setters. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 132 puntos.

### Clase Analizada: `PrimaryController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `PrimaryController` maneja múltiples responsabilidades, incluyendo la interfaz gráfica, el manejo de archivos y la lógica de negocio. Debería dividirse en clases más pequeñas y especializadas.

##### Dispensables

- **Comentarios (+2):**
  - Existen pocos comentarios explicativos en la clase, lo que dificulta la comprensión del código.

- **Código duplicado (+4):**
  - Hay varios métodos que contienen lógica repetitiva que podría ser refactorizada en métodos reutilizables.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene varios métodos que manipulan directamente los componentes gráficos y los archivos, lo que no sigue un diseño orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `PrimaryController` viola este principio al manejar tanto la lógica de la interfaz gráfica como la lógica de manejo de archivos. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+15):**
  - La clase depende directamente de implementaciones concretas, como `File`, `Desktop`, `Rectangle` y `Color`, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de los elementos gráficos, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de elementos gráficos.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los archivos y directorios de manera más uniforme y flexible.

    **Consejo:** Implementar un patrón Composite para manejar la estructura de archivos y directorios.

#### De comportamiento

- **Iterator (+30):**
  - Podría utilizarse para proporcionar una forma de acceder secuencialmente a los elementos de los directorios sin exponer su representación subyacente.

    **Consejo:** Utilizar el patrón Iterator para acceder secuencialmente a los elementos de los directorios.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(6, 2, 0) = (6 + 2 + 4) + (30 + 15) + (20 + 25 + 30) = 132
\]

La clase `PrimaryController` presenta varios malos olores de código, como clase grande y abuso de getters y setters. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 132 puntos.


Este repositorio fue obtenido de: https://github.com/AxcelVillagran/ProyectoEDD2
