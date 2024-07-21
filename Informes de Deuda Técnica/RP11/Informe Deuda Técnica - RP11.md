
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `ClientesController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** Los métodos initialize, llenarTableView, editarCliente, nuevoCliente, y cancelar no son particularmente largos, pero pueden ser simplificados.
- **Clase Grande (+6):** La clase ClientesController maneja múltiples responsabilidades como la configuración de la vista, la carga de datos y la transición entre vistas.
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de visualización y carga de datos pueden afectar la clase ClientesController.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** La clase ClientesController puede tener múltiples métodos afectados por cambios en la lógica de la aplicación.

#### Dispensables

- **Comentarios (+2):** La clase ClientesController carece de comentarios descriptivos que expliquen el propósito y funcionamiento del código.
- **Código duplicado (+7):**
- **Clase de datos (+5):** La clase ClientesController no es una simple clase de datos.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase realiza varias tareas relacionadas con la visualización y gestión de clientes.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase ClientesController maneja la configuración de la vista, la carga de datos, y la transición entre vistas. Podría beneficiarse de una mayor separación de responsabilidades.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está completamente diseñada para ser extensible sin modificar el código existente. La lógica de transición entre vistas podría ser extraída a una clase de servicio o gestor.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase ClientesController depende directamente de la implementación de FXMLLoader y las vistas, lo que puede dificultar el testeo y la extensión.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la creación de instancias de controladores y vistas.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Podría ser utilizado para simplificar la interacción con la lógica de carga y visualización de clientes.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)** Podría ser utilizado para encapsular las acciones de los botones (editarCliente, nuevoCliente, cancelar).
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)** Podría ser utilizado para manejar la comunicación entre ClientesController y otros componentes de la aplicación.
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `NewClienteController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos editarCliente y guardarCliente son extensos y realizan múltiples operaciones.
- **Clase Grande (+6):** La clase maneja tanto la lógica de edición como de adición de clientes y representantes, lo cual puede ser dividido en varias clases.
- **Obsesión Primitiva (+3):** Se utiliza texto plano para manejar datos, lo que puede ser mejorado utilizando objetos de dominio.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** La clase utiliza ArrayList para manejar colecciones de Cliente y Representante.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** Los métodos editarCliente y guardarCliente están acoplados a la lógica de manipulación de archivos, lo cual puede cambiar con el tiempo.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la estructura de archivos o en la representación de datos podrían afectar múltiples partes de esta clase.

#### Dispensables

- **Comentarios (+2):** La clase carece de comentarios descriptivos que expliquen la lógica de los métodos y las operaciones.
- **Código duplicado (+7):** Existen duplicaciones en la forma en que se manejan los datos de clientes y representantes.
- **Clase de datos (+5):** La clase NewClienteController no es simplemente una clase de datos, ya que contiene lógica de negocio.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase realiza múltiples tareas relacionadas con la adición y edición de clientes, lo que puede ser mejorado.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase accede y manipula datos de archivos directamente, lo cual puede ser mejorado.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase NewClienteController tiene múltiples responsabilidades (edición y adición de clientes y representantes), lo que puede ser mejorado separando responsabilidades en diferentes clases.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificar el código existente. Cambios en el formato de archivo o en la lógica de cliente y representante pueden requerir modificaciones en la clase.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de FileWriter, BufferedWriter y de la estructura de archivos. Utilizar un servicio o repositorio para manejar datos podría mejorar la flexibilidad y testabilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la creación de instancias de Cliente y Representante.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)** Podría ser utilizado para adaptar las interfaces de entrada/salida de archivos a la lógica de la aplicación.
* **Puente (+35)** 
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Podría ser utilizado para simplificar la interacción con la lógica de adición y edición de datos.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)** Podría ser utilizado para encapsular las operaciones de guardar y editar como comandos separados.
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)** Podría ser utilizado para manejar la comunicación entre el controlador y otras partes de la aplicación.
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `NewEmpleadoController `

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos editarEmpleado, guardarEmpleado y eliminarEmpleado son extensos y realizan varias operaciones.
- **Clase Grande (+6):** La clase maneja múltiples responsabilidades (edición, adición, y eliminación de empleados), lo que puede ser mejorado separando estas responsabilidades en diferentes clases o servicios.
- **Obsesión Primitiva (+3):** La clase utiliza datos primitivos para gestionar empleados en lugar de utilizar objetos bien definidos.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Los datos de empleados se manejan como cadenas de texto en lugar de objetos, lo que puede resultar en una gestión menos eficiente y más propensa a errores.
 
