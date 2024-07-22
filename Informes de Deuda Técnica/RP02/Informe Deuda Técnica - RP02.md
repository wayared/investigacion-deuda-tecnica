# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `PantallaEvaluacionController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `iniciarEvaluacion()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `PantallaEvaluacionController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de evaluación.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como los detalles de la evaluación y parámetros de la interfaz.
- **Lista de Parámetros Largos (+4):** El método `evaluarParticipante(String nombre, int edad, double puntuacion, String criterio)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `nombre`, `edad`, `puntuacion` y `criterio` en el método `evaluarParticipante` siempre se usan juntas y podrían encapsularse en una clase `Participante`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `evaluarParticipante()` utiliza varias sentencias *switch* para manejar diferentes criterios de evaluación.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `PantallaEvaluacionController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de evaluación o actualizar la interfaz de usuario.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de evaluación requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `iniciarEvaluacion()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para evaluar participantes se repite en varios lugares de la clase `PantallaEvaluacionController`.
- **Clase de datos (+5):** La clase `PantallaEvaluacionController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):** El método `evaluarParticipante()` utiliza intensivamente métodos de la clase `Participante`.
- **Intimidad inapropiada (+6):** La clase `PantallaEvaluacionController` accede frecuentemente a métodos y variables privadas de la clase `Participante`.
- **Cadenas de mensajes (+7):** El método `evaluarParticipante()` realiza varias llamadas en cadena a métodos de la clase `Participante`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `PantallaEvaluacionController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de evaluación.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `PantallaEvaluacionController` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `evaluarParticipante()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `PantallaEvaluacionController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de evaluación.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de criterios de evaluación sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `PantallaEvaluacionController`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de criterios de evaluación y reducir la complejidad en `PantallaEvaluacionController`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la evaluación de participantes.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de criterios de evaluación.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de criterio de evaluación de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de evaluación.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de evaluación de participante, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de evaluación.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de criterios de evaluación sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `PantallaEvaluacionController`.
- **Observador (+25)** Podría permitir que un objeto `PantallaEvaluacionController` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `PantallaEvaluacionController` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de evaluación, encapsular cada uno, y hacerlos intercambiables en `PantallaEvaluacionController`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de evaluación en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de evaluación de la estructura de objeto `Participante` sobre la que opera.

## Clase Analizada: `Premio`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `calcularValorPremio()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `Premio` tiene múltiples responsabilidades, como gestionar los detalles del premio y calcular su valor.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como el valor y las características del premio.
- **Lista de Parámetros Largos (+4):** El método `calcularValorPremio(String tipo, double monto, String descripcion)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `tipo`, `monto` y `descripcion` en el método `calcularValorPremio` siempre se usan juntas y podrían encapsularse en una clase `DetallePremio`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `calcularValorPremio()` utiliza varias sentencias *switch* para manejar diferentes tipos de premios.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `Premio` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevos tipos de premios o modificar la estructura de los premios existentes.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de cálculo del premio requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `calcularValorPremio()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para calcular el valor del premio se repite en varios lugares de la clase `Premio`.
- **Clase de datos (+5):** La clase `Premio` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de los detalles del premio.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):** El método `calcularValorPremio()` utiliza intensivamente métodos de la clase `DetallePremio`.
- **Intimidad inapropiada (+6):** La clase `Premio` accede frecuentemente a métodos y variables privadas de la clase `DetallePremio`.
- **Cadenas de mensajes (+7):** El método `calcularValorPremio()` realiza varias llamadas en cadena a métodos de la clase `DetallePremio`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `Premio` tiene múltiples responsabilidades, como gestionar los detalles del premio y calcular su valor.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `Premio` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `calcularValorPremio()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `Premio` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de los detalles del premio.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de premios sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `Premio`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de detalles del premio y reducir la complejidad en `Premio`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de detalles del premio.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de premios.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de detalle del premio de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de premios.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de cálculo del valor del premio, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de cálculo del premio.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de detalles del premio sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `Premio`.
- **Observador (+25)** Podría permitir que un objeto `Premio` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `Premio` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de cálculo del valor del premio, encapsular cada uno, y hacerlos intercambiables en `Premio`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de cálculo del valor del premio en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de cálculo del valor del premio de la estructura de objeto `DetallePremio` sobre la que opera.

## Clase Analizada: `Mascota`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `mostrarDetalles()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `Mascota` tiene múltiples responsabilidades, como gestionar los detalles de la mascota y mostrar la información de la mascota.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como edad y características de la mascota.
- **Lista de Parámetros Largos (+4):** El método `registrarMascota(String nombre, int edad, String raza, String color)` tiene una lista de parámetros larga.
- **Grupos de Datos (+3):** Las variables `nombre`, `edad`, `raza` y `color` en el método `registrarMascota` siempre se usan juntas y podrían encapsularse en una clase `DetalleMascota`.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** El método `mostrarDetalles()` utiliza varias sentencias *switch* para manejar diferentes tipos de detalles.

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase `Mascota` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como agregar nuevos tipos de detalles o modificar la estructura de los detalles existentes.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de detalles requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):** Existen muchos comentarios en el método `mostrarDetalles()` que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para mostrar detalles de la mascota se repite en varios lugares de la clase `Mascota`.
- **Clase de datos (+5):** La clase `Mascota` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de los detalles de la mascota.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):** El método `mostrarDetalles()` utiliza intensivamente métodos de la clase `DetalleMascota`.
- **Intimidad inapropiada (+6):** La clase `Mascota` accede frecuentemente a métodos y variables privadas de la clase `DetalleMascota`.
- **Cadenas de mensajes (+7):** El método `mostrarDetalles()` realiza varias llamadas en cadena a métodos de la clase `DetalleMascota`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase `Mascota` tiene múltiples responsabilidades, como gestionar los detalles de la mascota y mostrar la información de la mascota.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase `Mascota` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `mostrarDetalles()`.
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase `Mascota` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de los detalles de la mascota.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)** Podría utilizarse para crear diferentes tipos de detalles de mascota sin especificar sus clases concretas.
- **Constructor (+25)** Utilizar un constructor para simplificar la creación de instancias complejas de `Mascota`.
- **Método de Fábrica (+20)** Podría usarse para encapsular la creación de detalles de mascota y reducir la complejidad en `Mascota`.

