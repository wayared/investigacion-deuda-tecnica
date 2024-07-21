## Clase Analizada: FormularioEstado

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)**:
  - El método `editarEstado(id, estado)` tiene más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6)**:
  - La clase FormularioEstado tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica del formulario y realizar peticiones HTTP.

- **Obsesión Primitiva (+3)**:
  - Uso de tipos primitivos (`id` y `estado`) para representar datos que podrían encapsularse en una clase.

- **Lista de Parámetros Largos (+4)**:
  - El método `editarEstado` podría beneficiarse de un objeto que encapsule los parámetros `id` y `estado`.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5)**:
  - No se identificaron sentencias switch en esta clase.

#### Preventores de Cambio

- **Cambio divergente (+6)**:
  - La clase FormularioEstado tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica del formulario o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8)**:
  - Cambios pequeños en la lógica de manejo de estado requieren modificaciones en múltiples partes del código.

#### Dispensables

- **Comentarios (+2)**:
  - No se identificaron comentarios excesivos en esta clase.

- **Código duplicado (+7)**:
  - No se identificó código duplicado en esta clase.

- **Clase de datos (+5)**:
  - La clase actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.

- **Código muerto (+3)**:
  - No se identificó código muerto en esta clase.

#### Acopladores

- **Envidia de características (+5)**:
  - No se identificó envidia de características en esta clase.

- **Intimidad inapropiada (+6)**:
  - No se identificó acceso inapropiado a métodos y variables privadas de otras clases.

- **Cadenas de mensajes (+7)**:
  - No se identificaron cadenas de mensajes en esta clase.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**:
  - La clase FormularioEstado tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica del formulario.

- **Principio Abierto/Cerrado (OCP) (+40)**:
  - La clase no es fácilmente extensible sin modificar su código fuente, especialmente en el método `editarEstado`.

- **Principio de Inversión de Dependencias (DIP) (+45)**:
  - La clase depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica del formulario.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**:
  - Podría utilizarse para crear diferentes tipos de formularios sin especificar sus clases concretas.

- **Constructor (+25)**:
  - Utilizar un constructor para simplificar la creación de instancias complejas de FormularioEstado.

- **Método de Fábrica (+20)**:
  - Podría usarse para encapsular la creación de estados y reducir la complejidad en FormularioEstado.

#### Estructurales

- **Adaptador (+25)**:
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de estado.

- **Compuesto (+30)**:
  - Podría ser útil para representar jerarquías de estados.

- **Decorador (+25)**:
  - Podría usarse para añadir responsabilidades a objetos de estado de manera dinámica.

- **Fachada (+20)**:
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de manejo de estado.

#### De comportamiento

- **Cadena de Responsabilidad (+30)**:
  - Podría permitir que múltiples objetos manejen una solicitud de cambio de estado, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20)**:
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de cambio de estado.

- **Iterador (+15)**:
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de estados sin exponer su representación subyacente.

- **Mediador (+30)**:
  - Podría reducir las dependencias caóticas entre objetos de la clase FormularioEstado.

- **Observador (+25)**:
  - Podría permitir que un objeto FormularioEstado notifique a otros objetos sobre cambios en su estado.

- **Estado (+30)**:
  - Podría permitir que un objeto FormularioEstado altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20)**:
  - Podría definir una familia de algoritmos de manejo de estado, encapsular cada uno, y hacerlos intercambiables en FormularioEstado.

- **Método Plantilla (+25)**:
  - Podría definir el esqueleto de un algoritmo de manejo de estado en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35)**:
  - Podría separar un algoritmo de manejo de estado de la estructura de objeto sobre la que opera.

## Clase Analizada: SignupForm

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)**:
  - El método `submitForm(event)` tiene más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6)**:
  - La clase `SignupForm` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica del formulario y realizar peticiones HTTP.

- **Obsesión Primitiva (+3)**:
  - Uso de tipos primitivos (`fecha`, `nombre`, `descripcion`, `ubicacion`) para representar datos que podrían encapsularse en una clase.

- **Lista de Parámetros Largos (+4)**:
  - No se identificaron listas de parámetros largos en esta clase.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5)**:
  - No se identificaron sentencias switch en esta clase.

#### Preventores de Cambio

- **Cambio divergente (+6)**:
  - La clase `SignupForm` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica del formulario o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8)**:
  - Cambios pequeños en la lógica de manejo de estado requieren modificaciones en múltiples partes del código.

#### Dispensables

- **Comentarios (+2)**:
  - No se identificaron comentarios excesivos en esta clase.

- **Código duplicado (+7)**:
  - No se identificó código duplicado en esta clase.

- **Clase de datos (+5)**:
  - La clase actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.

- **Código muerto (+3)**:
  - No se identificó código muerto en esta clase.

#### Acopladores

- **Envidia de características (+5)**:
  - No se identificó envidia de características en esta clase.

- **Intimidad inapropiada (+6)**:
  - No se identificó acceso inapropiado a métodos y variables privadas de otras clases.

- **Cadenas de mensajes (+7)**:
  - No se identificaron cadenas de mensajes en esta clase.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**:
  - La clase `SignupForm` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica del formulario.

- **Principio Abierto/Cerrado (OCP) (+40)**:
  - La clase no es fácilmente extensible sin modificar su código fuente, especialmente en el método `submitForm`.

- **Principio de Inversión de Dependencias (DIP) (+45)**:
  - La clase depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica del formulario.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**:
  - Podría utilizarse para crear diferentes tipos de formularios sin especificar sus clases concretas.

