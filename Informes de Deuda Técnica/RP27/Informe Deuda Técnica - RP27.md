# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `User`

### Identificación de Olores de Código

#### Acaparadores

- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `String` para representar usuario y contraseña.

#### Dispensables

- **Clase de datos (+5):** La clase `User` actúa como una clase de datos con getters y setters.

### Violaciones de los Principios SOLID

No se encontraron violaciones a los principios SOLID.

### Patrones de diseño no utilizados

No se encontraron posibles patrones a utilizar.

## Clase Analizada: `LoginController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método `login` podría ser largo y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `LoginController` contiene múltiples responsabilidades y muchos atributos y métodos, lo que sugiere que es demasiado grande.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `String` para representar usuario y contraseña en lugar de objetos de dominio más ricos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de inicio de sesión podría afectar `LoginController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios, pero no parecen excesivos.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `LoginController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `LoginController`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre listas de elementos.
- **Observador (+25):** Podría ser utilizado para observar cambios en los datos.

## Clase Analizada: `RegisterController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `registerUser` pueden ser largos y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `RegisterController` contiene múltiples responsabilidades y muchos atributos y métodos, lo que sugiere que es demasiado grande.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `String` para representar usuario y contraseña en lugar de objetos de dominio más ricos.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** No identificado en la revisión detallada.
- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de registro podría afectar `RegisterController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios, pero no parecen excesivos.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `RegisterController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `RegisterController`.

#### De comportamiento

- **Observador (+25):** Podría ser utilizado para observar cambios en los datos.

## Clase Analizada: `PrincipalPaneController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `initialize` pueden ser largos y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `PrincipalPaneController` contiene múltiples responsabilidades y muchos atributos y métodos, lo que sugiere que es demasiado grande.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `String` y `int` en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** Métodos con múltiples parámetros que podrían encapsularse en objetos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica del panel principal podría afectar `PrincipalPaneController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios, pero no parecen excesivos.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `PrincipalPaneController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `PrincipalPaneController`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre listas de elementos.

---

Este repositorio fue obtenido de: https://github.com/jcvivas/EDD1_PROY1P_LUNA_VIVAS_TENESAC
