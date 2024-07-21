# Informe de Análisis de Deuda Técnica

## Clase Analizada: `Juego`

### Identificación de Olores de Código

#### Acaparadores

- **Clase Grande (+6):**
  - La clase `Juego` tiene múltiples responsabilidades, incluyendo la gestión de jugadores, configuración, mazo, y alineación.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos como la fecha (`String fecha`) y duración (`int duracion`), donde se podría usar una clase `Date` para la fecha y una clase `Duration` para la duración.

- **Cambio divergente (+6):**
  - La clase `Juego` tiene múltiples razones para cambiar, debido a su alto número de responsabilidades.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica del juego o la configuración pueden requerir modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Clase de datos (+5):**
  - La clase `Juego` actúa en gran medida como una estructura de datos sin comportamiento significativo en algunos aspectos.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - La clase `Juego` accede frecuentemente a métodos y variables privadas de otras clases como `Mazo` y `Alineacion`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
  - La clase `Juego` tiene múltiples responsabilidades, como gestionar jugadores, configuración, mazo, y alineación.

- **Principio Abierto/Cerrado (OCP) (+40)**
  - La clase `Juego` no es fácilmente extensible sin modificar su código fuente, especialmente en la gestión de la alineación y configuración del juego.

- **Principio de Inversión de Dependencias (DIP) (+45)**
  - La clase `Juego` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de mazo y alineación.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
  - Podría utilizarse para crear diferentes configuraciones de juego sin especificar sus clases concretas.

- **Constructor (+25)**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `Juego`.

- **Método de Fábrica (+20)**
  - Podría usarse para encapsular la creación de mazos y alineaciones y reducir la complejidad en `Juego`.

#### Estructurales

- **Adaptador (+25)**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de cartas y jugadores.

- **Compuesto (+30)**
  - Podría ser útil para representar jerarquías de cartas jugadas o jugadores.

- **Decorador (+25)**
  - Podría usarse para añadir responsabilidades a objetos de `Configuracion` de manera dinámica.

- **Fachada (+20)**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de juego.

#### De comportamiento

- **Cadena de Responsabilidad (+30)**
  - Podría permitir que múltiples objetos manejen una solicitud de gestión de juego, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20)**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de gestión de juego.

- **Iterador (+15)**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de jugadores sin exponer su representación subyacente.

- **Mediador (+30)**
  - Podría reducir las dependencias caóticas entre objetos de la clase `Juego`.

- **Observador (+25)**
  - Podría permitir que un objeto `Juego` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30)**
  - Podría permitir que un objeto `Juego` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20)**
  - Podría definir una familia de algoritmos de gestión de juego, encapsular cada uno, y hacerlos intercambiables en `Juego`.

- **Método Plantilla (+25)**
  - Podría definir el esqueleto de un algoritmo de gestión de juego en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35)**
  - Podría separar un algoritmo de gestión de juego de la estructura de objeto `Jugador` sobre la que opera.

## Clase Analizada: `ReporteController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
  - No se han identificado métodos largos en la clase `ReporteController`.

- **Clase Grande (+6):**
  - La clase `ReporteController` gestiona la interfaz de usuario, inicializa una tabla de reporte y maneja eventos de botones.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - No se han identificado sentencias switch en la clase `ReporteController`.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `ReporteController` tiene múltiples razones para cambiar, debido a su alto número de responsabilidades, como la gestión de la interfaz de usuario y la generación de reportes.

#### Dispensables

- **Clase de datos (+5):**
  - La clase interna `JuegoReporte` actúa en gran medida como una estructura de datos sin comportamiento significativo.

#### Acopladores