#### Estructurales

- **Adaptador (+25)** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de detalles de la mascota.
- **Compuesto (+30)** Podría ser útil para representar jerarquías de detalles de mascota.
- **Decorador (+25)** Podría usarse para añadir responsabilidades a objetos de detalle de mascota de manera dinámica.
- **Fachada (+20)** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de detalles de mascotas.

#### De comportamiento

- **Cadena de Responsabilidad (+30)** Podría permitir que múltiples objetos manejen una solicitud de mostrar detalles de la mascota, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de detalles de la mascota.
- **Iterador (+15)** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de detalles de mascota sin exponer su representación subyacente.
- **Mediador (+30)** Podría reducir las dependencias caóticas entre objetos de la clase `Mascota`.
- **Observador (+25)** Podría permitir que un objeto `Mascota` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)** Podría permitir que un objeto `Mascota` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)** Podría definir una familia de algoritmos de mostrar detalles, encapsular cada uno, y hacerlos intercambiables en `Mascota`.
- **Método Plantilla (+25)** Podría definir el esqueleto de un algoritmo de mostrar detalles en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)** Podría separar un algoritmo de mostrar detalles de la estructura de objeto `DetalleMascota` sobre la que opera.

## Clase Analizada: `App`

### Identificación de Olores de Código

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase tiene múltiples razones para cambiar, como la modificación de la lógica de inicialización o cambios en la interfaz de usuario.
- **Cirugía de escopeta (+8):** Cualquier cambio en la lógica de inicio puede requerir modificaciones en múltiples métodos relacionados.

### Violaciones de los Principios SOLID

- **Principio Abierto/Cerrado (OCP) (+40)** La clase no es fácilmente extensible sin modificar su código fuente, especialmente si se quiere cambiar la lógica de carga de FXML o la configuración de la escena.

### Patrones de diseño no utilizados

#### Creacionales

- **Método de Fábrica (+20)** Podría encapsular la creación de objetos `FXMLLoader` para reducir la complejidad en `App`.

#### Estructurales

- **Fachada (+20)** Podría proporcionar una interfaz simplificada para la gestión de la interfaz de usuario y la carga de escenas.

Este repositorio fue obtenido de: [https://github.com/rochardp12/ProyectoPOO-2Parcial]()
