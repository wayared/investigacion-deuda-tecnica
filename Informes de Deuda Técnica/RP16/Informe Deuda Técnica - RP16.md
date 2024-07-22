# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `PrimaryyController`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - `initialize`: Este método realiza múltiples tareas, como la configuración inicial de los elementos de la interfaz y la carga del árbol binario, lo que lo hace extenso y difícil de mantener.
  - `putQuestionNodes`: Este método es largo y complejo, ya que se encarga de leer datos desde un archivo y construir un árbol binario de manera iterativa.

##### Dispensables

- **Código duplicado (+7):**
  - Hay varias instancias donde se repite la lógica para establecer eventos y manejar nodos del árbol, como en los métodos `nOpciones` y `Display`.

- **Código muerto (+3):**
  - Existen comentarios de código y fragmentos de código comentados que no se utilizan y deberían ser eliminados para mejorar la legibilidad.

##### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `PrimaryyController` tiene múltiples responsabilidades, como la gestión de eventos de la interfaz de usuario, la lógica de negocio del juego de preguntas y respuestas, y la manipulación del árbol binario. Esto implica que cualquier cambio en una de estas áreas podría afectar a las otras, haciendo el código difícil de mantener.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - Aunque no se usan directamente sentencias `switch`, la clase utiliza múltiples condicionales (`if-else`) en métodos como `nOpciones` y `Display` para manejar diferentes respuestas y rutas en el árbol. Esto podría ser mejorado usando el patrón de diseño Estrategia.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - La clase `PrimaryyController` accede frecuentemente a métodos y variables privadas de otras clases, como `BinaryTree` y `DataManager`, lo que aumenta el acoplamiento y dificulta el mantenimiento.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `PrimaryyController` viola este principio al tener múltiples responsabilidades. Maneja la interfaz de usuario, la lógica de juego, y la manipulación de datos, lo que debería estar separado en diferentes clases.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `PrimaryyController` depende directamente de implementaciones concretas como `BinaryTree` y `DataManager` en lugar de abstracciones. Debería depender de interfaces o clases abstractas para reducir el acoplamiento y aumentar la flexibilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de nodos del árbol binario. Esto puede reducir la complejidad y mejorar la flexibilidad del código.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas. Esto sería útil para adaptar diferentes estructuras de datos a la lógica de la interfaz de usuario.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en el subsistema del árbol binario y la gestión de datos.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para manejar las respuestas del usuario en el árbol binario, reduciendo el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes de usuario como objetos, lo que permite parametrizar clientes con colas y solicitudes.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Esto sería útil para manejar diferentes tipos de respuestas y rutas en el árbol binario.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 0) = (5 + 7 + 3 + 6 + 6) + (30 + 45) + 0 = 102
\]

La clase `PrimaryyController` presenta varios malos olores de código, como métodos largos, código duplicado y acoplamiento inapropiado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 102 puntos.

### Clase Analizada: `DataManager`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `DataManager` tiene múltiples responsabilidades, incluyendo la carga de atributos, la carga de respuestas de animales, y la gestión de datos. Esta clase podría dividirse en varias clases más pequeñas para mejorar su mantenibilidad.

- **Método Largo (+5):**
  - `loadAnimalsResponses`: Este método realiza múltiples tareas, como leer líneas de un archivo y dividirlas en atributos y valores, lo que lo hace largo y complejo.

##### Obsesión Primitiva (+3):**
  - Uso de tipos primitivos (`String`, `List<String>`) para representar datos complejos. Esto se observa en la carga de atributos y valores de animales, donde se podrían usar clases más específicas para encapsular estos datos.

##### Dispensables

- **Comentarios (+2):**
  - Existen muchos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

##### Acopladores

- **Envidia de características (+5):**
  - La clase `DataManager` utiliza intensivamente métodos de la clase `Scanner`, lo que podría indicar que parte de esta lógica debería estar en una clase separada para manejar la lectura de archivos.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `DataManager` tiene múltiples razones para cambiar, ya sea por cambios en el formato de los datos de entrada o por cambios en la lógica de carga de datos.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `DataManager` viola este principio al tener múltiples responsabilidades. Maneja la carga de datos desde archivos, la organización de estos datos en estructuras, y la gestión de atributos y valores. Esto debería estar separado en diferentes clases.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `DataManager` depende directamente de implementaciones concretas como `Scanner` y `File`, en lugar de depender de abstracciones. Esto limita la flexibilidad y dificulta el mantenimiento y las pruebas.

### Patrones de diseño no utilizados

#### Creacionales

- **Constructor (+25):**
  - Consejo: Usa un Constructor para encapsular la creación de instancias de `DataManager`, lo que puede ayudar a establecer una configuración inicial más clara y a reducir la complejidad del constructor actual.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que diferentes tipos de fuentes de datos (por ejemplo, archivos, bases de datos) trabajen con la clase `DataManager`.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada para la carga y gestión de datos, encapsulando la complejidad interna.

#### De comportamiento

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos de carga de datos, encapsular cada uno, y hacerlos intercambiables. Esto sería útil para manejar diferentes formatos de datos.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 0) = (6 + 5 + 3 + 2 + 5 + 6) + (30 + 45) + 0 = 102
\]

La clase `DataManager` presenta varios malos olores de código, como métodos largos, obsesión primitiva, y acoplamiento inapropiado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 102 puntos.

### Clase Analizada: `BinaryTree`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `BinaryTree` maneja múltiples responsabilidades, incluyendo la gestión de nodos de árbol, el recorrido del árbol y la manipulación de niveles. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `preOrderTraversalRecursive`: Este método realiza múltiples operaciones de recorrido, haciéndolo largo y difícil de mantener.
  - `breadthTraversal`: Este método también es largo y maneja varias operaciones, lo que complica su comprensión.

##### Dispensables

- **Comentarios (+2):**
  - Existen comentarios que podrían ser eliminados si el código fuera más claro y autoexplicativo.

- **Código duplicado (+7):**
  - Hay métodos redundantes como `showLeaf` y `showLeaft` que podrían ser refactorizados en un solo método para evitar duplicación.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `BinaryTree` viola este principio al manejar tanto la estructura del árbol como las operaciones de recorrido y manipulación. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase depende directamente de implementaciones concretas, como `LinkedList`, `Queue` y `Stack`, en lugar de depender de abstracciones. Esto limita la flexibilidad y la posibilidad de reutilización del código.

### Patrones de diseño no utilizados

#### Creacionales

- **Constructor (+25):**
  - Consejo: Usa un Constructor que inicialice todos los elementos necesarios del árbol binario, lo que puede simplificar la creación de instancias y asegurar que el objeto se encuentre en un estado consistente.

#### Estructurales

- **Composite (+30):**
  - Consejo: Implementa el patrón Composite para manejar la estructura del árbol binario. Esto permitiría tratar tanto a los nodos individuales como a las estructuras compuestas de manera uniforme.

#### De comportamiento

- **Iterator (+15):**
  - Consejo: Usa el patrón Iterator para proporcionar una forma de acceder secuencialmente a los elementos del árbol sin exponer su representación subyacente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(5, 2, 0) = (6 + 5 + 2 + 7 + 4) + (30 + 45) + 0 = 99
\]

La clase `BinaryTree` presenta varios malos olores de código, como métodos largos, código duplicado y abuso de getters y setters. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 99 puntos.



Este repositorio fue obtenido de: https://github.com/katumbac/Proyecto06_ED_P2