- **Envidia de características (+5):**
  - No se han identificado métodos que utilicen intensivamente métodos de otra clase.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
  - La clase `ReporteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y generar reportes de juegos.

- **Principio Abierto/Cerrado (OCP) (+40)**
  - La clase `ReporteController` no es fácilmente extensible sin modificar su código fuente, especialmente en la gestión de la tabla de reportes.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
  - Podría utilizarse para crear diferentes configuraciones de reportes sin especificar sus clases concretas.

#### Estructurales

- **Adaptador (+25)**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de datos de juegos y su representación en la interfaz.

- **Compuesto (+30)**
  - Podría ser útil para representar jerarquías de reportes o juegos.

- **Decorador (+25)**
  - Podría usarse para añadir responsabilidades a objetos de `JuegoReporte` de manera dinámica.

- **Fachada (+20)**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de reportes.

#### De comportamiento

- **Cadena de Responsabilidad (+30)**
  - Podría permitir que múltiples objetos manejen una solicitud de generación de reportes, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20)**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de generación de reportes.

- **Iterador (+15)**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de juegos sin exponer su representación subyacente.

- **Mediador (+30)**
  - Podría reducir las dependencias caóticas entre objetos de la clase `ReporteController`.

- **Observador (+25)**
  - Podría permitir que un objeto `ReporteController` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30)**
  - Podría permitir que un objeto `ReporteController` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20)**
  - Podría definir una familia de algoritmos de generación de reportes, encapsular cada uno, y hacerlos intercambiables en `ReporteController`.

- **Método Plantilla (+25)**
  - Podría definir el esqueleto de un algoritmo de generación de reportes en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35)**
  - Podría separar un algoritmo de generación de reportes de la estructura de objeto `Juego` sobre la que opera.


## Clase Analizada: `Jugador`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
  - El método `verificarTablero` es largo y complejo, con múltiples bloques de lógica para diferentes alineaciones.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - El método `verificarTablero` utiliza varias sentencias switch para manejar diferentes tipos de alineaciones (FILA, COLUMNA, ESQUINA).

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `Jugador` podría tener múltiples razones para cambiar, especialmente si se agregan nuevas reglas de verificación de tablero o se modifican las existentes.

#### Dispensables

- **Clase de datos (+5):**
  - No se han identificado clases de datos sin comportamiento significativo en la clase `Jugador`.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - No se ha identificado intimidad inapropiada en la clase `Jugador`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
  - La clase `Jugador` tiene múltiples responsabilidades, como gestionar el nombre del jugador y verificar el tablero.

- **Principio Abierto/Cerrado (OCP) (+40)**
  - La clase `Jugador` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `verificarTablero`.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
  - Podría utilizarse para crear diferentes configuraciones de `Tablero` sin especificar sus clases concretas.

#### Estructurales

- **Adaptador (+25)**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de las cartas en el tablero.

- **Compuesto (+30)**
  - Podría ser útil para representar jerarquías de cartas en el tablero.

- **Decorador (+25)**
  - Podría usarse para añadir responsabilidades a objetos de `Tablero` de manera dinámica.

- **Fachada (+20)**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de tableros.

#### De comportamiento

- **Cadena de Responsabilidad (+30)**
  - Podría permitir que múltiples objetos manejen una solicitud de verificación de tablero, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20)**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de verificación de tablero.

- **Iterador (+15)**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de cartas en el tablero sin exponer su representación subyacente.

- **Mediador (+30)**
  - Podría reducir las dependencias caóticas entre objetos de la clase `Jugador`.

- **Observador (+25)**
  - Podría permitir que un objeto `Jugador` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30)**
  - Podría permitir que un objeto `Jugador` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20)**
  - Podría definir una familia de algoritmos de verificación de tablero, encapsular cada uno, y hacerlos intercambiables en `Jugador`.

- **Método Plantilla (+25)**
  - Podría definir el esqueleto de un algoritmo de verificación de tablero en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35)**
  - Podría separar un algoritmo de verificación de tablero de la estructura de objeto `Tablero` sobre la que opera.


## Clase Analizada: `Contador`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
  - No se han identificado métodos largos en la clase `Contador`.

- **Clase Grande (+6):**
  - No se han identificado múltiples responsabilidades en la clase `Contador`.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - No se han identificado sentencias switch en la clase `Contador`.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - No se han identificado múltiples razones para cambiar en la clase `Contador`.

#### Dispensables

- **Clase de datos (+5):**
  - No se han identificado clases de datos sin comportamiento significativo en la clase `Contador`.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - No se ha identificado intimidad inapropiada en la clase `Contador`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
  - La clase `Contador` tiene la responsabilidad de gestionar el tiempo del juego, lo cual es una única responsabilidad clara.

- **Principio Abierto/Cerrado (OCP) (+40)**
  - La clase `Contador` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `run`.

- **Principio de Inversión de Dependencias (DIP) (+45)**
  - La clase `Contador` depende directamente de la implementación concreta de `Juego` en lugar de una abstracción.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
  - Podría utilizarse para crear diferentes configuraciones de `Juego` sin especificar sus clases concretas.

#### Estructurales

- **Adaptador (+25)**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión del tiempo del juego.

#### De comportamiento

- **Comando (+20)**
  - Podría encapsular la acción de incrementar el tiempo del juego como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones.

- **Estado (+30)**
  - Podría permitir que un objeto `Contador` altere su comportamiento cuando el estado del juego cambia (e.g., el juego termina).

- **Estrategia (+20)**
  - Podría definir una familia de algoritmos de gestión del tiempo del juego, encapsular cada uno, y hacerlos intercambiables en `Contador`.

- **Método Plantilla (+25)**
  - Podría definir el esqueleto de un algoritmo de gestión del tiempo del juego en una operación, dejando algunos pasos a las subclases.




Este repositorio fue obtenido de: https://github.com/JEduardoRT/PROYECTOPOO-P2-G2
