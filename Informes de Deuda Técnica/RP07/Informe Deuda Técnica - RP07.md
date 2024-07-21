
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `ProyectoPOOG6`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** El método main y algunos de los métodos anidados (como el manejo de menús) son largos y tienen múltiples responsabilidades, lo que puede hacerlos difíciles de mantener y entender.
- **Clase Grande (+6):** La clase ProyectoPOOG6 contiene múltiples métodos para manejar diferentes aspectos del sistema (servicios, empleados, clientes, citas, atenciones), lo que la convierte en una clase grande.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos (String, int, etc.) en lugar de encapsular la lógica en objetos más específicos. Por ejemplo, la validación de entradas de usuario podría beneficiarse de clases dedicadas.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):** Se utilizan múltiples sentencias switch en el manejo de los menús, lo que puede ser un indicativo de que una estructura de comandos podría ser más adecuada.
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase ProyectoPOOG6 podría cambiar por múltiples razones, ya que maneja varias responsabilidades (inicialización del sistema, manejo de menús, operaciones CRUD para servicios, empleados, clientes, citas, y atenciones).
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la lógica del sistema afectarán múltiples métodos dentro de esta clase, lo que puede indicar una necesidad de refactorización para mejorar la cohesión.

#### Dispensables

- **Comentarios (+2):**
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase ProyectoPOOG6 no se adhiere completamente al SRP, ya que maneja múltiples responsabilidades, como la inicialización del sistema, la gestión de menús y las operaciones CRUD.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser fácilmente extensible sin modificar su código fuente, lo que puede dificultar futuras extensiones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase ProyectoPOOG6 no depende de abstracciones, sino de implementaciones concretas.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la lógica de creación de objetos de validación.
- **Prototipo (+30)**
- **Singleton (+15)** Podría ser utilizado si se necesita una única instancia de ProyectoPOOG6.

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
* **Comando (+20)** Podría ser utilizado para encapsular las acciones del menú en comandos.
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)** Podría ser utilizado para encapsular diferentes algoritmos de validación.
* **Método Plantilla (+25)** Podría ser utilizado para definir la estructura de los métodos de validación y permitir que las subclases redefinan ciertos pasos.
* **Visitante (+35)**

## Clase Analizada: `Empleado`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos agregarEmpleado, editarEmpleado y mostrarEmpleadosDisponibles son largos y realizan múltiples tareas, lo que puede hacerlos difíciles de mantener y entender. 
- **Clase Grande (+6):** La clase Empleado maneja varias responsabilidades, lo que la convierte en una clase grande.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos (String, boolean, etc.) en lugar de encapsular la lógica en objetos más específicos.
- **Lista de Parámetros Largos (+4):** Los métodos mostrarEmpleadosDisponibles y editarEmpleado tienen listas de parámetros largas.
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase Empleado podría cambiar por múltiples razones, ya que maneja varias responsabilidades (mostrar, agregar, editar y eliminar empleados, así como verificar disponibilidad).
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la lógica del sistema afectarán múltiples métodos dentro de esta clase, lo que puede indicar una necesidad de refactorización para mejorar la cohesión.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios descriptivos que explican el propósito de cada método.
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Empleado no se adhiere completamente al SRP, ya que maneja múltiples responsabilidades, como mostrar, agregar, editar y eliminar empleados, así como verificar disponibilidad.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser fácilmente extensible sin modificar su código fuente, lo que puede dificultar futuras extensiones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Empleado no depende de abstracciones, sino de implementaciones concretas.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la lógica de creación de empleados.
- **Prototipo (+30)**
- **Singleton (+15)** Podría ser utilizado si se necesita una única instancia de Empleado.

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
* **Comando (+20)** Podría ser utilizado para encapsular las acciones del menú en comandos.
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)** Podría ser utilizado para encapsular diferentes algoritmos de validación.
* **Método Plantilla (+25)** Podría ser utilizado para definir la estructura de los métodos de validación y permitir que las subclases redefinan ciertos pasos.
* **Visitante (+35)**

## Clase Analizada: `Atencion`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos registrarAtencion y consultarAtencion son largos y realizan múltiples tareas, lo que puede hacerlos difíciles de mantener y entender.
- **Clase Grande (+6):** La clase Atencion maneja varias responsabilidades, lo que la convierte en una clase grande.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos (String, int, etc.) en lugar de encapsular la lógica en objetos más específicos.
- **Lista de Parámetros Largos (+4):** Los métodos registrarAtencion tienen listas de parámetros largas.
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase Atencion podría cambiar por múltiples razones, ya que maneja varias responsabilidades (registrar y consultar atenciones).
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la lógica del sistema afectarán múltiples métodos dentro de esta clase, lo que puede indicar una necesidad de refactorización para mejorar la cohesión.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios descriptivos que explican el propósito de cada método.
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Atencion no se adhiere completamente al SRP, ya que maneja múltiples responsabilidades, como registrar y consultar atenciones.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser fácilmente extensible sin modificar su código fuente, lo que puede dificultar futuras extensiones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Atencion no depende de abstracciones, sino de implementaciones concretas.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la lógica de creación de atenciones.
- **Prototipo (+30)**
- **Singleton (+15)** Podría ser utilizado si se necesita una única instancia de Atencion.

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
* **Comando (+20)** Podría ser utilizado para encapsular las acciones del menú en comandos.
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)** Podría ser utilizado para encapsular diferentes algoritmos de validación.
* **Método Plantilla (+25)** Podría ser utilizado para definir la estructura de los métodos de validación y permitir que las subclases redefinan ciertos pasos.
* **Visitante (+35)**

## Clase Analizada: `Cita`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos crearCita, eliminarCita, consultarCita, y citasNoAtendidas son largos y realizan múltiples tareas.
- **Clase Grande (+6):** La clase Cita maneja varias responsabilidades, como la creación, eliminación y consulta de citas.
- **Obsesión Primitiva (+3):** La clase utiliza tipos primitivos (String, int) para representar la información de las citas en lugar de objetos más específicos.
- **Lista de Parámetros Largos (+4):** Los métodos crearCita y eliminarCita tienen listas de parámetros largas.
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase Cita podría cambiar por múltiples razones, ya que maneja varias responsabilidades.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la lógica de las citas afectan múltiples métodos dentro de esta clase, lo que indica una necesidad de refactorización.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios descriptivos que explican el propósito de cada método.
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Cita maneja múltiples responsabilidades (creación, eliminación, consulta, verificación), lo que va en contra del SRP.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extensible sin modificar el código existente, lo que puede dificultar futuras extensiones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase Cita depende de implementaciones concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** Podría ser utilizado para encapsular la lógica de creación de citas.
- **Prototipo (+30)**
- **Singleton (+15)** No aplicable si se requiere una única instancia de Cita.

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Podría ser utilizado para simplificar la interacción con métodos relacionados con citas.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)** Podría ser utilizado para manejar las validaciones de citas de manera más flexible.
* **Comando (+20)** Podría ser utilizado para encapsular las acciones relacionadas con citas.
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)** Podría ser utilizado para encapsular diferentes algoritmos de validación de citas.
* **Método Plantilla (+25)** Podría ser utilizado para definir la estructura de los métodos relacionados con citas y permitir que las subclases redefinan ciertos pasos.
* **Visitante (+35)**



Este repositorio fue obtenido de: https://github.com/mbravop/POO-P2-G06