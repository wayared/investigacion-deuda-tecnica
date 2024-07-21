
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `Tablero`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** utilidadTablero(fichas fAJugar, fichas fOponente) y funcionUtilidadDe(fichas fACalcular) son métodos largos y complejos. Podrían beneficiarse de ser divididos en métodos más pequeños.
- **Clase Grande (+6):** La clase Tablero tiene múltiples métodos y campos, lo que la hace relativamente grande. Considerar dividir la funcionalidad en clases más pequeñas podría mejorar la mantenibilidad.
- **Obsesión Primitiva (+3):** El uso de tipos primitivos como int y char en lugar de clases podría ser un indicador. La clase fichas podría manejar más de esta lógica.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Los métodos que copian el estado de un tablero a otro (copiarTablero, copiarUtilidad, copiarMov) podrían beneficiarse de encapsular estos grupos de datos en una clase.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** Los métodos largos y complejos indican que cambios en una parte del método podrían requerir cambios en otras partes.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):** La lógica de comprobación de utilidad y ganador podría estar duplicada.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):** La clase Tablero maneja mucha lógica que podría estar en la clase fichas.
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Tablero maneja múltiples responsabilidades: manejo del tablero, cálculo de utilidad, y comprobación de ganador.
- **Principio Abierto/Cerrado (OCP) (+40)** Añadir nuevas funcionalidades podría requerir modificar la clase Tablero.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)**
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `JuegoController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos initialize(), oponenteJuega(), arbolOponente(), y arbolJugador() son largos y realizan múltiples tareas, lo que dificulta su comprensión y mantenimiento.
- **Clase Grande (+6):** La clase JuegoController tiene una gran cantidad de métodos y campos, lo que la convierte en una clase grande con múltiples responsabilidades.
- **Obsesión Primitiva (+3):** El uso extensivo de tipos primitivos (e.g., int[][] espacios_ocupados, int[] posiciones) en lugar de clases específicas para representar estos datos.
- **Lista de Parámetros Largos (+4):** Métodos como oponenteJuega() tienen una lista de parámetros extensa, lo que complica su uso y comprensión.
- **Grupos de Datos (+3):** Los datos como espacios_ocupados, figuraJugador, figuraOponente, entre otros, están relacionados pero dispersos en la clase.
 
#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** La clase JuegoController interactúa con varias clases (Tablero, fichas, Tree, TreeComparator), y algunas de estas interacciones se podrían abstraer mejor.
- **Legado Rechazado (+6):** La clase parece tener un diseño basado en código heredado o no modernizado, reflejando una posible falta de uso de prácticas actuales de diseño.
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** Campos como figuraJugador y figuraOponente se utilizan principalmente durante el juego y podrían ser mejor encapsulados.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase JuegoController está haciendo demasiado, afectando varias áreas del juego (interfaz, lógica del juego, etc.), lo que complica los cambios.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Las modificaciones en la clase afectan múltiples aspectos del juego, reflejando una falta de separación de responsabilidades.

#### Dispensables

- **Comentarios (+2):** Los comentarios en el código son mínimos y no proporcionan información útil sobre la lógica o propósito de los métodos.
- **Código duplicado (+7):** Hay duplicación en la lógica para la gestión de tableros y fichas, especialmente en la configuración y manipulación del tablero.
- **Clase de datos (+5):** La clase JuegoController tiene campos que actúan como datos pero están mezclados con lógica, lo que podría ser manejado por clases de datos separadas.
- **Código muerto (+3):** Algunas partes del código parecen no tener un uso claro o estar en desarrollo.
- **Clase perezosa (+4):** La clase tiene responsabilidades que deberían ser delegadas a otras clases, lo que la hace perezosa y difícil de mantener.
- **Generalidad especulativa (+5):** La clase incluye lógica para casos que pueden no ser necesarios o utilizados en la aplicación actual.

#### Acopladores

- **Envidia de características (+5):** 
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase JuegoController tiene múltiples responsabilidades, incluyendo la lógica del juego, la interfaz de usuario y la manipulación de datos.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está abierta para extensiones sin modificar su código, ya que muchas funcionalidades están implementadas directamente en ella.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende de detalles concretos (por ejemplo, Tablero, fichas) en lugar de abstraerse a través de interfaces o clases abstractas.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** La creación de objetos (e.g., Tablero, fichas) podría beneficiarse de una fábrica abstracta para gestionar la instanciación.
- **Constructor (+25)** Los constructores están siendo utilizados, pero no se aprovechan patrones como el Constructor para la creación de objetos complejos.
- **Método de Fábrica (+20)** Podría ser útil para encapsular la lógica de creación de objetos relacionados, especialmente para Tablero y fichas.
- **Prototipo (+30)** La clonación de objetos, como Tablero, podría ser manejada mejor con un patrón de prototipo.
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)** La separación entre la lógica del juego y la interfaz de usuario podría beneficiarse de un patrón puente.
* **Compuesto (+30)** La manipulación de tableros y fichas podría ser más flexible con el patrón compuesto.
* **Decorador (+25)** No se utiliza un patrón decorador para añadir funcionalidades adicionales a los objetos sin modificar su estructura.
* **Fachada (+20)** Una fachada podría simplificar la interacción con la lógica del juego y la interfaz de usuario.
* **Peso Ligero (+40)** El patrón peso ligero podría ser utilizado para manejar eficientemente los objetos similares (e.g., fichas).
* **Proxy (+30)** Un proxy podría ser utilizado para controlar el acceso a los objetos Tablero o fichas.

#### De comportamiento

* **Cadena de Responsabilidad (+30)** La lógica del juego y la interfaz podrían ser gestionadas mejor con una cadena de responsabilidad.
* **Comando (+20)** La gestión de comandos de usuario podría beneficiarse del patrón comando para encapsular las acciones.
* **Intérprete (+40)** La lógica de evaluación del juego (e.g., utilidad del tablero) podría beneficiarse del patrón intérprete.
* **Iterador (+15)** No se utiliza un iterador para manejar colecciones como los posibles movimientos.
* **Mediador (+30)** Un mediador podría coordinar la comunicación entre diferentes componentes del juego (e.g., interfaz y lógica del juego).
* **Memento (+35)** El patrón memento podría ser utilizado para gestionar los estados del juego y permitir deshacer acciones.
* **Observador (+25)** El patrón observador podría ser útil para notificar a la interfaz sobre cambios en el estado del juego.
* **Estado (+30)** La lógica del juego podría beneficiarse del patrón estado para manejar diferentes etapas del juego.
* **Estrategia (+20)** El patrón estrategia podría ser utilizado para manejar diferentes algoritmos de movimiento.
* **Método Plantilla (+25)** El patrón método plantilla podría ser utilizado para definir el esqueleto de un algoritmo de juego, permitiendo variaciones.
* **Visitante (+35)** El patrón visitante podría ser utilizado para operar sobre elementos del juego sin modificar sus clases.

## Clase Analizada: `SeleccionController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)****:**
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):** Se utiliza un tipo primitivo (char) para representar las figuras del jugador y del oponente, en lugar de una enumeración o una clase dedicada.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Los campos figuraJugador, figuraOponente y jugadorEmpieza podrían agruparse en una clase o estructura en lugar de estar como campos estáticos.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** La clase depende de JavaFX para la interfaz de usuario, pero no se observan interfaces alternativas o diferentes implementaciones.
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** La clase usa campos estáticos para manejar el estado, lo cual puede ser problemático en un contexto de múltiples instancias.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase maneja diferentes tipos de cambios (selección de opciones de juego, validación de selección) en un solo lugar, lo que puede hacer que el código sea difícil de mantener.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** La clase realiza varias tareas relacionadas con la selección de opciones, lo que la convierte en una "cirugía de escopeta" al mezclar responsabilidades.

