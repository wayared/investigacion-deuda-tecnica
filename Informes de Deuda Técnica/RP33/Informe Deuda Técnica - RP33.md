# Informe de Análisis de Deuda Técnica

## Clase Analizada: `Animal`

### Identificación de Olores de Código

#### Acaparadores
**Método Largo (+5)**
- Los métodos `cargarAnimales` y `cargarAnimales2` contienen más de 20 líneas, dificultando su lectura y comprensión.

**Clase Grande (+6)**
- La clase `Animal` maneja múltiples responsabilidades, como la gestión de datos de animales y la carga de archivos.

#### Dispensables
**Comentarios (+2)**
- No hay comentarios innecesarios. La clase está suficientemente documentada.

### Violaciones de los Principios SOLID
**Principio de Responsabilidad Única (SRP) (+30)**
- La clase `Animal` tiene múltiples responsabilidades, como gestionar la información de los animales y cargar datos desde archivos.

**Principio Abierto/Cerrado (OCP) (+40)**
- La clase podría ser extendida sin modificar su código actual en algunos casos, pero en otros no, debido a la mezcla de lógica de diferentes responsabilidades.

### Patrones de diseño no utilizados

#### Estructurales
**Fachada (+20)**
- Podría proporcionar una interfaz simplificada para la carga y gestión de animales.

#### De comportamiento
**Comando (+20)**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de gestión de datos.

**Mediador (+30)**
- Podría reducir las dependencias caóticas entre objetos de la clase `Animal`.

**Estrategia (+20)**
- Podría definir una familia de algoritmos de carga de datos, encapsular cada uno, y hacerlos intercambiables en `Animal`.

**Método Plantilla (+25)**
- Podría definir el esqueleto de un algoritmo de carga de datos en una operación, dejando algunos pasos a las subclases.


### Clase Analizada: `Partida`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo (+5):** 
  - `empezarJuego()`, `empezarJuego2()`, y `generarArbolJuego()` tienen más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6):** 
  - La clase `Partida` tiene múltiples responsabilidades, como gestionar la lógica del juego, manipular archivos y manejar la interfaz de usuario.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos complejos, como las preguntas, respuestas y detalles del juego.

- **Lista de Parámetros Largos (+4):** 
  - El método `addAnimalToTxt(String animal, Queue<String> respuestas)` tiene una lista de parámetros larga.

**Abusadores de Orientación a Objetos**

- **Sentencias Switch (+5):** 
  - El método `empezarJuego()` y `empezarJuego2()` utilizan sentencias condicionales para manejar las respuestas del usuario.

**Preventores de Cambio**

- **Cambio divergente (+6):** 
  - La clase `Partida` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica del juego o actualizar el manejo de archivos.

- **Cirugía de escopeta (+8):** 
  - Cambios pequeños en la lógica del juego requieren modificaciones en múltiples métodos y clases relacionadas.

**Dispensables**

- **Comentarios (+2):**
  - Existen muchos comentarios en los métodos `empezarJuego()`, `empezarJuego2()`, y `generarArbolJuego()` que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):** 
  - El código para manejar las respuestas del usuario se repite en varios lugares de la clase `Partida`.

- **Código muerto (+3):** 
  - Existen métodos y variables no utilizados, como los comentados al inicio de la clase.

**Acopladores**

- **Envidia de características (+5):** 
  - Los métodos `empezarJuego()` y `empezarJuego2()` utilizan intensivamente métodos de la clase `BinaryTree`.

- **Intimidad inapropiada (+6):**
  - La clase `Partida` accede frecuentemente a métodos y variables privadas de la clase `BinaryTree`.

