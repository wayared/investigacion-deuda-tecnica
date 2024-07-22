# Informe de Análisis de Deuda Técnica
### Clase Analizada: `Ventas`

---

## Identificación de Olores de Código

### Acaparadores

- **Método Largo (+5):** El método `leerVentas()` tiene más de 20 líneas, lo que dificulta su lectura y comprensión.

- **Clase Grande (+6):** La clase `Ventas` tiene múltiples responsabilidades, como gestionar propiedades de ventas, leer datos de archivos, calcular el monto facturado y agregar nuevas ventas.

- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`String`, `double`) para representar datos complejos como ventas y montos facturados.

- **Lista de Parámetros Largos (+4):** El constructor de la clase `Ventas` tiene una lista de parámetros larga.

- **Grupos de Datos (+3):** Las variables `fecha`, `mesero`, `cuenta`, `mesa`, `venta` y `cliente` siempre se usan juntas y podrían encapsularse en una clase `Venta`.

### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):** No se encontraron sentencias switch en esta clase.

### Preventores de Cambio

- **Cambio divergente (+6):** La clase `Ventas` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de lectura de archivos o actualizar las propiedades de ventas.

- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de manejo de ventas requieren modificaciones en múltiples métodos de la clase `Ventas`.

### Dispensables

- **Comentarios (+2):** Existen algunos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):** El código para leer y escribir ventas se repite en varios lugares de la clase `Ventas`.

- **Clase de datos (+5):** La clase `Ventas` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos.

- **Código muerto (+3):** No se identificó código muerto en esta clase.

### Acopladores

- **Envidia de características (+5):** El método `leerVentas()` utiliza intensivamente métodos de la clase `App` y `BufferedReader`.

- **Intimidad inapropiada (+6):** No se encontró acceso a métodos o variables privadas de otras clases de manera inapropiada.

- **Cadenas de mensajes (+7):** El método `leerVentas()` realiza varias llamadas en cadena a métodos de las clases `BufferedReader` y `InputStreamReader`.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `Ventas` tiene múltiples responsabilidades, como gestionar las propiedades de ventas, leer y escribir archivos.

- **Principio Abierto/Cerrado (OCP) (+40):** La clase `Ventas` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `leerVentas()` y `agregarVenta()`.

- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `Ventas` depende directamente de implementaciones concretas como `BufferedReader`, `FileWriter`, `InputStreamReader`.

## Patrones de diseño no utilizados

### Creacionales

- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de ventas sin especificar sus clases concretas.

- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de `Ventas`.

- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de ventas y reducir la complejidad en `Ventas`.

### Estructurales

- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la lectura y escritura de archivos.

- **Compuesto (+30):** Podría ser útil para representar jerarquías de ventas.

- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de venta de manera dinámica.

- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de manejo de ventas.

### De comportamiento

- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de venta, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de venta.

- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de ventas sin exponer su representación subyacente.

- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase `Ventas`.

- **Observador (+25):** Podría permitir que un objeto `Ventas` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):** Podría permitir que un objeto `Ventas` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):** Podría definir una familia de algoritmos de manejo de ventas, encapsular cada uno, y hacerlos intercambiables en `Ventas`.

- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de manejo de ventas en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):** Podría separar un algoritmo de manejo de ventas de la estructura de objeto `Ventas` sobre la que opera.

### Clase Analizada: `LoginController`

---

## Identificación de Olores de Código

### Acaparadores

- **Método Largo (+5):** El método `irInterfaz()` tiene más de 20 líneas, lo que dificulta su lectura y comprensión.

- **Clase Grande (+6):** La clase `LoginController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la autenticación y registrar usuarios ingresados.

- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`String`) para representar datos complejos como usuarios y credenciales.

- **Lista de Parámetros Largos (+4):** No se encontró un método con lista de parámetros largos, pero el constructor de la clase `Usuario` podría beneficiarse de una encapsulación.

- **Grupos de Datos (+3):** Las variables `txtCorreo` y `txtContrasena` siempre se usan juntas y podrían encapsularse en una clase `Credenciales`.

### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):** No se encontraron sentencias switch en esta clase.

### Preventores de Cambio

- **Cambio divergente (+6):** La clase `LoginController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de autenticación o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de manejo de usuarios requieren modificaciones en múltiples métodos de la clase `LoginController`.

