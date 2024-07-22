# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `Concurso`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `calcularGanador()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `Concurso` tiene múltiples responsabilidades, como gestión de participantes, cálculo de ganadores y manejo de eventos.
- **Obsesión Primitiva (+3):** Se utilizan tipos primitivos para representar entidades complejas, como `fechaInicio` y `fechaFin` en lugar de una clase `Fecha`.
- **Lista de Parámetros Largos (+4):** El método `agregarParticipante(String nombre, int edad, double puntuacion)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `nombre`, `edad` y `puntuacion` en el método `agregarParticipante` siempre se usan juntas y podrían encapsularse en una clase `Participante`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `calcularGanador()` utiliza varias sentencias *switch* para manejar diferentes criterios de cálculo de ganador.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `Concurso` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevos criterios de cálculo o modificar la estructura de participantes.
- **Cirugía de escopeta (+8):** Cambios pequeños en los criterios de cálculo de ganadores requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `calcularGanador()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para agregar participantes se repite en varios lugares de la clase `Concurso`.
- **Clase de datos (+5):** La clase `Concurso` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de participantes.
- **Código muerto (+3):** El método `eliminarParticipante()` no se utiliza en ninguna parte del código.

#### Acopladores

- **Envidia de características (+5):** El método `calcularGanador()` utiliza intensivamente métodos de la clase `Participante`.
- **Intimidad inapropiada (+6):** La clase `Concurso` accede frecuentemente a métodos y variables privadas de la clase `Participante`.
- **Cadenas de mensajes (+7):** El método `calcularGanador()` realiza varias llamadas en cadena a métodos de la clase `Participante`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `Concurso` tiene múltiples responsabilidades, como gestión de participantes, cálculo de ganadores y manejo de eventos.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `Concurso` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `calcularGanador()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `Concurso` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de participantes.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de participantes sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `Concurso`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de participantes y reducir la complejidad en `Concurso`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de participantes.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de objetos de participantes.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de participante de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de concursos.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de cálculo de ganador, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de concurso.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de participantes sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `Concurso`.
- **Observador (+25)** Podría permitir que un objeto `Concurso` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `Concurso` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de cálculo de ganador, encapsular cada uno, y hacerlos intercambiables en `Concurso`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de cálculo de ganador en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de cálculo de ganador de la estructura de objeto `Participante` sobre la que opera.

## Clase Analizada: `Criterio`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `evaluarParticipante()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `Criterio` tiene múltiples responsabilidades, como evaluación de participantes y manejo de diferentes criterios.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como las puntuaciones y los parámetros de evaluación.
- **Lista de Parámetros Largos (+4):** El método `evaluarParticipante(String nombre, int edad, double puntuacion)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `nombre`, `edad` y `puntuacion` en el método `evaluarParticipante` siempre se usan juntas y podrían encapsularse en una clase `Participante`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `evaluarParticipante()` utiliza varias sentencias *switch* para manejar diferentes criterios de evaluación.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `Criterio` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevos criterios de evaluación.
- **Cirugía de escopeta (+8):** Cambios pequeños en los criterios de evaluación requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `evaluarParticipante()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para evaluar participantes se repite en varios lugares de la clase `Criterio`.
- **Clase de datos (+5):** La clase `Criterio` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la evaluación de participantes.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):** El método `evaluarParticipante()` utiliza intensivamente métodos de la clase `Participante`.
- **Intimidad inapropiada (+6):** La clase `Criterio` accede frecuentemente a métodos y variables privadas de la clase `Participante`.
- **Cadenas de mensajes (+7):** El método `evaluarParticipante()` realiza varias llamadas en cadena a métodos de la clase `Participante`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `Criterio` tiene múltiples responsabilidades, como evaluación de participantes y manejo de diferentes criterios.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `Criterio` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `evaluarParticipante()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `Criterio` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la evaluación de participantes.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de criterios sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `Criterio`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de criterios y reducir la complejidad en `Criterio`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la evaluación de participantes.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de criterios de evaluación.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de criterio de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de evaluación de criterios.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de evaluación de participante, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de evaluación.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de criterios sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `Criterio`.
- **Observador (+25)** Podría permitir que un objeto `Criterio` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `Criterio` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de evaluación, encapsular cada uno, y hacerlos intercambiables en `Criterio`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de evaluación en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de evaluación de la estructura de objeto `Participante` sobre la que opera.

## Clase Analizada: `Inscripcion`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `registrarParticipante()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `Inscripcion` tiene múltiples responsabilidades, como registrar participantes, gestionar los detalles de inscripción y manejar los criterios de inscripción.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como fechas y detalles del participante.
- **Lista de Parámetros Largos (+4):** El método `registrarParticipante(String nombre, int edad, String email, String telefono)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `nombre`, `edad`, `email` y `telefono` en el método `registrarParticipante` siempre se usan juntas y podrían encapsularse en una clase `Participante`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `verificarCriterios()` utiliza varias sentencias *switch* para manejar diferentes criterios de verificación.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `Inscripcion` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevos criterios de verificación o modificar la estructura de participantes.
- **Cirugía de escopeta (+8):** Cambios pequeños en los criterios de verificación requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `registrarParticipante()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para registrar participantes se repite en varios lugares de la clase `Inscripcion`.
- **Clase de datos (+5):** La clase `Inscripcion` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de participantes.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):** El método `verificarCriterios()` utiliza intensivamente métodos de la clase `Participante`.
- **Intimidad inapropiada (+6):** La clase `Inscripcion` accede frecuentemente a métodos y variables privadas de la clase `Participante`.
- **Cadenas de mensajes (+7):** El método `verificarCriterios()` realiza varias llamadas en cadena a métodos de la clase `Participante`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `Inscripcion` tiene múltiples responsabilidades, como registrar participantes, gestionar los detalles de inscripción y manejar los criterios de inscripción.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `Inscripcion` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `verificarCriterios()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `Inscripcion` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de participantes.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de criterios de inscripción sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `Inscripcion`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de participantes y criterios de inscripción, reduciendo la complejidad en `Inscripcion`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de participantes.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de criterios de inscripción.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de criterio de inscripción de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de inscripción.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de verificación de criterios, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de inscripción.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de criterios de inscripción sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `Inscripcion`.
- **Observador (+25)** Podría permitir que un objeto `Inscripcion` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `Inscripcion` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de verificación de criterios, encapsular cada uno, y hacerlos intercambiables en `Inscripcion`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de verificación de criterios en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de verificación de criterios de la estructura de objeto `Participante` sobre la que opera.

## Clase Analizada: `MiembroJurado`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `evaluarParticipante()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `MiembroJurado` tiene múltiples responsabilidades, como evaluar participantes y gestionar los detalles del jurado.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como puntuaciones y criterios de evaluación.
- **Lista de Parámetros Largos (+4):** El método `evaluarParticipante(String nombre, int edad, double puntuacion)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `nombre`, `edad` y `puntuacion` en el método `evaluarParticipante` siempre se usan juntas y podrían encapsularse en una clase `Participante`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `evaluarParticipante()` utiliza varias sentencias *switch* para manejar diferentes criterios de evaluación.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `MiembroJurado` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevos criterios de evaluación o modificar la estructura de los miembros del jurado.
- **Cirugía de escopeta (+8):** Cambios pequeños en los criterios de evaluación requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `evaluarParticipante()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para evaluar participantes se repite en varios lugares de la clase `MiembroJurado`.
- **Clase de datos (+5):** La clase `MiembroJurado` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de los miembros del jurado.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):** El método `evaluarParticipante()` utiliza intensivamente métodos de la clase `Participante`.
- **Intimidad inapropiada (+6):** La clase `MiembroJurado` accede frecuentemente a métodos y variables privadas de la clase `Participante`.
- **Cadenas de mensajes (+7):** El método `evaluarParticipante()` realiza varias llamadas en cadena a métodos de la clase `Participante`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `MiembroJurado` tiene múltiples responsabilidades, como evaluar participantes y gestionar los detalles del jurado.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `MiembroJurado` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `evaluarParticipante()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `MiembroJurado` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la evaluación de participantes.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de criterios de evaluación sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `MiembroJurado`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de criterios de evaluación y reducir la complejidad en `MiembroJurado`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la evaluación de participantes.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de criterios de evaluación.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de criterio de evaluación de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de evaluación.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de evaluación de participante, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de evaluación.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de criterios de evaluación sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `MiembroJurado`.
- **Observador (+25)** Podría permitir que un objeto `MiembroJurado` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `MiembroJurado` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de evaluación, encapsular cada uno, y hacerlos intercambiables en `MiembroJurado`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de evaluación en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de evaluación de la estructura de objeto `Participante` sobre la que opera.

---

Este repositorio fue obtenido de: [https://github.com/rochardp12/proyecto]()
