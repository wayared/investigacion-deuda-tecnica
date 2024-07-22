
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `App`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** La clase App tiene varios métodos largos, en particular aquellos relacionados con la carga de datos y la gestión de imágenes.
- **Clase Grande (+6):** La clase App hace muchas cosas (carga de datos, manejo de imágenes, gestión de ventanas, etc.), lo que la convierte en una clase grande. 
- **Obsesión Primitiva (+3):** La clase utiliza primitivos y cadenas en algunos casos (por ejemplo, en cargarDatos y en la serialización de usuarios).
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** La clase utiliza campos temporales para manejar rutas y estados, pero no de manera crítica.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase está bastante enfocada en la gestión de la aplicación, pero las responsabilidades están mezcladas, lo que puede hacer que los cambios sean más difíciles de implementar.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):** La clase tiene pocos comentarios, lo que puede dificultar la comprensión del código.
- **Código duplicado (+7):** Hay duplicación en la lógica de manejo de imágenes.
- **Clase de datos (+5):** La clase tiene una mezcla de responsabilidades y no es solo una clase de datos.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase está bastante activa, pero la responsabilidad está un poco mezclada.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** La clase maneja cadenas de mensajes, pero podría ser más robusta en el manejo de errores.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase App viola SRP porque maneja múltiples responsabilidades, como la carga de escenas, la gestión de imágenes, y la serialización de usuarios.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase es difícil de extender sin modificar el código existente, especialmente en el manejo de imágenes y datos.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende de detalles de implementación (como FileInputStream y BufferedReader), lo que puede ser una oportunidad para mejorar la flexibilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)** La clase App utiliza constructores, pero no se observa un patrón de diseño específico para la creación de instancias.
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)** La clase App podría beneficiarse del patrón Singleton para asegurar una única instancia.

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** La clase App podría beneficiarse del patrón Fachada para simplificar la interacción con la carga de datos y la gestión de imágenes.
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

## Clase Analizada: `VentanaDetalleController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** La clase tiene métodos extensos como filtrarNuevos(), filtrarViejos(), filtrarMejores(), y filtrarPeores() que realizan múltiples operaciones, haciendo que sea difícil de leer y mantener.
- **Clase Grande (+6):** VentanaDetalleController es una clase muy grande con muchas responsabilidades, incluyendo la manipulación de la interfaz de usuario, la gestión de eventos, el manejo de datos y la interacción con archivos.
- **Obsesión Primitiva (+3):** La clase usa tipos primitivos como String y int para representar datos que podrían ser encapsulados en clases propias (por ejemplo, Valoracion).
- **Lista de Parámetros Largos (+4):** Métodos como anadirVboxResenia() tienen muchos parámetros, lo que puede ser confuso y propenso a errores.
- **Grupos de Datos (+3):** La clase contiene numerosos grupos de datos y atributos que se utilizan en varios métodos, lo que incrementa la complejidad y acoplamiento.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** La clase está muy acoplada a la interfaz gráfica y a la lógica de negocio, mezclando responsabilidades que deberían estar en diferentes clases.
- **Legado Rechazado (+6):** El uso de PriorityQueue para filtrar reseñas parece inusual y puede ser un indicativo de un enfoque anticuado o inadecuado para el manejo de colecciones.
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** Algunos campos, como modo y modocontrario, son utilizados en varias partes del código, lo que puede ser una indicación de que la clase está manejando demasiadas responsabilidades.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase está diseñada de tal manera que un cambio en la lógica de presentación, manejo de datos, o interacción del usuario requiere modificaciones en múltiples métodos.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la interfaz de usuario o en la lógica de negocio afectan múltiples métodos y áreas del código, lo que sugiere una falta de separación de preocupaciones.

#### Dispensables

- **Comentarios (+2):** Los comentarios son mínimos y no proporcionan información útil sobre la lógica o el propósito de los métodos.
- **Código duplicado (+7):** Métodos como filtrarNuevos(), filtrarViejos(), filtrarMejores(), y filtrarPeores() tienen una lógica similar que podría ser extraída a un método común.
- **Clase de datos (+5):** La clase maneja muchos tipos de datos específicos y operaciones directamente, en lugar de delegar a clases de datos especializadas.
- **Código muerto (+3):** Hay fragmentos de código comentado (por ejemplo, llenarVboxSS()), que pueden ser eliminados si ya no se utilizan.
- **Clase perezosa (+4):** La clase tiene muchas responsabilidades (UI, lógica de negocio, manejo de eventos), lo que sugiere que debería ser dividida en varias clases.
- **Generalidad especulativa (+5):** El uso de métodos como cambiarImagen() para realizar transiciones puede estar sobrediseñado si no se usa en contextos más generales.