### Dispensables

- **Comentarios (+2):** Existen algunos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):** El código para autenticar y registrar usuarios se repite en varios lugares de la clase `LoginController`.

- **Clase de datos (+5):** La clase `LoginController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos.

- **Código muerto (+3):** No se identificó código muerto en esta clase.

### Acopladores

- **Envidia de características (+5):** El método `irInterfaz()` utiliza intensivamente métodos de la clase `App` y de las clases `Administrador` y `Mesero`.

- **Intimidad inapropiada (+6):** No se encontró acceso a métodos o variables privadas de otras clases de manera inapropiada.

- **Cadenas de mensajes (+7):** El método `irInterfaz()` realiza varias llamadas en cadena a métodos de las clases `App` y `BufferedReader`.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `LoginController` tiene múltiples responsabilidades, como gestionar la autenticación de usuarios, registrar usuarios ingresados y manejar la interfaz de usuario.

- **Principio Abierto/Cerrado (OCP) (+40):** La clase `LoginController` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `irInterfaz()` y `registrarUsuariosIngresados()`.

- **Principio de Inversión de Dependencias (DIP) (+45):** La clase `LoginController` depende directamente de implementaciones concretas como `BufferedReader`, `FileWriter`, `InputStreamReader`.

## Patrones de diseño no utilizados

### Creacionales

- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de usuarios sin especificar sus clases concretas.

- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de `LoginController`.

- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de usuarios y reducir la complejidad en `LoginController`.

### Estructurales

- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la autenticación y registro de usuarios.

- **Compuesto (+30):** Podría ser útil para representar jerarquías de usuarios.

- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de usuario de manera dinámica.

- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de manejo de usuarios.

### De comportamiento

- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de autenticación de usuario, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de autenticación.

- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de usuarios sin exponer su representación subyacente.

- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase `LoginController`.

- **Observador (+25):** Podría permitir que un objeto `LoginController` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):** Podría permitir que un objeto `LoginController` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):** Podría definir una familia de algoritmos de manejo de autenticación, encapsular cada uno, y hacerlos intercambiables en `LoginController`.

- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de manejo de autenticación en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):** Podría separar un algoritmo de manejo de autenticación de la estructura de objeto `Usuario` sobre la que opera.

### Clase Analizada: `RegistrarCuentaController`

---

## Identificación de Olores de Código

### Acaparadores

- **Clase Grande (+6):** La clase `RegistrarCuentaController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario para el registro y manejar la lógica de creación de usuarios.

- **Obsesión Primitiva (+3):** Uso de tipos primitivos (`String`) para representar datos complejos como usuarios y credenciales.

- **Grupos de Datos (+3):** Las variables `txtCorreo`, `txtContrasena` y `tipoUsuario` siempre se usan juntas y podrían encapsularse en una clase `Registro`.

### Preventores de Cambio

- **Cambio divergente (+6):** La clase `RegistrarCuentaController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de registro o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica de manejo de usuarios requieren modificaciones en múltiples métodos de la clase `RegistrarCuentaController`.

### Dispensables

- **Comentarios (+2):** Existen algunos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):** El código para registrar usuarios se repite en varios lugares de la clase `RegistrarCuentaController`.

- **Clase de datos (+5):** La clase `RegistrarCuentaController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos.

### Acopladores

- **Envidia de características (+5):** El método `registrarUsuario()` utiliza intensivamente métodos de la clase `LoginController`.

- **Cadenas de mensajes (+7):** El método `registrarUsuario()` realiza varias llamadas en cadena a métodos de las clases `LoginController` y `UsuarioData`.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `RegistrarCuentaController` tiene múltiples responsabilidades, como gestionar la interfaz de registro de usuarios, y manejar la lógica de registro y validación.

