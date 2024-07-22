
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `InterfazAtencion`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** El método `mostrarInterfazAtencion()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `InterfazAtencion` tiene múltiples responsabilidades, como gestión de atenciones, manejo de citas y empleados.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos para representar entidades complejas, como fechas, en lugar de una clase `Fecha`.
- **Lista de Parámetros Largos (+4):** El método `validarFecha(int mes, int dia, int anio)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `mes`, `dia` y `anio` en el método `validarFecha` siempre se usan juntas y podrían encapsularse en una clase `Fecha`.
 
#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `mostrarInterfazAtencion()` utiliza varias sentencias switch para manejar diferentes opciones de menú.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `InterfazAtencion` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevas funcionalidades o modificar la lógica existente.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de atenciones requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `mostrarInterfazAtencion()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para manejar opciones de menú se repite en varios lugares de la clase `InterfazAtencion`.
- **Clase de datos (+5):** La clase `InterfazAtencion` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de atenciones.
- **Código muerto (+3):** El método `opcionInvalida()` no se utiliza en ninguna parte del código.

#### Acopladores

- **Envidia de características (+5):** El método `mostrarInterfazAtencion`() utiliza intensivamente métodos de la clase `Cita` y `Empleado`.
- **Intimidad inapropiada (+6):** La clase `InterfazAtencion` accede frecuentemente a métodos y variables privadas de la clase `Cita` y `Empleado`.
- **Cadenas de mensajes (+7):** El método `mostrarInterfazAtencion()` realiza varias llamadas en cadena a métodos de las clases `Cita` y `Empleado`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `InterfazAtencion` tiene múltiples responsabilidades, como gestión de atenciones, manejo de citas y empleados.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `InterfazAtencion` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `mostrarInterfazAtencion()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `InterfazAtencion` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de atenciones y citas.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de atenciones sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `InterfazAtencion`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de atenciones y reducir la complejidad en `InterfazAtencion`.

#### Estructurales

* **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de atenciones.
* **Compuesto (+30)** Podría ser útil para representar jerarquías de objetos de atenciones.
* **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de atención de manera dinámica.
* **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de atenciones.

#### De comportamiento

* **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de atención, evitando el acoplamiento entre el emisor y el receptor.
* **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de atención.
* **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de atenciones sin exponer su representación subyacente.
* **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `InterfazAtencion`.
* **Observador (+25)** Podría permitir que un objeto `InterfazAtencion` notifique a otros objetos sobre cambios en su estado.
* **Estado (+30)** Podría permitir que un objeto `InterfazAtencion` altere su comportamiento cuando su estado interno cambia.
* **Estrategia (+20)** Podría definir una familia de algoritmos de gestión de atenciones, encapsular cada uno, y hacerlos intercambiables en `InterfazAtencion`.
* **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de gestión de atenciones en una operación, dejando algunos pasos a las subclases.
* **Visitante (+35)** Podría separar un algoritmo de gestión de atenciones de la estructura de objeto `Atencion` sobre la que opera.

## Clase Analizada: `InterfazEmpleado`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `mostrarInterfazEmpleado()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `InterfazEmpleado` tiene múltiples responsabilidades, como gestión de empleados, edición y eliminación de empleados.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos para representar entidades complejas, como `cedula`, `nombre`, `telefono` y `email` en lugar de clases específicas para cada entidad.
- **Lista de Parámetros Largos (+4):** El método `agregarEmpleado()` solicita múltiples parámetros, lo cual podría simplificarse.
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `mostrarInterfazEmpleado()` utiliza varias sentencias switch para manejar diferentes opciones de menú.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `InterfazEmpleado` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevas funcionalidades o modificar la lógica existente.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de manejo de empleados requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en los métodos que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para manejar opciones de menú y validaciones se repite en varios lugares de la clase `InterfazEmpleado`.
- **Clase de datos (+5):** La clase `InterfazEmpleado` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de empleados.

#### Acopladores

