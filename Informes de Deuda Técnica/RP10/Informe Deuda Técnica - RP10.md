
# Informe de Análisis de Deuda Técnica

## Malos Olores de Código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `RegistrarResidenteController`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo (+5):** El método `registrarResidente()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `RegistrarResidenteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de registro de residentes.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como los detalles del residente (nombre, correo, género, cédula).
- **Lista de Parámetros Largos (+4):** El método `registrarResidente()` podría tener parámetros encapsulados en una clase `Residente` o similar.
- **Grupos de Datos (+3):** Las variables `nombre`, `correo`, `genero` y `cedula` en el método `registrarResidente()` siempre se usan juntas y podrían encapsularse en una clase `Residente`.

**Abusadores de Orientación a Objetos**

- **Sentencias Switch (+5):** No se identificaron sentencias switch en la clase.

**Preventores de Cambio**

- **Cambio divergente (+6):** La clase `RegistrarResidenteController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de registro o actualizar la interfaz de usuario.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de registro de residentes requieren modificaciones en múltiples métodos y clases relacionadas.

**Dispensables**

- **Comentarios (+2):** Existen comentarios en la clase que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** La lógica para verificar y registrar un residente se repite en varios lugares de la clase.
- **Clase de datos (+5):** La clase `RegistrarResidenteController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.
- **Código muerto (+3):** No se identificaron métodos y variables no utilizados.

**Acopladores**

- **Envidia de características (+5):** El método `registrarResidente()` utiliza intensivamente métodos de la clase `Residente`.
- **Intimidad inapropiada (+6):** La clase `RegistrarResidenteController` accede frecuentemente a métodos y variables privadas de la clase `Residente`.
- **Cadenas de mensajes (+7):** El método `registrarResidente()` realiza varias llamadas en cadena a métodos de la clase `Residente`.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `RegistrarResidenteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de registro.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase `RegistrarResidenteController` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `registrarResidente()`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `RegistrarResidenteController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de registro.

#### Patrones de diseño no utilizados

**Creacionales**

- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de residentes sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de `RegistrarResidenteController`.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de residentes y reducir la complejidad en `RegistrarResidenteController`.

**Estructurales**

- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el registro de residentes.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de residentes.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de residente de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de registro.

**De comportamiento**

- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de registro de residente, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de registro.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de residentes sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase `RegistrarResidenteController`.
- **Observador (+25):** Podría permitir que un objeto `RegistrarResidenteController` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto `RegistrarResidenteController` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de registro, encapsular cada uno, y hacerlos intercambiables en `RegistrarResidenteController`.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de registro en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de registro de la estructura de objeto `Residente` sobre la que opera.


### Clase Analizada: `PrincipalController`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo:** No se identificaron métodos largos en esta clase, ya que todos los métodos tienen una longitud manejable.
- **Clase Grande:** La clase `PrincipalController` es relativamente pequeña y maneja principalmente la navegación de la interfaz de usuario, por lo que no se considera una clase grande.
- **Obsesión Primitiva:** No se identificaron obsesiones primitivas en esta clase.
- **Lista de Parámetros Largos:** No se identificaron listas de parámetros largos en esta clase.
- **Grupos de Datos:** La clase `PrincipalController` no presenta grupos de datos que siempre se usen juntos y que podrían encapsularse.

**Preventores de Cambio**

- **Cambio divergente:** La clase `PrincipalController` tiene una única responsabilidad clara: manejar la navegación de la interfaz de usuario. No se identificaron cambios divergentes.
- **Cirugía de escopeta:** No se identificaron cambios pequeños que requieran modificaciones en múltiples métodos y clases relacionadas.

**Dispensables**

- **Comentarios (+2):** Existen comentarios generados automáticamente por el IDE que podrían eliminarse para mejorar la claridad del código.
- **Código muerto (+3):** La variable `casas` parece ser inicializada pero nunca utilizada. Esto puede considerarse código muerto.

**Acopladores**

- **Envidia de características:** No se identificó envidia de características en esta clase.
- **Intimidad inapropiada:** No se identificó intimidad inapropiada en esta clase.
- **Cadenas de mensajes:** No se identificaron cadenas de mensajes en esta clase.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+10):** La clase `PrincipalController` tiene una única responsabilidad clara: manejar la navegación de la interfaz de usuario. Sin embargo, la inicialización de la lista de casas puede ser considerada fuera de su responsabilidad principal.
- **Principio Abierto/Cerrado (OCP) (+10):** La clase `PrincipalController` no es fácilmente extensible sin modificar su código fuente. Por ejemplo, si se agregan más funcionalidades de navegación, se necesitarían modificar los métodos existentes.
- **Principio de Inversión de Dependencias (DIP) (+15):** La clase `PrincipalController` depende directamente de implementaciones concretas (e.g., `Casa.listaCasa()` y `App.setRoot()`), en lugar de abstracciones.

#### Patrones de diseño no utilizados

**Estructurales**

- **Fachada (+10):** Podría proporcionar una interfaz simplificada a la gestión de navegación.

### Clase Analizada: `VistaResidenteController`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo (+5):** Los métodos `initialize()`, `cambiarPin()`, `registrarVehiculo()`, e `ingresarVisita()` tienen más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `VistaResidenteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica de vehículos y visitantes, y cambiar el PIN.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como los detalles de visitantes y vehículos.
- **Lista de Parámetros Largos (+4):** El método `ingresarVisita()` podría tener parámetros encapsulados en una clase `Visitante` o similar.
- **Grupos de Datos (+3):** Las variables `nombreVisitante`, `numCedula`, `correoVisitante`, y `fecha` en el método `ingresarVisita()` siempre se usan juntas y podrían encapsularse en una clase `Visitante`.