#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase está acoplada a la lógica de manejo de archivos. Cambios en el formato del archivo o en la lógica del empleado pueden requerir modificaciones en la clase.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en el formato de archivo o en la estructura de datos podrían afectar múltiples partes de esta clase.

#### Dispensables

- **Comentarios (+2):** Falta de comentarios descriptivos que expliquen el propósito de los métodos y operaciones.
- **Código duplicado (+7):** Hay duplicación en la forma en que se gestionan las listas de empleados y se actualizan los archivos.
- **Clase de datos (+5):** Los datos se manejan como texto en lugar de usar objetos bien definidos para representar empleados.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase realiza múltiples tareas (adición, edición y eliminación), lo que puede ser mejorado.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase accede y manipula directamente los archivos, lo que podría ser mejorado utilizando un servicio o repositorio para manejar datos.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase maneja múltiples responsabilidades: adición, edición y eliminación de empleados, lo que va en contra del SRP. Esta clase debería enfocarse en una sola responsabilidad.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificar el código existente. Cambios en la lógica de manejo de archivos o en la estructura de datos pueden requerir modificaciones en la clase.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de FileWriter, BufferedWriter y de la estructura de archivos. Utilizar un servicio o repositorio para manejar datos podría mejorar la flexibilidad y testabilidad.

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

## Clase Analizada: `SecondaryControllers`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos initialize, tablaBingo, portadaGanadora, portadaIcono, y segundo son extensos y realizan múltiples tareas.
- **Clase Grande (+6):** La clase maneja la configuración de una vista completa en la aplicación, incluyendo la inicialización, gestión de botones y multimedia, lo cual puede ser mejorado.
- **Obsesión Primitiva (+3):** Se utilizan datos primitivos para gestionar el número y las estadísticas en lugar de utilizar objetos o clases dedicadas.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Los datos como los números y botones se manejan como primitivas o listas sin encapsular en objetos adecuados.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase está acoplada a la lógica de manejo de interfaz de usuario y multimedia. Cambios en la interfaz o en la lógica de archivos pueden requerir modificaciones en esta clase.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la interfaz o en la lógica de manejo de archivos pueden requerir cambios en varios métodos de esta clase.

#### Dispensables

- **Comentarios (+2):** La clase carece de comentarios explicativos sobre el propósito y funcionamiento de sus métodos.
- **Código duplicado (+7):** Hay duplicación en la forma en que se gestionan imágenes y botones. Los métodos portadaIcono y portadaGanadora tienen código repetitivo para cargar imágenes.
- **Clase de datos (+5):** Los datos se manejan como texto o números en lugar de usar objetos bien definidos para representar la lógica de juego y estadísticas.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase maneja múltiples responsabilidades, lo que puede ser considerado como una pereza en la separación de responsabilidades.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase accede y manipula directamente los archivos y recursos multimedia, lo que podría ser mejorado utilizando un servicio o repositorio para manejar datos y recursos.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase maneja múltiples responsabilidades: inicialización de la vista, manejo de botones, y reproducción de medios, lo que va en contra del SRP. Esta clase debería enfocarse en una sola responsabilidad.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificar el código existente. Cambios en la lógica de interfaz o multimedia pueden requerir modificaciones en la clase.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de recursos específicos como archivos de imagen y audio, lo que va en contra del DIP. Utilizar un servicio o repositorio para manejar la carga de recursos podría mejorar la flexibilidad y testabilidad de la clase.

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



Este repositorio fue obtenido de: https://github.com/LastDaniels/POO-P1-G08-2P