- **Envidia de características (+5):** Los métodos `mostrarInterfazEmpleado()`, `agregarEmpleado()`, `editarEmpleado()` y `eliminarEmpleado()` utilizan intensivamente métodos de la clase Empleado.
- **Intimidad inapropiada (+6):** La clase `InterfazEmpleado` accede frecuentemente a métodos y variables privadas de la clase `Empleado`.
- **Cadenas de mensajes (+7):** El método `mostrarInterfazEmpleado()` realiza varias llamadas en cadena a métodos de la clase `Empleado`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `InterfazEmpleado` tiene múltiples responsabilidades, como gestión de empleados, edición y eliminación de empleados.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `InterfazEmpleado` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `mostrarInterfazEmpleado()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `InterfazEmpleado` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de empleados.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de empleados sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `InterfazEmpleado`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de empleados y reducir la complejidad en `InterfazEmpleado`.

#### Estructurales

* **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de empleados.
* **Compuesto (+30)** Podría ser útil para representar jerarquías de objetos de empleados.
* **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de empleado de manera dinámica.
* **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de empleados.

#### De comportamiento

* **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de manejo de empleados, evitando el acoplamiento entre el emisor y el receptor.
* **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de manejo de empleados.
* **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de empleados sin exponer su representación subyacente.
* **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `InterfazEmpleado`.
* **Observador (+25)** Podría permitir que un objeto `InterfazEmpleado` notifique a otros objetos sobre cambios en su estado.
* **Estado (+30)** Podría permitir que un objeto `InterfazEmpleado` altere su comportamiento cuando su estado interno cambia.
* **Estrategia (+20)** Podría definir una familia de algoritmos de gestión de empleados, encapsular cada uno, y hacerlos intercambiables en `InterfazEmpleado`.
* **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de gestión de empleados en una operación, dejando algunos pasos a las subclases.
* **Visitante (+35)** Podría separar un algoritmo de gestión de empleados de la estructura de objeto `Empleado` sobre la que opera.

## Clase Analizada: `InterfazCita`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `mostrarInterfazCita()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `InterfazCita` tiene múltiples responsabilidades, como creación, eliminación y consulta de citas.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos para representar entidades complejas, como fecha y hora, en lugar de una clase específica.
- **Lista de Parámetros Largos (+4):** El método `crearCita()` solicita múltiples parámetros, lo cual podría simplificarse.
- **Grupos de Datos (+3):** Las variables `anio`, `mes`, `dia`, `hora` y `min` en el método crearCita siempre se usan juntas y podrían encapsularse en una clase `Fecha`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `mostrarInterfazCita()` utiliza varias sentencias switch para manejar diferentes opciones de menú.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase InterfazCita tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevas funcionalidades o modificar la lógica existente.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de manejo de citas requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en los métodos que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para manejar opciones de menú y validaciones se repite en varios lugares de la clase InterfazCita.
- **Clase de datos (+5):** La clase InterfazCita actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de citas.
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):** Los métodos crearCita(), eliminarCita() y consultarCitas() utilizan intensivamente métodos de otras clases como Cliente, Empleado, Servicio y Cita.
- **Intimidad inapropiada (+6):** La clase InterfazCita accede frecuentemente a métodos y variables privadas de las clases Cliente, Empleado, Servicio y Cita.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** El método crearCita() realiza varias llamadas en cadena a métodos de las clases Cliente, Empleado, Servicio y Cita.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase InterfazCita tiene múltiples responsabilidades, como creación, eliminación y consulta de citas.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase InterfazCita no es fácilmente extensible sin modificar su código fuente, especialmente en el método mostrarInterfazCita().
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase InterfazCita depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de citas.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de citas sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de InterfazCita.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de citas y reducir la complejidad en InterfazCita.
- **Prototipo (+30)** 
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de citas.
* **Puente (+35)**
* **Compuesto (+30)** Podría ser útil para representar jerarquías de objetos de citas.
* **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de cita de manera dinámica.
* **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de citas.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de manejo de citas, evitando el acoplamiento entre el emisor y el receptor.
* **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de manejo de citas.
* **Intérprete (+40)**
* **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de citas sin exponer su representación subyacente.
* **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase InterfazCita.
* **Memento (+35)**
* **Observador (+25)** Podría permitir que un objeto InterfazCita notifique a otros objetos sobre cambios en su estado.
* **Estado (+30)** Podría permitir que un objeto InterfazCita altere su comportamiento cuando su estado interno cambia.
* **Estrategia (+20)** Podría definir una familia de algoritmos de gestión de citas, encapsular cada uno, y hacerlos intercambiables en InterfazCita.
* **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de gestión de citas en una operación, dejando algunos pasos a las subclases.
* **Visitante (+35)** Podría separar un algoritmo de gestión de citas de la estructura de objeto Cita sobre la que opera.

## Clase Analizada: `InterfazCliente`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método mostrarInterfazClientes() tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase InterfazCliente tiene múltiples responsabilidades, como agregar, editar y mostrar clientes.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos para representar entidades complejas, como teléfono y email, en lugar de una clase específica.
- **Lista de Parámetros Largos (+4):** El método agregarCliente() solicita múltiples parámetros, lo cual podría simplificarse.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método mostrarInterfazClientes() utiliza varias sentencias switch para manejar diferentes opciones de menú.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase puede necesitar cambios frecuentes si se agregan o modifican funcionalidades de la interfaz del cliente.
- **Cirugía de escopeta (+8):** Cambios en los datos del cliente pueden requerir cambios en múltiples lugares.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):** Las estructuras de switch en editarCliente() pueden ser consideradas como código duplicado en menor medida.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):** Algunos métodos están muy acoplados con la clase Cliente.
- **Intimidad inapropiada (+6):** La clase InterfazCliente accede directamente a los detalles de Cliente.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase InterfazCliente tiene múltiples responsabilidades (mostrar, agregar, editar clientes).
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no es fácilmente extensible sin modificar su código.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)** No aplica directamente, pero la interfaz de la clase podría beneficiarse de ser dividida.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase InterfazCliente depende directamente de la clase Cliente.

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
* **Comando (+20)** Podría ser utilizado para las acciones de agregar y editar clientes.
* **Intérprete (+40)** No utilizado.
* **Iterador (+15)** No utilizado.
* **Mediador (+30)** No utilizado.
* **Memento (+35)** No utilizado.
* **Observador (+25)** No utilizado.
* **Estado (+30)** No utilizado.
* **Estrategia (+20)** No utilizado.
* **Método Plantilla (+25)** No utilizado.
* **Visitante (+35)** No utilizado.



Este repositorio fue obtenido de: https://github.com/sAngello31/POO-P1-G04