- **Principio Abierto/Cerrado (OCP) (+40):** La clase `RegistrarCuentaController` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `registrarUsuario()` e `initialize()`.

## Patrones de diseño no utilizados

### Creacionales

- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de usuarios sin especificar sus clases concretas.

### Estructurales

- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de manejo de usuarios.

### De comportamiento

- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de registro de usuario, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de registro.

- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de usuarios sin exponer su representación subyacente.

- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase `RegistrarCuentaController`.

- **Observador (+25):** Podría permitir que un objeto `RegistrarCuentaController` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):** Podría permitir que un objeto `RegistrarCuentaController` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):** Podría definir una familia de algoritmos de manejo de registro, encapsular cada uno, y hacerlos intercambiables en `RegistrarCuentaController`.

- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de manejo de registro en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):** Podría separar un algoritmo de manejo de registro de la estructura de objeto `Usuario` sobre la que opera.


### Clase Analizada: `MonitoreoRestaurante2Controller`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
  - El método `initialize()` tiene más de 50 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6):**
  - La clase `MonitoreoRestaurante2Controller` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica de ventas y administración del menú.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos complejos, como los detalles de ventas y platos.

- **Lista de Parámetros Largos (+4):**
  - El método `informacionMesa(int numero, int capacidad, String mesero, String estado, String pestana, Ubicacion u)` tiene una lista de parámetros larga.

- **Grupos de Datos (+3):**
  - Las variables `numero, capacidad, mesero, estado, pestana, ubicacion` en el método `informacionMesa` siempre se usan juntas y podrían encapsularse en una clase `MesaInfo`.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - El método `iniciarElementosPanel` utiliza varias sentencias condicionales para manejar diferentes estados de mesas.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `MonitoreoRestaurante2Controller` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de ventas o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de ventas requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

- **Comentarios (+2):**
  - Existen muchos comentarios en el método `initialize()` que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):**
  - El código para la gestión de platos se repite en varios lugares de la clase `MonitoreoRestaurante2Controller`.

- **Clase de datos (+5):**
  - La clase `MonitoreoRestaurante2Controller` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de la interfaz.

- **Código muerto (+3):**
  - Existen métodos y variables no utilizados.

#### Acopladores

- **Envidia de características (+5):**
  - El método `iniciarElementosPanel()` utiliza intensivamente métodos de la clase `Mesa`.

- **Intimidad inapropiada (+6):**
  - La clase `MonitoreoRestaurante2Controller` accede frecuentemente a métodos y variables privadas de la clase `Mesa`.

- **Cadenas de mensajes (+7):**
  - El método `initialize()` realiza varias llamadas en cadena a métodos de otras clases.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `MonitoreoRestaurante2Controller` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica de ventas y administración del menú.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `MonitoreoRestaurante2Controller` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `initialize()`.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `MonitoreoRestaurante2Controller` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de ventas y platos.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes tipos de `Mesa` sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `MonitoreoRestaurante2Controller`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de `Mesa` y reducir la complejidad en `MonitoreoRestaurante2Controller`.

#### Estructurales

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de mesas y platos.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de `Mesa` y `Plato`.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de `Mesa` y `Plato` de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de ventas y gestión de mesas.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de actualización de mesa, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de ventas.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de `Mesa` y `Plato` sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `MonitoreoRestaurante2Controller`.

- **Observador (+25):**
  - Podría permitir que un objeto `MonitoreoRestaurante2Controller` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `MonitoreoRestaurante2Controller` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de gestión de mesas y ventas, encapsular cada uno, y hacerlos intercambiables en `MonitoreoRestaurante2Controller`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de gestión de mesas y ventas en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
  - Podría separar un algoritmo de gestión de mesas y ventas de la estructura de objeto `Mesa` y `Plato` sobre la que opera.



Este repositorio fue obtenido de: https://github.com/vicpebarragan/Proyecto2Parcial