#### Acopladores

- **Envidia de características (+5):** La clase accede a atributos de Juego y Usuario directamente, en lugar de delegar en métodos de esos objetos.
- **Intimidad inapropiada (+6):** La clase accede a detalles internos de Juego y Usuario, lo que sugiere una fuerte dependencia entre las clases.
- **Clase de biblioteca incompleta (+4):** La clase parece ser un controlador de la vista con poca modularidad y reutilización, lo que sugiere que podría haber una mejor separación de responsabilidades.
- **Cadenas de mensajes (+7):** La clase utiliza múltiples cadenas de texto para definir estilos y mensajes, lo que podría ser centralizado en una clase de recursos.
- **Hombre medio (+6):** La clase actúa como un "hombre medio" entre la interfaz de usuario y la lógica de negocio, sin una separación clara de responsabilidades.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase tiene múltiples responsabilidades: manejar la interfaz de usuario, gestionar eventos, filtrar datos, y manejar archivos. Debería dividirse en varias clases con responsabilidades más específicas.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está abierta a la extensión y está cerrada a la modificación; cualquier cambio en la lógica de filtrado o en la interfaz requiere modificar la clase.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)** Aunque no se usan interfaces explícitas, la clase implementa demasiadas responsabilidades para un solo controlador, sugiriendo que se podrían haber creado interfaces más específicas para la funcionalidad.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de las implementaciones de Juego y Usuario, en lugar de depender de abstracciones o interfaces que permitan una mayor flexibilidad.

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

## Clase Analizada: `LoginController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** La clase tiene métodos como verificarIngreso() y registrar() que realizan múltiples tareas, incluyendo lógica de control de flujo, manipulación de archivos, y actualización de la interfaz de usuario. Estos métodos podrían beneficiarse de ser descompuestos en métodos más pequeños y enfocados.
- **Clase Grande (+6):** La clase maneja múltiples responsabilidades: la lógica de autenticación de usuarios, el registro de nuevos usuarios, la manipulación de archivos y la actualización de la interfaz de usuario. Considerar la separación de estas responsabilidades en diferentes clases puede mejorar la mantenibilidad.
- **Obsesión Primitiva (+3):** Se usa directamente tipos primitivos (como String para contraseñas y nombres de usuario) y colecciones básicas en lugar de abstraer estas operaciones con clases específicas (como un Usuario).
- **Lista de Parámetros Largos (+4):** Aunque la clase no tiene métodos con listas largas de parámetros, las cadenas de texto usadas para archivos ("Usuarios/" + txfUsuario.getText() + ".bin") son largas y propensas a errores. Se podrían usar constantes o configuraciones para manejar estas rutas.
- **Grupos de Datos (+3):** La clase maneja datos de usuario y configuración que podrían beneficiarse de ser encapsulados en objetos separados en lugar de manipular directamente archivos de usuario.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** No se utilizan interfaces ni clases alternativas para manejar la lógica de usuario y la interfaz. Podría ser útil introducir interfaces para la lógica de autenticación o registro.
- **Legado Rechazado (+6):** La manipulación directa de archivos y la serialización de objetos es una práctica que puede llevar a problemas de mantenimiento y escalabilidad. Considerar el uso de un sistema de persistencia más robusto podría mejorar el diseño.
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** El uso de campos temporales como txfUsuario y txfClave está bien, pero se podrían usar variables locales en lugar de campos si no es necesario mantener el estado entre métodos.

#### Preventores de Cambio

- **Cambio divergente (+6):**  Los cambios en la lógica de autenticación o registro requerirían modificaciones en múltiples partes del código debido a la falta de separación de responsabilidades.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Los cambios en la lógica de manejo de usuarios o archivos afectarían múltiples métodos y áreas de la clase, lo que hace que el mantenimiento sea más complejo.
 
#### Dispensables

- **Comentarios (+2):** La clase carece de comentarios que expliquen la lógica de negocio o el propósito de los métodos y variables. Agregar comentarios ayudaría a mejorar la comprensión del código.
- **Código duplicado (+7):** Hay duplicación en el manejo de errores y el código para limpiar los campos de texto. Podría ser útil abstraer estas operaciones en métodos reutilizables.
- **Clase de datos (+5):** La clase maneja datos de usuario como strings y no aprovecha la encapsulación adecuada en objetos. El uso de una clase de datos específica para manejar usuarios podría ser beneficioso.
- **Código muerto (+3):** 
- **Clase perezosa (+4):** La clase maneja varias responsabilidades y puede beneficiarse de ser dividida en clases más específicas y responsables.
- **Generalidad especulativa (+5):** La clase no muestra una alta generalidad especulativa, pero la implementación actual podría no ser flexible para futuros cambios en la lógica de autenticación o registro.

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase LoginController maneja múltiples responsabilidades, como la autenticación de usuarios, el registro de nuevos usuarios y la manipulación de la interfaz de usuario. Esto viola el SRP, que sugiere que una clase debe tener una sola razón para cambiar.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está abierta para extensión y cerrada para modificación. Cambios en los requisitos de autenticación o registro requerirán modificaciones en la clase, en lugar de extenderla de forma modular.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de la implementación concreta de manejo de archivos y de la lógica de Usuario. Debería depender de abstracciones, como interfaces para la persistencia y la gestión de usuarios.

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

