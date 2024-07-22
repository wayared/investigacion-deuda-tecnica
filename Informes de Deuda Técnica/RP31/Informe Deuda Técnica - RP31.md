# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `ChooseXorOController`

### Identificación de Olores de Código

#### Acaparadores

- **Obsesión Primitiva (+3):** Uso de tipos primitivos en lugar de objetos de dominio más ricos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica del controlador podría afectar `ChooseXorOController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `ChooseXorOController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `ChooseXorOController`.

#### De comportamiento

- **Observador (+25):** Podría ser utilizado para observar cambios en los datos.

## Clase Analizada: `ChooseWhoStartsController`

### Identificación de Olores de Código

#### Acaparadores

- **Obsesión Primitiva (+3):** Uso de tipos primitivos en lugar de objetos de dominio más ricos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica del controlador podría afectar `ChooseWhoStartsController`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en las reglas de negocio podría afectar múltiples métodos dentro del controlador.

#### Dispensables

- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `ChooseWhoStartsController` maneja múltiples responsabilidades: validación, manipulación de UI y lógica de negocio.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de controladores o vistas.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `ChooseWhoStartsController`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre listas de elementos.
- **Observador (+25):** Podría ser utilizado para observar cambios en los datos.

## Clase Analizada: `Square`

### Identificación de Olores de Código

#### Dispensables

- **Código duplicado (+7):** Se encuentra bloques de código repetidos.

#### Acopladores

- **Intimidad inapropiada (+6):** `ifIsComputerNextTurn` realiza llamadas a muchos métodos de otras clases.
- **Cadenas de mensajes (+7):** Se encuentran muchos métodos llamando a métodos de otras clases de manera explícita formando una cadena de mensajes.

### Violaciones de los Principios SOLID

No se encontraron violaciones a los principios SOLID.

### Patrones de diseño no utilizados

#### Creacionales

- **Constructor (+25):** Puede ser utilizado para construir y configuar de manera óptima los componentes.

#### Estructurales

- **Fachada (+20):** Puede ser utilizado para facilitar la interacción con el controlador.

#### De comportamiento

- **Estrategia (+20):** No identificado en la revisión detallada.
- **Método Plantilla (+25):** No identificado en la revisión detallada.
- **Visitante (+35):** No identificado en la revisión detallada.

## Clase Analizada: `Board`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Métodos que pueden ser largos y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `Board` contiene múltiples responsabilidades y muchos atributos y métodos, lo que sugiere que es demasiado grande.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** Métodos con múltiples parámetros que podrían encapsularse en objetos.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para validaciones que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica del tablero podría afectar `Board`, debido a sus múltiples responsabilidades.
- **Cirugía de escopeta (+8):** Cualquier cambio en los procedimientos podría afectar múltiples métodos dentro de la clase.

#### Dispensables

- **Código duplicado (+7):** Lógica repetida en la validación de entradas y gestión de excepciones.

#### Acopladores

- **Envidia de características (+5):** Métodos que acceden a múltiples propiedades de otras clases, mostrando una posible necesidad de refactorización.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otros objetos en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas a múltiples métodos de diferentes clases en una secuencia.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `Board` maneja múltiples responsabilidades: lógica del tablero, validaciones y manipulaciones de datos.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase no está abierta para extensión pero cerrada para modificación. Cualquier nueva funcionalidad requiere cambios en el código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** La clase depende de métodos que no utiliza directamente.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser usado para crear diferentes tipos de tableros.
- **Constructor (+25):** Podría mejorarse el constructor actual para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Podría ser usado para la creación de instancias.

#### Estructurales

- **Fachada (+20):** Podría ser utilizado para simplificar la interacción con `Board`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre listas de elementos.
- **Observador (+25):** Podría ser utilizado para observar cambios en el estado del tablero.

---

Este repositorio fue obtenido de: [https://github.com/niplinig/Grupo_09]()
