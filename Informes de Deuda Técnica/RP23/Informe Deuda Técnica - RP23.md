# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `PInicioController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `initialize` pueden ser largos y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** Métodos con múltiples parámetros que podrían encapsularse en objetos.
- **Grupos de Datos (+3):** Varios parámetros relacionados que podrían agruparse en una clase separada.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):** No identificado en la revisión detallada.
- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de inicio podría afectar `PInicioController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `PInicioController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `PInicioController`.

## Clase Analizada: `PLogInController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `sceneInicio` pueden ser largos y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `PLogInController` podría considerarse grande debido a la cantidad de dependencias importadas y funcionalidades que maneja.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.
- **Campos Temporales (+4):** Variables que se utilizan solo en ciertos métodos y que podrían reducirse mediante la refactorización.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de inicio podría afectar `PLogInController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios innecesarios.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `PLogInController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Sustitución de Liskov (LSP) (+35):** No identificado en la revisión detallada.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Constructor (+25):** Podría mejorarse el constructor actual para crear objetos como `alert`
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar métodos de GUI.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre listas de elementos.

## Clase Analizada: `Mark`

### Identificación de Olores de Código

#### Acaparadores

- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `char` para representar los valores del enum.

#### Dispensables

- **Clase de datos (+5):** La clase `Mark` actúa como un enum con valores de datos.

### Violaciones de los Principios SOLID

No se encontraron violaciones a los principios SOLID.

### Patrones de diseño no utilizados

No se encontraron posibles patrones a utilizar.

## Clase Analizada: `PGameController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos como `initialize` y `runGameLoop` pueden ser largos y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `PGameController` podría considerarse grande debido a la cantidad de dependencias importadas y funcionalidades que maneja.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos como `String` e `int` en lugar de objetos de dominio más ricos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.
- **Campos Temporales (+4):** Variables que se utilizan solo en ciertos métodos y que podrían reducirse mediante la refactorización.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica del juego podría afectar `PGameController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio procedural podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios, pero no parecen excesivos.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `PGameController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `PGameController`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre listas de elementos.
- **Observador (+25):** Podría ser utilizado para observar cambios en los datos.

---

Este repositorio fue obtenido de: [https://github.com/Rjzaruma/Grupo_12](Rjzaruma/Grupo_12)