## Clase Analizada: `VentanaPrincipalDemoController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como initialize, moverIzq, moverDer, llenarCatalogo2, moverDestacados, y cambiarModo tienen una longitud considerable, lo que puede hacer que sean difíciles de entender y mantener.
- **Clase Grande (+6):** La clase tiene muchos atributos y métodos, lo que sugiere que realiza muchas tareas y puede violar el Principio de Responsabilidad Única.
- **Obsesión Primitiva (+3):** Utiliza cadenas de texto para representar colores y otros datos en lugar de tipos más adecuados o enums.
- **Lista de Parámetros Largos (+4):** Métodos como abrirVentanaJuego y abrirVentanaUsuario tienen múltiples parámetros que podrían ser agrupados en objetos.
- **Grupos de Datos (+3):** Atributos como modo y modocontrario podrían ser encapsulados en una clase específica para manejar configuraciones de UI.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** La clase mezcla lógica de negocio (gestión de juegos, cambios de modo) con lógica de UI (eventos de botones, cambios de escena).
- **Legado Rechazado (+6):** La clase parece estar diseñada para heredar o extender en un futuro, pero el acoplamiento fuerte y la falta de interfaces complican esta extensión.
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** Los campos como img_juego_actual, juego_actual, imagenDestacada_actual, etc., parecen ser utilizados temporalmente y podrían ser reemplazados por objetos más adecuados.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de UI afectan la lógica de negocio y viceversa. La clase maneja tanto la lógica de presentación como la de gestión de datos.
- **Jerarquías de herencia paralela (+7):** La clase usa múltiples tipos de datos y objetos que no se heredan ni se extienden fácilmente, lo que puede limitar la flexibilidad.
- **Cirugía de escopeta (+8):** Cambios en la apariencia de la UI requieren cambios extensivos en múltiples métodos que manejan la lógica de visualización.

#### Dispensables

- **Comentarios (+2):** La clase contiene algunos comentarios, pero no son suficientes para explicar la lógica compleja ni la intención detrás de algunos bloques de código.
- **Código duplicado (+7):** Existen bloques de código repetidos, como la configuración de estilos en el método cambiarModo y en otros métodos.
- **Clase de datos (+5):** La clase podría beneficiarse de la introducción de clases de datos para encapsular configuraciones y datos temporales.
- **Código muerto (+3):** Algunas secciones comentadas o métodos no utilizados, como el código comentado para hbox_h, sugieren código muerto.
- **Clase perezosa (+4):** La clase realiza muchas tareas y tiene muchas responsabilidades, lo que la hace menos manejable y reutilizable.
- **Generalidad especulativa (+5):** La clase incluye configuraciones y funcionalidades que pueden no ser necesarias en su forma actual, lo que sugiere una posible sobrecarga.

#### Acopladores

- **Envidia de características (+5):** La clase parece manejar muchas características de los objetos Juego y Image sin delegar responsabilidades a ellos.
- **Intimidad inapropiada (+6):** La clase accede y modifica los atributos internos de otras clases, como App, en lugar de utilizar métodos apropiados para interactuar con ellos.
- **Clase de biblioteca incompleta (+4):** La clase parece ser una implementación específica y no está diseñada para ser una biblioteca reutilizable o extensible.
- **Cadenas de mensajes (+7):** Se observan cadenas de mensajes que se pasan entre métodos sin utilizar mecanismos de comunicación más robustos.
- **Hombre medio (+6):** La clase realiza tareas que podrían ser realizadas por otras clases, lo que resulta en un acoplamiento alto y una responsabilidad excesiva.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase tiene múltiples responsabilidades, incluyendo manejo de UI, gestión de datos, y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está fácilmente extensible sin modificar su código, lo que la hace difícil de extender sin cambiar la implementación existente.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)** La clase maneja una variedad de interfaces que no están bien separadas, violando el principio de interfaces específicas para clientes específicos.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende de implementaciones concretas en lugar de interfaces o abstracciones, lo que dificulta la flexibilidad y la prueba del código.

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



Este repositorio fue obtenido de: https://github.com/Fausto-Briones/ProyectoEstructuras