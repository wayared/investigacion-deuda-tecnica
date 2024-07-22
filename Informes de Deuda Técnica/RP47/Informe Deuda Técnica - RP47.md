# Informe de Análisis de Deuda Técnica
## Clase Analizada: EnVenta

### Identificación de Olores de Código

#### Acaparadores
- **Clase Grande (+6):** La clase `EnVenta` contiene tanto los atributos de la entidad como la lógica de validación. Podría beneficiarse de separar la lógica de validación en una clase diferente.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`Integer`, `String`) para representar datos que podrían encapsularse en objetos más significativos.
- **Lista de Parámetros Largos (+4):** El constructor `EnVenta(Integer codigo)` tiene una lista de parámetros larga que podría simplificarse.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase `EnVenta` tiene múltiples razones para cambiar, como cambios en la estructura de la base de datos o en las reglas de validación.
  
#### Dispensables
- **Código duplicado (+7):** La lógica de validación está duplicada en las anotaciones de los atributos y podría beneficiarse de una validación centralizada.
- **Código muerto (+3):** La interfaz `EnVentaCreation` y `EnVentaUpdate` no tienen métodos definidos y podrían considerarse código muerto si no se utilizan en otra parte.

#### Acopladores
- **Envidia de características (+5):** La clase `EnVenta` podría estar accediendo o manipulando directamente atributos de otras clases, lo cual no es evidente en el fragmento proporcionado.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `EnVenta` está manejando tanto la definición de la entidad como la validación de sus atributos. Sería más claro si se separaran estas responsabilidades.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `EnVenta` depende directamente de implementaciones concretas (anotaciones de validación), en lugar de abstracciones, especialmente en la gestión de la lógica de validación.

### Patrones de diseño no utilizados

#### Creacionales
- **Constructor (+25):** Utilizar un constructor más elaborado para simplificar la creación de instancias de `EnVenta`.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para adaptar la clase `EnVenta` a diferentes interfaces de servicios, especialmente si se requiere interactuar con diferentes sistemas.

#### De comportamiento
- **Estado (+30):** Podría permitir que un objeto `EnVenta` altere su comportamiento cuando su estado interno cambia, especialmente en el manejo del atributo `vendido`.
- **Estrategia (+20):** Podría definir diferentes estrategias de validación y encapsular cada una, haciéndolas intercambiables en `EnVenta`.

---

## Clase Analizada: Objeto

### Identificación de Olores de Código

#### Acaparadores
- **Clase Grande (+6):** La clase `Objeto` tiene múltiples responsabilidades, gestionando tanto la información del objeto como su validación.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`Integer`, `String`, `Double`) para representar datos que podrían encapsularse en objetos más significativos.
- **Lista de Parámetros Largos (+4):** El constructor `Objeto(Integer codigo)` tiene una lista de parámetros larga que podría simplificarse.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase `Objeto` tiene múltiples razones para cambiar, como cambios en la estructura de la base de datos o en las reglas de validación.

#### Dispensables
- **Código duplicado (+7):** La lógica de validación está duplicada en las anotaciones de los atributos y podría beneficiarse de una validación centralizada.
- **Código muerto (+3):** La interfaz `ObjetoCreation` y `ObjetoUpdate` no tienen métodos definidos y podrían considerarse código muerto si no se utilizan en otra parte.

#### Acopladores
- **Envidia de características (+5):** La clase `Objeto` podría estar accediendo o manipulando directamente atributos de otras clases, lo cual no es evidente en el fragmento proporcionado.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `Objeto` está manejando tanto la definición de la entidad como la validación de sus atributos. Sería más claro si se separaran estas responsabilidades.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `Objeto` depende directamente de implementaciones concretas (anotaciones de validación), en lugar de abstracciones, especialmente en la gestión de la lógica de validación.

### Patrones de diseño no utilizados

#### Creacionales
- **Constructor (+25):** Utilizar un constructor más elaborado para simplificar la creación de instancias de `Objeto`.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para adaptar la clase `Objeto` a diferentes interfaces de servicios, especialmente si se requiere interactuar con diferentes sistemas.

#### De comportamiento
- **Estado (+30):** Podría permitir que un objeto `Objeto` altere su comportamiento cuando su estado interno cambia, especialmente en el manejo del atributo `descripcion`.
- **Estrategia (+20):** Podría definir diferentes estrategias de validación y encapsular cada una, haciéndolas intercambiables en `Objeto`.

## Clase Analizada: SecuenciaPrimaria

### Identificación de Olores de Código

