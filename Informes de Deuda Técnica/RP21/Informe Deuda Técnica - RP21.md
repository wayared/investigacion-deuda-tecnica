
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `JuegoController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** Métodos initialize, filtrarFeedback, comprar, fbAbajo, fbArriba, llenarFeedback, feedbackCargado y feedbackJuego son largos y realizan múltiples tareas.
- **Clase Grande (+6):** La clase JuegoController maneja muchas responsabilidades: interfaz de usuario, lógica de negocio, y manipulación de datos.
- **Obsesión Primitiva (+3):** Uso extensivo de String para manejar el estado y filtros de feedback en lugar de tipos más especializados.
- **Lista de Parámetros Largos (+4):** Métodos como llenarFeedback y feedbackCargado toman varios parámetros o manipulan listas sin encapsular estos datos.
- **Grupos de Datos (+3):** Se agrupan variables relacionadas con la interfaz de usuario y con la lógica de juego en una sola clase.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** La clase JuegoController tiene demasiadas responsabilidades, mezclando lógica de negocio con lógica de presentación.
- **Legado Rechazado (+6):** El controlador está muy acoplado a las clases específicas como PrimaryController y App, lo que dificulta la reutilización.
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** Campos como feedbackMostrado, lista, y textoCmbFiltro podrían ser calculados en lugar de ser campos estáticos.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica del juego pueden requerir modificaciones en el controlador y viceversa, lo que indica un alto acoplamiento.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la UI o en la lógica de negocio requieren cambios en múltiples lugares dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene pocos comentarios explicativos, lo cual puede dificultar la comprensión del código.
- **Código duplicado (+7):** Hay lógica repetitiva en el manejo de feedback y la actualización de la interfaz de usuario que podría ser extraída en métodos separados.
- **Clase de datos (+5):** El controlador actúa como una clase de datos al manejar múltiples variables de estado y manipular datos directamente.
- **Código muerto (+3):** Hay fragmentos de código comentado que parecen ser innecesarios o incompletos.
- **Clase perezosa (+4):** La clase podría beneficiarse de una refactorización para separar responsabilidades y simplificar su estructura.
- **Generalidad especulativa (+5):** La clase incluye funcionalidades que podrían ser redundantes o innecesarias para el caso actual.

#### Acopladores

- **Envidia de características (+5):** La clase JuegoController parece envidiar la funcionalidad de otras clases, como PrimaryController y App.
- **Intimidad inapropiada (+6):** Accede a campos y métodos de PrimaryController y App directamente, rompiendo el encapsulamiento.
- **Clase de biblioteca incompleta (+4):** La clase JuegoController parece ser parte de una biblioteca más grande y carece de una abstracción adecuada.
- **Cadenas de mensajes (+7):** La clase utiliza múltiples mensajes y métodos encadenados para realizar tareas complejas, lo que puede ser mejorado con el uso de patrones de diseño.
- **Hombre medio (+6):** La clase asume múltiples responsabilidades, incluyendo la lógica de presentación, manipulación de datos y lógica de negocio.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase JuegoController maneja múltiples responsabilidades: presentación, lógica de negocio, y acceso a datos.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificación; cambios en los requisitos pueden requerir cambios en la clase existente.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase está estrechamente acoplada a las implementaciones concretas de PrimaryController y App, violando el principio de inversión de dependencias.

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

## Clase Analizada: `MisJuegosController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos initialize, llenarJuegos, y misJuegosOrdenados son algo largos y contienen varias responsabilidades. Estos métodos podrían beneficiarse de ser divididos en métodos más pequeños y específicos.
- **Clase Grande (+6):** La clase MisJuegosController maneja tanto la inicialización como la lógica de interfaz de usuario y la ordenación de los juegos. Considerar delegar responsabilidades específicas a otras clases podría mejorar la mantenibilidad.
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** Las variables estáticas textoCmbFiltroMisJuegos, listaMisJuegos, y miJuegoMostrado son utilizadas en varios lugares. Mantener el estado de la clase con variables estáticas puede ser problemático si la clase se utiliza en múltiples contextos.

#### Preventores de Cambio

