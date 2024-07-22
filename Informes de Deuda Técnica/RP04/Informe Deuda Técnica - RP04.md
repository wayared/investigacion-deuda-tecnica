
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `Main`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** No hay métodos particularmente largos, pero la repetición de lógica en buscarServicio(), buscarEmpleado(), y buscarCliente() hace que cada uno tenga una longitud considerable.
- **Clase Grande (+6):** La clase Main tiene varios métodos, lo que la hace un poco extensa.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos y cadenas para representar datos que podrían encapsularse en objetos más complejos.
- **Lista de Parámetros Largos (+4):** No se observan listas largas de parámetros.
- **Grupos de Datos (+3):** Hay varios métodos que operan sobre datos relacionados (servicios, empleados, clientes) que podrían encapsularse mejor.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):** Uso de switch en el método main().
- **Campos Temporales (+4):** Variables temporales se utilizan dentro de métodos, pero no se observan campos temporales.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de búsqueda pueden requerir cambios en múltiples lugares debido a la repetición de lógica.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en las validaciones o en la forma de seleccionar elementos pueden requerir cambios en varios métodos.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):** Lógica de selección de elementos (buscarServicio(), buscarEmpleado(), buscarCliente()) es muy similar.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):** Métodos están muy acoplados con la clase Usuario. 
- **Intimidad inapropiada (+6):** La clase Main accede directamente a los detalles de Usuario.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Main tiene múltiples responsabilidades (buscar servicios, empleados, clientes, manejar el menú).
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no es fácilmente extensible sin modificar su código.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)** No aplica directamente, pero la interfaz de la clase podría beneficiarse de ser dividida.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Main depende directamente de la clase Usuario.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** No utilizado.
- **Constructor (+25)** No utilizado.
- **Método de Fábrica (+20)** No utilizado.
- **Prototipo (+30)** No utilizado.
- **Singleton (+15)** No utilizado.

#### Estructurales

* **Adaptador (+25)** No utilizado.
* **Puente (+35)** No utilizado.
* **Compuesto (+30)** No utilizado.
* **Decorador (+25)** No utilizado. 
* **Fachada (+20)** No utilizado.
* **Peso Ligero (+40)** No utilizado.
* **Proxy (+30)** No utilizado.

#### De comportamiento

* **Cadena de Responsabilidad (+30)** No utilizado.
* **Comando (+20)** Podría ser utilizado para las acciones de buscar y validar datos.
* **Intérprete (+40)** No utilizado.
* **Iterador (+15)** No utilizado.
* **Mediador (+30)** No utilizado.
* **Memento (+35)** No utilizado.
* **Observador (+25)** No utilizado.
* **Estado (+30)** No utilizado.
* **Estrategia (+20)** No utilizado.
* **Método Plantilla (+25)** No utilizado.
* **Visitante (+35)** No utilizado.

## Clase Analizada: `Menu`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como menuServicio, menuEmpleado, menuCliente, menuCita y menuAtencion son bastante largos.
- **Clase Grande (+6):** La clase Menu maneja muchas responsabilidades relacionadas con diferentes entidades (Servicios, Empleados, Clientes, Citas y Atenciones).
- **Obsesión Primitiva (+3):** Uso intensivo de tipos primitivos para representar opciones de menú y datos de entrada.
- **Lista de Parámetros Largos (+4):** No se observa una lista de parámetros largos, aunque se podrían mejorar las firmas de métodos.
- **Grupos de Datos (+3):** Los datos relacionados podrían encapsularse en clases más específicas para mejorar la organización.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):** Uso extensivo de sentencias switch para la lógica del menú.
- **Campos Temporales (+4):** Variables temporales usadas dentro de los métodos, aunque no hay campos temporales explícitos.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de menú pueden requerir modificaciones en múltiples lugares.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en validaciones o en la forma de gestionar las opciones pueden requerir cambios en varios métodos.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):** Lógica similar en diferentes métodos de menú.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):** Métodos están muy acoplados con la clase Usuario.
- **Intimidad inapropiada (+6):** La clase Menu accede directamente a los detalles de Usuario.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Menu tiene múltiples responsabilidades (gestionar servicios, empleados, clientes, citas y atenciones).
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no es fácilmente extensible sin modificar su código.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)** No aplica directamente, pero la interfaz de la clase podría beneficiarse de ser dividida.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Menu depende directamente de la clase Usuario.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** No utilizado.
- **Constructor (+25)** No utilizado.
- **Método de Fábrica (+20)** No utilizado.
- **Prototipo (+30)** No utilizado.
- **Singleton (+15)** No utilizado.
 
#### Estructurales

* **Adaptador (+25)** No utilizado.
* **Puente (+35)** No utilizado.
* **Compuesto (+30)** No utilizado.
* **Decorador (+25)** No utilizado.
* **Fachada (+20)** No utilizado.
* **Peso Ligero (+40)** No utilizado.
* **Proxy (+30)** No utilizado.

#### De comportamiento