- **Constructor (+25)**:
  - Utilizar un constructor para simplificar la creación de instancias complejas de `SignupForm`.

- **Método de Fábrica (+20)**:
  - Podría usarse para encapsular la creación de datos del formulario y reducir la complejidad en `SignupForm`.

#### Estructurales

- **Adaptador (+25)**:
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de datos del formulario.

- **Compuesto (+30)**:
  - Podría ser útil para representar jerarquías de datos del formulario.

- **Decorador (+25)**:
  - Podría usarse para añadir responsabilidades a objetos de datos del formulario de manera dinámica.

- **Fachada (+20)**:
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de manejo de datos del formulario.

#### De comportamiento

- **Cadena de Responsabilidad (+30)**:
  - Podría permitir que múltiples objetos manejen una solicitud de envío de formulario, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20)**:
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de envío de formulario.

- **Iterador (+15)**:
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de datos del formulario sin exponer su representación subyacente.

- **Mediador (+30)**:
  - Podría reducir las dependencias caóticas entre objetos de la clase `SignupForm`.

- **Observador (+25)**:
  - Podría permitir que un objeto `SignupForm` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30)**:
  - Podría permitir que un objeto `SignupForm` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20)**:
  - Podría definir una familia de algoritmos de manejo de datos del formulario, encapsular cada uno, y hacerlos intercambiables en `SignupForm`.

- **Método Plantilla (+25)**:
  - Podría definir el esqueleto de un algoritmo de manejo de datos del formulario en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35)**:
  - Podría separar un algoritmo de manejo de datos del formulario de la estructura de objeto sobre la que opera.


## Clase Analizada: DenunciasManager (script.js)

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)**:
  - Los métodos `procesarDenuncias(denunciasObj)` y `llenarLista()` tienen más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6)**:
  - La clase DenunciasManager tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica del formulario, realizar peticiones HTTP y procesar datos.

- **Obsesión Primitiva (+3)**:
  - Uso de tipos primitivos (`id`, `nombre`, `descripcion`, `ubicacion`, `fecha`, `estado`) para representar datos que podrían encapsularse en una clase.

- **Lista de Parámetros Largos (+4)**:
  - No se identificaron listas de parámetros largos en esta clase.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5)**:
  - No se identificaron sentencias switch en esta clase.

#### Preventores de Cambio

- **Cambio divergente (+6)**:
  - La clase DenunciasManager tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica del formulario o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8)**:
  - Cambios pequeños en la lógica de manejo de estado requieren modificaciones en múltiples partes del código.

#### Dispensables

- **Comentarios (+2)**:
  - No se identificaron comentarios excesivos en esta clase.

- **Código duplicado (+7)**:
  - No se identificó código duplicado en esta clase.

- **Clase de datos (+5)**:
  - La clase actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.

- **Código muerto (+3)**:
  - No se identificó código muerto en esta clase.

#### Acopladores

- **Envidia de características (+5)**:
  - No se identificó envidia de características en esta clase.

- **Intimidad inapropiada (+6)**:
  - No se identificó acceso inapropiado a métodos y variables privadas de otras clases.

- **Cadenas de mensajes (+7)**:
  - No se identificaron cadenas de mensajes en esta clase.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**:
  - La clase DenunciasManager tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica del formulario.

- **Principio Abierto/Cerrado (OCP) (+40)**:
  - La clase no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `procesarDenuncias` y `llenarLista`.

- **Principio de Inversión de Dependencias (DIP) (+45)**:
  - La clase depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica del formulario.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**:
  - Podría utilizarse para crear diferentes tipos de denuncias sin especificar sus clases concretas.

- **Constructor (+25)**:
  - Utilizar un constructor para simplificar la creación de instancias complejas de `DenunciasManager`.

- **Método de Fábrica (+20)**:
  - Podría usarse para encapsular la creación de datos de denuncias y reducir la complejidad en `DenunciasManager`.

#### Estructurales

- **Adaptador (+25)**:
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de datos de denuncias.

- **Compuesto (+30)**:
  - Podría ser útil para representar jerarquías de datos de denuncias.

- **Decorador (+25)**:
  - Podría usarse para añadir responsabilidades a objetos de datos de denuncias de manera dinámica.

- **Fachada (+20)**:
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de manejo de datos de denuncias.

#### De comportamiento

- **Cadena de Responsabilidad (+30)**:
  - Podría permitir que múltiples objetos manejen una solicitud de procesamiento de denuncias, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20)**:
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de procesamiento de denuncias.

- **Iterador (+15)**:
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de datos de denuncias sin exponer su representación subyacente.

- **Mediador (+30)**:
  - Podría reducir las dependencias caóticas entre objetos de la clase `DenunciasManager`.

- **Observador (+25)**:
  - Podría permitir que un objeto `DenunciasManager` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30)**:
  - Podría permitir que un objeto `DenunciasManager` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20)**:
  - Podría definir una familia de algoritmos de manejo de datos de denuncias, encapsular cada uno, y hacerlos intercambiables en `DenunciasManager`.

- **Método Plantilla (+25)**:
  - Podría definir el esqueleto de un algoritmo de manejo de datos de denuncias en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35)**:
  - Podría separar un algoritmo de manejo de datos de denuncias de la estructura de objeto sobre la que opera.




Este repositorio fue obtenido de: https://github.com/CarlosLoorB/FrontendLP
