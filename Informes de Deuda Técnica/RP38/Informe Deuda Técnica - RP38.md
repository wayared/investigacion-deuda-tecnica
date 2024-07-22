# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `GrupoOperador`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Método `agregarMiembro`: Este método tiene lógica compleja para agregar miembros a un grupo, lo cual podría dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `GrupoOperador` tiene múltiples responsabilidades, incluyendo la gestión de miembros y la creación de grupos.
- **Obsesión Primitiva (+3):** Uso de listas y strings para representar miembros del grupo en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** Método `crearGrupo`: Toma múltiples parámetros que podrían encapsularse en un objeto.
- **Grupos de Datos (+3):** Los parámetros relacionados con la creación de grupos podrían agruparse en una clase separada.

#### Abusadores de Orientación a Objetos

- **Campos Temporales (+4):** Uso de variables temporales dentro de métodos largos como `agregarMiembro`.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de la gestión de grupos podrían afectar múltiples métodos.
- **Cirugía de escopeta (+8):** Cambios en las reglas de negocio afectan varios métodos dentro de `GrupoOperador`.

#### Dispensables

- **Comentarios (+2):** Existen comentarios que podrían ser innecesarios si el código estuviera mejor estructurado.
- **Código duplicado (+7):** Lógica repetida en la validación de miembros y creación de grupos.
- **Clase de datos (+5):** La clase actúa como una clase de datos con múltiples getters y setters.

#### Acopladores

- **Envidia de características (+5):** Métodos que manipulan directamente las propiedades de otras clases.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otras clases en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas encadenadas a múltiples métodos de diferentes clases.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** `GrupoOperador` maneja múltiples responsabilidades: gestión de miembros y creación de grupos.
- **Principio Abierto/Cerrado (OCP) (+40):** No es fácil extender la clase sin modificar su código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** Métodos que no son utilizados directamente por la clase.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser utilizado para la creación de diferentes tipos de grupos.
- **Constructor (+25):** El constructor actual podría mejorarse para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Crear instancias de grupos.

#### Estructurales

- **Fachada (+20):** Podría simplificar la interacción con `GrupoOperador`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre miembros de un grupo.
- **Observador (+25):** Observar cambios en el estado de los miembros del grupo.