**Abusadores de Orientación a Objetos**

- **Sentencias Switch (+5):** No se identificaron sentencias switch en la clase.

**Preventores de Cambio**

- **Cambio divergente (+6):** La clase `VistaResidenteController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de visitantes, actualizar la interfaz de usuario, o cambiar la lógica de vehículos.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de visitantes y vehículos requieren modificaciones en múltiples métodos y clases relacionadas.

**Dispensables**

- **Comentarios (+2):** Existen comentarios en la clase que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** La lógica para verificar y registrar visitantes y vehículos se repite en varios lugares de la clase.
- **Clase de datos (+5):** La clase `VistaResidenteController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.
- **Código muerto (+3):** No se identificaron métodos y variables no utilizados.

**Acopladores**

- **Envidia de características (+5):** Los métodos `cambiarPin()`, `registrarVehiculo()`, e `ingresarVisita()` utilizan intensivamente métodos de la clase `Residente` y `Visitante`.
- **Intimidad inapropiada (+6):** La clase `VistaResidenteController` accede frecuentemente a métodos y variables privadas de las clases `Residente` y `Visitante`.
- **Cadenas de mensajes (+7):** Los métodos `cambiarPin()`, `registrarVehiculo()`, e `ingresarVisita()` realizan varias llamadas en cadena a métodos de las clases `Residente` y `Visitante`.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `VistaResidenteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de visitantes y vehículos.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase `VistaResidenteController` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `cambiarPin()`, `registrarVehiculo()`, e `ingresarVisita()`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `VistaResidenteController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de visitantes y vehículos.

#### Patrones de diseño no utilizados

**Creacionales**

- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de visitantes sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de `VistaResidenteController`.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de visitantes y vehículos y reducir la complejidad en `VistaResidenteController`.

**Estructurales**

- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el registro de visitantes y vehículos.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de visitantes.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de visitante de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de registro.

**De comportamiento**

- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de registro de visitante o vehículo, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de registro.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de visitantes sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase `VistaResidenteController`.
- **Observador (+25):** Podría permitir que un objeto `VistaResidenteController` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto `VistaResidenteController` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de registro, encapsular cada uno, y hacerlos intercambiables en `VistaResidenteController`.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de registro en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de registro de la estructura de objeto `Visitante` sobre la que opera.

### Clase Analizada: `RegistrarResidenteController`

#### Identificación de Olores de Código

**Acaparadores**

- **Método Largo (+5):** El método `registrarResidente()` tiene más de 20 líneas, dificultando su lectura y comprensión.
- **Clase Grande (+6):** La clase `RegistrarResidenteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de registro de residentes.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos, como los detalles del residente (nombre, correo, género, cédula).
- **Lista de Parámetros Largos (+4):** El método `registrarResidente()` podría tener parámetros encapsulados en una clase `Residente` o similar.
- **Grupos de Datos (+3):** Las variables `nombre`, `correo`, `genero` y `cedula` en el método `registrarResidente()` siempre se usan juntas y podrían encapsularse en una clase `Residente`.

**Abusadores de Orientación a Objetos**

- **Sentencias Switch (+5):** No se identificaron sentencias switch en la clase.

**Preventores de Cambio**

- **Cambio divergente (+6):** La clase `RegistrarResidenteController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de registro o actualizar la interfaz de usuario.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de registro de residentes requieren modificaciones en múltiples métodos y clases relacionadas.

**Dispensables**

- **Comentarios (+2):** Existen comentarios en la clase que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** La lógica para verificar y registrar un residente se repite en varios lugares de la clase.
- **Clase de datos (+5):** La clase `RegistrarResidenteController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.
- **Código muerto (+3):** No se identificaron métodos y variables no utilizados.

**Acopladores**

- **Envidia de características (+5):** El método `registrarResidente()` utiliza intensivamente métodos de la clase `Residente`.
- **Intimidad inapropiada (+6):** La clase `RegistrarResidenteController` accede frecuentemente a métodos y variables privadas de la clase `Residente`.
- **Cadenas de mensajes (+7):** El método `registrarResidente()` realiza varias llamadas en cadena a métodos de la clase `Residente`.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `RegistrarResidenteController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de registro.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase `RegistrarResidenteController` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `registrarResidente()`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `RegistrarResidenteController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de registro.

#### Patrones de diseño no utilizados

**Creacionales**

- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de residentes sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de `RegistrarResidenteController`.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de residentes y reducir la complejidad en `RegistrarResidenteController`.

**Estructurales**

- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el registro de residentes.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de residentes.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de residente de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de registro.

**De comportamiento**

- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de registro de residente, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de registro.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de residentes sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase `RegistrarResidenteController`.
- **Observador (+25):** Podría permitir que un objeto `RegistrarResidenteController` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto `RegistrarResidenteController` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de registro, encapsular cada uno, y hacerlos intercambiables en `RegistrarResidenteController`.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de registro en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de registro de la estructura de objeto `Residente` sobre la que opera.


Este repositorio fue obtenido de: https://github.com/josamaci/ProyectoPOO_G8