* **Cadena de Responsabilidad (+30)** No utilizado.
* **Comando (+20)** Podría ser utilizado para las acciones de menú.
* **Intérprete (+40)** No utilizado.
* **Iterador (+15)** No utilizado.
* **Mediador (+30)** No utilizado.
* **Memento (+35)** No utilizado.
* **Observador (+25)** No utilizado.
* **Estado (+30)** No utilizado.
* **Estrategia (+20)** No utilizado.
* **Método Plantilla (+25)** No utilizado.
* **Visitante (+35)** No utilizado.

## Clase Analizada: `Usuario`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)****:** El método crearCliente tiene múltiples tareas, como validar datos de clientes y representantes, y podría dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase Usuario contiene múltiples responsabilidades, como la gestión de servicios, empleados, clientes, citas y atenciones, lo que la hace considerablemente grande.
- **Obsesión Primitiva (+3):** Uso intensivo de tipos de datos primitivos (String, int, double) para representar información que podría ser encapsulada en objetos más específicos.
- **Lista de Parámetros Largos (+4):** Métodos como crearEmpleado y crearCliente tienen múltiples parámetros de entrada, lo que dificulta su mantenimiento y comprensión.
- **Grupos de Datos (+3):** Los datos de cliente y representante en el método crearCliente son grupos de datos que podrían encapsularse en objetos.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):** El método consultarAtenciones utiliza un switch para diferenciar entre varias opciones de consulta, lo que puede considerarse un olor a código.
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase Usuario tiene múltiples razones para cambiar, como cambios en la lógica de citas, empleados, servicios, etc.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la validación de datos o lógica de negocio afectarían múltiples métodos en esta clase.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):** La lógica de validación de datos (nombre, cédula, teléfono, email) se repite en varios métodos como crearCliente y crearEmpleado.
- **Clase de datos (+5):** La clase contiene muchos métodos para manejar datos, lo que puede ser considerado una clase de datos.
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Usuario tiene múltiples responsabilidades, como la gestión de servicios, empleados, clientes, citas y atenciones.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser fácilmente extensible sin modificar su código fuente, lo que puede dificultar futuras extensiones.
- **Principio de Sustitución de Liskov (LSP) (+35)** 
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Usuario depende de clases concretas como Servicio, Empleado, Cliente, Cita, y Atencion en lugar de abstracciones, lo que viola DIP.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría ser utilizado para crear servicios, empleados y clientes de manera más flexible.
- **Constructor (+25)** Podría ser utilizado para encapsular la lógica de construcción de objetos complejos como Empleado y Cliente.
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la lógica de creación de objetos y reducir la duplicación de código.
- **Prototipo (+30)**
- **Singleton (+15)** Podría ser utilizado si se necesita una única instancia de Usuario.

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Podría ser utilizado para simplificar la interacción con múltiples clases y métodos.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)** Podría ser utilizado para manejar las validaciones de datos de manera más flexible.
* **Comando (+20)** Podría ser utilizado para encapsular solicitudes como la creación de servicios, empleados, etc.
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)** Podría ser utilizado para reducir la complejidad de las interacciones entre objetos.
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)** Podría ser utilizado para manejar el estado de los servicios y empleados de manera más estructurada.
* **Estrategia (+20)** Podría ser utilizado para encapsular algoritmos de validación y creación de objetos.
* **Método Plantilla (+25)** Podría ser utilizado para definir la estructura de los métodos de creación de objetos y permitir que las subclases redefinan ciertos pasos.
* **Visitante (+35)**

## Clase Analizada: `Validacion`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** 
- **Clase Grande (+6):** La clase Validacion es relativamente pequeña y se enfoca en validaciones, por lo que no califica como clase grande.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos y String en lugar de encapsular lógica en objetos más específicos, especialmente en la validación de nombres y emails.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** La validación de nombres utiliza un array de caracteres especiales y un ArrayList, lo que podría considerarse un grupo de datos.
 
#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio
 
- **Cambio divergente (+6):** La clase Validacion podría cambiar por múltiples razones (validación de diferentes tipos de datos), pero cada método está suficientemente encapsulado.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la lógica de validación afectarán solo métodos específicos.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios detallados que explican cada método, lo cual es útil pero puede ser excesivo si el código fuera autoexplicativo.
- **Código duplicado (+7):**
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Validacion se adhiere al SRP, ya que cada método tiene una única responsabilidad de validación.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser fácilmente extensible sin modificar su código fuente, lo que puede dificultar futuras extensiones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Validacion no depende de abstracciones, sino de implementaciones concretas.
 
### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la lógica de creación de objetos de validación.
- **Prototipo (+30)**
- **Singleton (+15)** Podría ser utilizado si se necesita una única instancia de Validacion.

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Podría ser utilizado para simplificar la interacción con múltiples validaciones.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)** Podría ser utilizado para manejar las validaciones de manera más flexible.
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)** Podría ser utilizado para encapsular diferentes algoritmos de validación.
* **Método Plantilla (+25)** Podría ser utilizado para definir la estructura de los métodos de validación y permitir que las subclases redefinan ciertos pasos.
* **Visitante (+35)**



Este repositorio fue obtenido de: https://github.com/ChrisAcosta19/POO-P2-G04