#### Acaparadores
- **Clase Grande (+6):** La clase `SecuenciaPrimaria` tiene múltiples responsabilidades, incluyendo la definición de la entidad, validación de atributos y la lógica de pre-inserción.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`Long`, `String`, `Integer`) para representar datos que podrían encapsularse en objetos más significativos.
- **Lista de Parámetros Largos (+4):** El constructor `SecuenciaPrimaria(Long codigo, String ciclica, String descripcion, Integer incrementaEn, Long valorActual, Long valorInicial)` tiene una lista de parámetros larga que podría simplificarse.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase `SecuenciaPrimaria` tiene múltiples razones para cambiar, como cambios en la estructura de la base de datos o en las reglas de validación.
  
#### Dispensables
- **Código duplicado (+7):** La lógica de validación está duplicada en las anotaciones de los atributos y podría beneficiarse de una validación centralizada.
- **Código muerto (+3):** La interfaz `SecuenciaPrimariaCreation` y `SecuenciaPrimariaUpdate` no tienen métodos definidos y podrían considerarse código muerto si no se utilizan en otra parte.

#### Acopladores
- **Envidia de características (+5):** La clase `SecuenciaPrimaria` podría estar accediendo o manipulando directamente atributos de otras clases, lo cual no es evidente en el fragmento proporcionado.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `SecuenciaPrimaria` está manejando tanto la definición de la entidad como la validación de sus atributos y la lógica de pre-inserción. Sería más claro si se separaran estas responsabilidades.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `SecuenciaPrimaria` depende directamente de implementaciones concretas (anotaciones de validación), en lugar de abstracciones, especialmente en la gestión de la lógica de validación.

### Patrones de diseño no utilizados

#### Creacionales
- **Constructor (+25):** Utilizar un constructor más elaborado para simplificar la creación de instancias de `SecuenciaPrimaria`.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para adaptar la clase `SecuenciaPrimaria` a diferentes interfaces de servicios, especialmente si se requiere interactuar con diferentes sistemas.

#### De comportamiento
- **Estado (+30):** Podría permitir que un objeto `SecuenciaPrimaria` altere su comportamiento cuando su estado interno cambia, especialmente en el manejo del atributo `ciclica`.
- **Estrategia (+20):** Podría definir diferentes estrategias de validación y encapsular cada una, haciéndolas intercambiables en `SecuenciaPrimaria`.

---

## Clase Analizada: EnVentaController

### Identificación de Olores de Código

#### Acaparadores
- **Método Largo (+5):** Los métodos `ingresar` y `ingresarVarios` tienen más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `EnVentaController` tiene múltiples responsabilidades, como gestionar las solicitudes HTTP, manejar transacciones y validar datos.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`Integer`, `String`, `List<EnVenta>`) para representar datos que podrían encapsularse en objetos más significativos.
- **Lista de Parámetros Largos (+4):** Los métodos `consultarTodos` y `ingresar` tienen listas de parámetros largas que podrían simplificarse.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase `EnVentaController` tiene múltiples razones para cambiar, como cambios en la lógica de transacciones, validación o la estructura de los endpoints.
- **Cirugía de escopeta (+8):** Pequeños cambios en la lógica de negocio o en la estructura de datos pueden requerir modificaciones en múltiples métodos dentro de la clase.

#### Dispensables
- **Comentarios (+2):** Existen muchos comentarios en los métodos que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** La lógica de transacciones y validación está duplicada en los métodos `ingresar` y `ingresarVarios`.
- **Clase de datos (+5):** La clase `EnVentaController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de las transacciones.

#### Acopladores
- **Envidia de características (+5):** Los métodos `ingresar` y `ingresarVarios` utilizan intensivamente métodos de la clase `FuncionesGenerales`.
- **Intimidad inapropiada (+6):** La clase `EnVentaController` accede frecuentemente a métodos y variables privadas de la clase `FuncionesGenerales`.
- **Cadenas de mensajes (+7):** Los métodos `ingresar` y `ingresarVarios` realizan varias llamadas en cadena a métodos de la clase `FuncionesGenerales`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `EnVentaController` tiene múltiples responsabilidades, como gestionar las solicitudes HTTP, manejar transacciones y validar datos.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase `EnVentaController` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `ingresar` y `ingresarVarios`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `EnVentaController` depende directamente de implementaciones concretas (repositorios y clases de utilidades), en lugar de abstracciones, especialmente en la gestión de la lógica de negocio.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de transacciones sin especificar sus clases concretas.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de transacciones y reducir la complejidad en `EnVentaController`.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la interacción con `FuncionesGenerales`.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en el subsistema de transacciones.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de transacción, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud de transacción como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones.
- **Observador (+25):** Podría permitir que un objeto `EnVentaController` notifique a otros objetos sobre cambios en su estado.
- **Estrategia (+20):** Podría definir una familia de algoritmos de validación y encapsular cada uno, haciéndolos intercambiables en `EnVentaController`.



Este repositorio fue obtenido de: https://github.com/JEduardoRT/LP-Kotlin/tree/master/SEGUNDOPROYECTO