## Clase Analizada: `Main`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Método `main`: Puede ser largo y contener lógica compleja que debería dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `Main` tiene múltiples responsabilidades relacionadas con la inicialización de la aplicación.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos en lugar de objetos de dominio más ricos.
- **Lista de Parámetros Largos (+4):** Métodos con múltiples parámetros que podrían encapsularse en objetos.
- **Grupos de Datos (+3):** Parámetros relacionados que podrían agruparse en una clase separada.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` que podrían ser reemplazadas por polimorfismo.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cualquier cambio en la lógica de inicialización podría afectar a múltiples métodos.
- **Cirugía de escopeta (+8):** Cambios en las reglas de negocio afectan varios métodos dentro de `Main`.

#### Dispensables

- **Comentarios (+2):** Existen comentarios que podrían ser innecesarios si el código estuviera mejor estructurado.
- **Código duplicado (+7):** Lógica repetida en la inicialización de la aplicación.
- **Generalidad especulativa (+5):** Métodos o clases que parecen innecesarios para el caso actual.

#### Acopladores

- **Envidia de características (+5):** Métodos que manipulan directamente las propiedades de otras clases.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otras clases en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas encadenadas a múltiples métodos de diferentes clases.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `Main` maneja múltiples responsabilidades: inicialización y configuración de la aplicación.
- **Principio Abierto/Cerrado (OCP) (+40):** No es fácil extender la clase sin modificar su código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** Métodos que no son utilizados directamente por la clase.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser utilizado para la creación de diferentes configuraciones de inicialización.
- **Constructor (+25):** El constructor actual podría mejorarse para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Crear instancias de configuraciones.

#### Estructurales

- **Fachada (+20):** Podría simplificar la interacción con `Main`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre configuraciones.
- **Observador (+25):** Observar cambios en el estado de la aplicación.

## Clase Analizada: `ChatScreen`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Método `build`: Contiene lógica compleja para construir la interfaz de usuario, lo cual podría dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `ChatScreen` maneja múltiples responsabilidades, incluyendo la visualización y gestión de mensajes.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos y listas para representar mensajes y usuarios.
- **Lista de Parámetros Largos (+4):** Métodos con múltiples parámetros que podrían encapsularse en objetos.
- **Grupos de Datos (+3):** Parámetros relacionados que podrían agruparse en una clase separada.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para manejar diferentes tipos de mensajes.
- **Campos Temporales (+4):** Uso de variables temporales dentro de métodos largos como `build`.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de visualización podrían afectar múltiples métodos.
- **Cirugía de escopeta (+8):** Cambios en las reglas de negocio afectan varios métodos dentro de `ChatScreen`.

#### Dispensables

- **Comentarios (+2):** Existen comentarios que podrían ser innecesarios si el código estuviera mejor estructurado.
- **Código duplicado (+7):** Lógica repetida en la construcción de la interfaz de usuario.

#### Acopladores

- **Envidia de características (+5):** Métodos que manipulan directamente las propiedades de otras clases.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otras clases en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas encadenadas a múltiples métodos de diferentes clases.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `ChatScreen` maneja múltiples responsabilidades: visualización de mensajes y gestión de eventos de usuario.
- **Principio Abierto/Cerrado (OCP) (+40):** No es fácil extender la clase sin modificar su código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** Métodos que no son utilizados directamente por la clase.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser utilizado para la creación de diferentes componentes de la interfaz de usuario.
- **Constructor (+25):** El constructor actual podría mejorarse para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Crear instancias de componentes de la interfaz de usuario.

#### Estructurales

- **Fachada (+20):** Podría simplificar la interacción con `ChatScreen`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre mensajes.
- **Observador (+25):** Observar cambios en el estado de los mensajes.

## Clase Analizada: `CrearGrupo`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Método `build`: Contiene lógica compleja para construir la interfaz de usuario, lo cual podría dividirse en métodos más pequeños.
- **Clase Grande (+6):** La clase `CrearGrupo` maneja múltiples responsabilidades, incluyendo la creación de grupos y validación de entradas.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos y listas para representar los miembros del grupo.
- **Lista de Parámetros Largos (+4):** Métodos con múltiples parámetros que podrían encapsularse en objetos.
- **Grupos de Datos (+3):** Parámetros relacionados que podrían agruparse en una clase separada.

#### Abusadores de Orientación a Objetos

- **Sentencias *Switch* (+5):** Uso de múltiples sentencias `if-else` para manejar diferentes tipos de entradas.
- **Campos Temporales (+4):** Uso de variables temporales dentro de métodos largos como `build`.

#### Preventores de Cambio

- **Cambio divergente (+6):** Cambios en la lógica de creación de grupos podrían afectar múltiples métodos.
- **Cirugía de escopeta (+8):** Cambios en las reglas de negocio afectan varios métodos dentro de `CrearGrupo`.

#### Dispensables

- **Comentarios (+2):** Existen comentarios que podrían ser innecesarios si el código estuviera mejor estructurado.
- **Código duplicado (+7):** Lógica repetida en la validación de entradas y creación de grupos.
- **Generalidad especulativa (+5):** Métodos o clases que parecen innecesarios para el caso actual.

#### Acopladores

- **Envidia de características (+5):** Métodos que manipulan directamente las propiedades de otras clases.
- **Intimidad inapropiada (+6):** Acceso directo a propiedades de otras clases en lugar de usar métodos de acceso.
- **Cadenas de mensajes (+7):** Llamadas encadenadas a múltiples métodos de diferentes clases.
- **Hombre medio (+6):** Métodos que simplemente delegan llamadas a otros métodos sin agregar valor.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase `CrearGrupo` maneja múltiples responsabilidades: creación de grupos y validación de entradas.
- **Principio Abierto/Cerrado (OCP) (+40):** No es fácil extender la clase sin modificar su código existente.
- **Principio de Segregación de Interfaces (ISP) (+25):** Métodos que no son utilizados directamente por la clase.
- **Principio de Inversión de Dependencias (DIP) (+45):** Alta dependencia en clases concretas en lugar de abstracciones.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** Podría ser utilizado para la creación de diferentes tipos de grupos.
- **Constructor (+25):** El constructor actual podría mejorarse para manejar múltiples parámetros.
- **Método de Fábrica (+20):** Crear instancias de grupos.

#### Estructurales

- **Fachada (+20):** Podría simplificar la interacción con `CrearGrupo`.

#### De comportamiento

- **Iterador (+15):** Podría ser útil para iterar sobre los miembros del grupo.
- **Observador (+25):** Observar cambios en el estado de los miembros del grupo.

Este repositorio fue obtenido de: https://github.com/AxcelVillagran/FrontendLP