#### Dispensables

- **Comentarios (+2):** Los comentarios son mínimos y no explican en detalle la lógica del código.
- **Código duplicado (+7):** Hay duplicación en la lógica de selección de radio buttons, lo que podría ser refactorizado.
- **Clase de datos (+5):** La clase maneja datos estáticos que podrían ser encapsulados mejor.
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase tiene acceso a la configuración global (campos estáticos), lo que puede romper el encapsulamiento.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** La clase tiene mensajes duros en el código que podrían ser reemplazados por constantes.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase tiene múltiples responsabilidades (manejo de la UI y lógica de selección de opciones), lo que viola el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificarla. Cambios en la lógica de selección o en la UI requerirían modificaciones en esta clase.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase está acoplada a la lógica de JavaFX directamente, lo que viola el DIP. La lógica de selección debería estar desacoplada de la implementación de la interfaz gráfica.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)**
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `App`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):** La clase usa tipos primitivos para tamaño de ventana y no tiene una abstracción para ellos.
- **Lista de Parámetros Largos (+4):** El método switchScenes utiliza varios parámetros, lo cual puede ser problemático.
- **Grupos de Datos (+3):** No se agrupan los datos en una estructura o clase específica, pero los datos utilizados son simples.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** La clase está muy acoplada a JavaFX y no permite interfaces alternativas.
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** Utiliza campos estáticos para almacenar el Stage y el Scene, lo cual puede ser problemático en un contexto de múltiples instancias.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase maneja la configuración de la interfaz de usuario, lo que puede hacer que sea difícil cambiar la lógica de la aplicación sin modificar esta clase.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** La clase tiene múltiples responsabilidades relacionadas con la gestión de escenas y la carga de archivos FXML.

#### Dispensables

- **Comentarios (+2):** Hay un comentario mínimo, lo que podría dificultar la comprensión del propósito del método switchScenes.
- **Código duplicado (+7):**
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase utiliza campos estáticos para manejar el estado, lo que puede romper el encapsulamiento.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** La clase tiene un mensaje duro para la excepción en switchScenes, que podría ser mejor gestionado.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase maneja tanto la configuración de la interfaz de usuario como la gestión de escenas, lo que viola el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificarla, lo que viola el OCP.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase está acoplada a JavaFX directamente y no está desacoplada de la implementación de la interfaz gráfica, lo que viola el DIP.
 
### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** La clase App podría funcionar como una fachada para la gestión de la interfaz gráfica.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**



Este repositorio fue obtenido de: https://github.com/jcgallo1/2doParcialEstructuras