- **Cambio divergente (+6):** El método initialize realiza múltiples tareas, desde la configuración inicial hasta la verificación del tamaño de la lista de juegos. Dividir este método en varias funciones más pequeñas podría facilitar las modificaciones futuras.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):** La clase contiene algunos comentarios que podrían ser innecesarios si el código se refactoriza para ser más legible.
- **Código duplicado (+7):** La lógica de configuración de los VBox para los juegos en el método llenarJuegos parece repetitiva. Extraer esta lógica en un método separado ayudaría a reducir la duplicación.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase MisJuegosController maneja múltiples responsabilidades, incluyendo la inicialización de la interfaz, la filtración y la actualización de la vista. Dividir estas responsabilidades en clases separadas cumpliría mejor con el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** La creación y configuración de los VBox y ImageView en el método llenarJuegos podría beneficiarse del uso de un método de fábrica para encapsular la lógica de creación.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)** Si hay diferencias significativas en cómo se manejan los distintos tipos de datos de los juegos, un patrón Adaptador podría ser útil para estandarizar estas interacciones.
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** La clase MisJuegosController podría beneficiarse de una fachada que maneje la lógica de interacción con los datos y la vista, simplificando el controlador.
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

## Clase Analizada: `CarritoController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos initialize, comprar, y llenarCarrito son largos y contienen múltiples responsabilidades. Dividir estos métodos en submétodos más específicos mejoraría la claridad y la mantenibilidad.
- **Clase Grande (+6):** La clase CarritoController maneja la inicialización de la interfaz de usuario, la actualización del carrito y la lógica de compra. Desglosar estas responsabilidades en clases más pequeñas podría ser beneficioso.
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** La variable estática carritoMostrado se utiliza en varios métodos. El uso de variables estáticas para mantener el estado puede ser problemático en aplicaciones concurrentes o en diferentes contextos de uso.

#### Preventores de Cambio

- **Cambio divergente (+6):** El método initialize realiza múltiples tareas, desde la inicialización de la interfaz hasta la actualización de etiquetas y la habilitación/deshabilitación de botones. Dividir este método en varias funciones más pequeñas facilitaría las modificaciones futuras.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):** Los comentarios en la clase podrían ser innecesarios si el código se refactoriza para ser más legible.
- **Código duplicado (+7):** La lógica de creación y configuración de los elementos del carrito en el método llenarCarrito es repetitiva. Extraer esta lógica en un método separado ayudaría a reducir la duplicación.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase CarritoController maneja múltiples responsabilidades, incluyendo la inicialización de la interfaz, la actualización del carrito y la lógica de compra. Dividir estas responsabilidades en clases separadas cumpliría mejor con el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** La creación y configuración de los elementos del carrito (HBox, ImageView, Label) en el método llenarCarrito podría beneficiarse del uso de un método de fábrica para encapsular la lógica de creación.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)** Si hay diferencias significativas en cómo se manejan los distintos tipos de datos de los juegos, un patrón Adaptador podría ser útil para estandarizar estas interacciones.
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** La clase CarritoController podría beneficiarse de una fachada que maneje la lógica de interacción con los datos y la vista, simplificando el controlador.
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

## Clase Analizada: `PrimaryController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos initialize, llenarCarr, y llenarCategoria son bastante largos y contienen múltiples responsabilidades.
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** El uso de múltiples variables estáticas como juegoMostrado, categoriaMostrada, y carrito puede dificultar el manejo del estado de la aplicación en diferentes contextos.

#### Preventores de Cambio

- **Cambio divergente (+6):** Los métodos initialize, llenarCarr, y llenarCategoria realizan múltiples tareas, lo que hace que sea difícil modificar una parte del método sin afectar a otras.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables
 
- **Comentarios (+2):** Algunos comentarios podrían ser innecesarios si el código se refactoriza para ser más legible.
- **Código duplicado (+7):** La lógica de creación y configuración de los elementos de la interfaz se repite en varios lugares, especialmente en los métodos llenarCarr y llenarCategoria.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase PrimaryController maneja múltiples responsabilidades, incluyendo la inicialización de la interfaz, la actualización del carrusel y la búsqueda de juegos. Dividir estas responsabilidades en clases separadas cumpliría mejor con el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** La creación y configuración de los elementos del carrusel y las categorías podrían beneficiarse del uso de un método de fábrica para encapsular la lógica de creación.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** La clase PrimaryController podría beneficiarse de una fachada que maneje la lógica de interacción con los datos y la vista, simplificando el controlador.
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



Este repositorio fue obtenido de: https://github.com/DereckSantander/EDD-G3