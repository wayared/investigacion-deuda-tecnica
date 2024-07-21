# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `Cita`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos como el constructor y `guardarCita` pueden ser considerados largos y podrían beneficiarse de una refactorización.
- **Clase Grande (+6):** La clase `Cita` tiene múltiples responsabilidades y muchos atributos, lo que puede indicar que es demasiado grande.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `LocalDate`, `LocalTime`, `String` en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** El constructor y algunos métodos toman múltiples parámetros que podrían encapsularse en un objeto.
- **Grupos de Datos (+3):** Varios parámetros relacionados que podrían agruparse en una clase separada, especialmente en el constructor.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de cita, cliente o servicio podría afectar `Cita`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro de `Cita`.

#### Dispensables

- **Comentarios (+2):** Algunos comentarios explicativos podrían eliminarse mediante la refactorización del código para que sea autoexplicativo.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `Cita` maneja múltiples responsabilidades: validación, manipulación de datos y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de citas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de citas.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `Cita`.

## Clase Analizada: `CitasController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos no identificados en la vista preliminar, pero la clase puede tener métodos largos considerando la naturaleza de un controlador.
- **Clase Grande (+6):** La clase `CitasController` podría considerarse grande debido a la cantidad de dependencias importadas y funcionalidades que probablemente maneje.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `LocalDate` y `LocalTime`.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios innecesarios.

#### Acopladores

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `CitasController` maneja múltiples responsabilidades relacionadas con la UI y la lógica de negocio.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de controladores.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `CitasController`.


## Clase Analizada: `AgregarCitaController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `guardarCita` y `initialize` tienen un número considerable de líneas de código y lógica compleja que puede dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `AgregarCitaController` tiene muchas responsabilidades y contiene un número elevado de métodos y atributos.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `LocalDate`, `LocalTime`, `String`, `int` en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** Métodos como `guardarCita` toman múltiples parámetros que podrían encapsularse en un objeto.
- **Grupos de Datos (+3):** Varios parámetros relacionados que podrían agruparse en una clase separada.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.
- **Campos Temporales (+4):** Variables que se utilizan solo en ciertos métodos y que podrían reducirse mediante la refactorización.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de cita, cliente o servicio podría afectar `AgregarCitaController`, debido a sus múltiples responsabilidades.

- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** Algunos comentarios explicativos podrían eliminarse mediante la refactorización del código para que sea autoexplicativo.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `AgregarCitaController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `AgregarCitaController`.

## Clase Analizada: `AtencionesController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `initialize` y `eliminarAtencion` tienen un número considerable de líneas de código y lógica compleja que puede dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `AtencionesController` podría considerarse grande debido a la cantidad de dependencias importadas y funcionalidades que maneja.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `LocalDate`, `LocalTime`, `String` en lugar de objetos de dominio más ricos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.
- **Campos Temporales (+4):** Variables que se utilizan solo en ciertos métodos y que podrían reducirse mediante la refactorización.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de atención podría afectar `AtencionesController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios innecesesarios.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `AtencionesController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de atenciones.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `AtencionesController`.




Este repositorio fue obtenido de: https://github.com/Jeremy-Poveda/Medical-appointment-system-for-special-children