- **Cadenas de mensajes (+7):**
  - Los métodos `empezarJuego()` y `empezarJuego2()` realizan varias llamadas en cadena a métodos de la clase `BinaryTree`.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Partida` tiene múltiples responsabilidades, como gestionar la lógica del juego, manipular archivos y manejar la interfaz de usuario.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `Partida` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `empezarJuego()` y `empezarJuego2()`.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `Partida` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica del juego.

#### Patrones de diseño no utilizados

**Creacionales**

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes tipos de árboles binarios sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `Partida`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de árboles binarios y reducir la complejidad en `Partida`.

**Estructurales**

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de archivos.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de preguntas y respuestas.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de preguntas y respuestas de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión del juego.

**De comportamiento**

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de respuesta del usuario, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de juego.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de preguntas sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `Partida`.

- **Observador (+25):**
  - Podría permitir que un objeto `Partida` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `Partida` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de juego, encapsular cada uno, y hacerlos intercambiables en `Partida`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de juego en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
   - Podría separar un algoritmo de juego de la estructura de objeto `BinaryTree` sobre la que opera. 
  
### Clase Analizada: `Utilidades`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo (+5):** 
  - `crearBinaryTreePreguntas(Stack<BinaryTree<String>> piloPreguntas)` tiene más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6):** 
  - La clase `Utilidades` tiene múltiples responsabilidades, como construir pilas de preguntas, crear árboles binarios, manipular archivos y gestionar respuestas.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos complejos, como las preguntas y respuestas del juego.

**Abusadores de Orientación a Objetos**

- **Sentencias Switch (+5):** 
  - El método `chargeAnswers(BinaryTree<String> treeQuestion, BinaryTree<String> animal, Queue<String> answers)` utiliza sentencias condicionales para manejar las respuestas del usuario.

**Preventores de Cambio**

- **Cambio divergente (+6):** 
  - La clase `Utilidades` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica del juego o actualizar el manejo de archivos.

- **Cirugía de escopeta (+8):** 
  - Cambios pequeños en la lógica del juego requieren modificaciones en múltiples métodos y clases relacionadas.

**Dispensables**

- **Comentarios (+2):**
  - Existen muchos comentarios en los métodos que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):** 
  - El código para manejar las respuestas del usuario se repite en varios lugares de la clase `Utilidades`.

- **Código muerto (+3):** 
  - Existen métodos y variables no utilizados o comentados que no se usan en la clase actual.

**Acopladores**

- **Envidia de características (+5):** 
  - Los métodos utilizan intensivamente métodos de la clase `BinaryTree` y `BufferedReader`.

- **Intimidad inapropiada (+6):**
  - La clase `Utilidades` accede frecuentemente a métodos y variables privadas de la clase `BinaryTree`.

- **Cadenas de mensajes (+7):**
  - Los métodos realizan varias llamadas en cadena a métodos de la clase `BinaryTree`.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Utilidades` tiene múltiples responsabilidades, como gestionar la lógica del juego, manipular archivos y manejar la creación de árboles binarios.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `Utilidades` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos relacionados con la creación de árboles binarios.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `Utilidades` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica del juego.

#### Patrones de diseño no utilizados

**Creacionales**

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes tipos de árboles binarios sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `Utilidades`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de árboles binarios y reducir la complejidad en `Utilidades`.

**Estructurales**

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de archivos.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de preguntas y respuestas.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de preguntas y respuestas de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión del juego.

**De comportamiento**

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de respuesta del usuario, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de juego.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de preguntas sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `Utilidades`.

- **Observador (+25):**
  - Podría permitir que un objeto `Utilidades` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `Utilidades` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de juego, encapsular cada uno, y hacerlos intercambiables en `Utilidades`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de juego en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
  - Podría separar un algoritmo de juego de la estructura de objeto `BinaryTree` sobre la que opera.


### Clase Analizada: `GanaPartidaController`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo (+5):**
  - El método `setearImageView(String ruta)` tiene más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6):**
  - La clase `GanaPartidaController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar eventos y cargar imágenes.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos complejos, como la ruta de la imagen.

**Abusadores de Orientación a Objetos**

- **Sentencias Switch (+5):**
  - No se encontraron sentencias switch en esta clase.

**Preventores de Cambio**

- **Cambio divergente (+6):**
  - La clase `GanaPartidaController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de manejo de eventos o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de manejo de eventos o en la carga de imágenes requieren modificaciones en múltiples métodos relacionados.

**Dispensables**

- **Comentarios (+2):**
  - Existen algunos comentarios que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):**
  - El código para manejar eventos de acción se repite en varios métodos (`mostrarInforme`, `jugarDeNuevo`, `salir`).

- **Código muerto (+3):**
  - No se encontró código muerto en esta clase.

**Acopladores**

- **Envidia de características (+5):**
  - Los métodos utilizan intensivamente métodos de la clase `App`.

- **Intimidad inapropiada (+6):**
  - La clase `GanaPartidaController` accede frecuentemente a métodos y variables de la clase `App`.

- **Cadenas de mensajes (+7):**
  - Los métodos realizan varias llamadas en cadena a métodos de la clase `App`.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `GanaPartidaController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar eventos y cargar imágenes.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `GanaPartidaController` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos relacionados con la carga de imágenes y manejo de eventos.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `GanaPartidaController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica del juego y la carga de imágenes.

#### Patrones de diseño no utilizados

**Creacionales**

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes tipos de controladores de interfaz sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `GanaPartidaController`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de controladores y reducir la complejidad en `GanaPartidaController`.

**Estructurales**

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la carga de imágenes.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de componentes de la interfaz de usuario.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de controladores de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión del juego.

**De comportamiento**

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de evento, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de evento.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de componentes de la interfaz sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `GanaPartidaController`.

- **Observador (+25):**
  - Podría permitir que un objeto `GanaPartidaController` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `GanaPartidaController` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de manejo de eventos, encapsular cada uno, y hacerlos intercambiables en `GanaPartidaController`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de manejo de eventos en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
  - Podría separar un algoritmo de manejo de eventos de la estructura de objeto `GanaPartidaController` sobre la que opera.


Este repositorio fue obtenido de: https://github.com/rexman10/Juego_preguntas_BDT
