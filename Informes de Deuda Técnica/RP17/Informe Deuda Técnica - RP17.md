
# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `ImagenController`

#### Identificación de Olores de Código

##### Acaparadores
- **Método Largo (+5):** 
  - `guardarImagen` (es largo y realiza múltiples tareas)
  - `llenarCampos` (realiza muchas tareas y contiene lógica compleja)

##### Abusadores de Orientación a Objetos
- **Campos Temporales (+4):** 
  - `InputStream input` (en `llenarCampos` se utiliza temporalmente)

##### Dispensables
- **Comentarios (+2):** 
  - Comentarios explicativos en diversas partes del código en lugar de utilizar nombres de métodos y variables más claros.

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30):** 
  - La clase `ImagenController` maneja múltiples responsabilidades como cargar imágenes, guardar datos, y manejar la interfaz de usuario.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** No
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Esto facilita la extensión y el mantenimiento del código.
- **Constructor (+25):** No
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `ImagenController`, encapsulando la lógica de inicialización.
- **Método de Fábrica (+20):** No
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos, lo que puede reducir la complejidad y mejorar la flexibilidad del código.

#### Estructurales
- **Adaptador (+25):** No
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas, facilitando la integración y el mantenimiento.
- **Puente (+35):** No
- **Compuesto (+30):** No
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Esto puede simplificar la gestión de colecciones de objetos similares.
- **Decorador (+25):** No
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica.
- **Fachada (+20):** No
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema, mejorando la usabilidad del código.
- **Peso Ligero (+40):** No
- **Proxy (+30):** No

#### De comportamiento
- **Cadena de Responsabilidad (+30):** No
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** No
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes.
- **Intérprete (+40):** No
- **Iterador (+15):** No
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente.
- **Mediador (+30):** No
- **Memento (+35):** No
- **Observador (+25):** No
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto.
- **Estado (+30):** No
- **Estrategia (+20):** No
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables, mejorando la flexibilidad y la reutilización del código.
- **Método Plantilla (+25):** No
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** No

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 1, 0) = (5 + 5 + 4 + 2) + 30 + 0 = 46
\]

La clase `ImagenController` presenta algunos malos olores de código, especialmente métodos largos y campos temporales. También hay violaciones del Principio de Responsabilidad Única (SRP). No se identificaron patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 46 puntos.

### Clase Analizada: `PrincipalMenuController`

#### Identificación de Olores de Código

##### Acaparadores
- **Método Largo (+5):** 
  - `initialize` (es largo y realiza múltiples tareas)
  - `setearDatosInterfaz` (realiza muchas tareas y contiene lógica compleja)
- **Clase Grande (+6):** 
  - La clase `PrincipalMenuController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica de álbumes, y controlar la visualización de imágenes.
- **Campos Temporales (+4):** 
  - `InputStream input` (en varios métodos se utiliza temporalmente)

##### Dispensables
- **Comentarios (+2):** 
  - Comentarios explicativos en diversas partes del código en lugar de utilizar nombres de métodos y variables más claros.

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30):** 
  - La clase `PrincipalMenuController` maneja múltiples responsabilidades como la gestión de álbumes, la visualización de imágenes, y el manejo de eventos de la interfaz de usuario.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** 
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Esto facilita la extensión y el mantenimiento del código.
- **Constructor (+25):** 
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `PrincipalMenuController`, encapsulando la lógica de inicialización.
- **Método de Fábrica (+20):** 
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos, lo que puede reducir la complejidad y mejorar la flexibilidad del código.

#### Estructurales
- **Adaptador (+25):** 
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas, facilitando la integración y el mantenimiento.
- **Compuesto (+30):** 
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Esto puede simplificar la gestión de colecciones de objetos similares.
- **Decorador (+25):** 
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica.
- **Fachada (+20):** 
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema, mejorando la usabilidad del código.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** 
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** 
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes.
- **Iterador (+15):** 
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente.
- **Observador (+25):** 
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto.
- **Estrategia (+20):** 
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables, mejorando la flexibilidad y la reutilización del código.
- **Método Plantilla (+25):** 
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (5 + 6 + 4 + 2) + 30 + 0 = 47
\]

La clase `PrincipalMenuController` presenta varios malos olores de código, especialmente métodos largos y campos temporales. También hay violaciones del Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 47 puntos.

### Clase Analizada: `CircularDoubleLinkedList`

#### Identificación de Olores de Código

##### Acaparadores
- **Método Largo (+5):** 
  - `listIterator` (realiza múltiples tareas y contiene lógica compleja)

##### Dispensables
- **Comentarios (+2):** 
  - Comentarios generados automáticamente por la herramienta en varios métodos sin implementación.

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30):** 
  - La clase `CircularDoubleLinkedList` maneja múltiples responsabilidades como la gestión de nodos, iteradores y excepciones, lo cual podría dividirse en varias clases especializadas.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** 
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de nodos y listas sin especificar sus clases concretas. Esto facilita la extensión y el mantenimiento del código.
- **Constructor (+25):** 
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `CircularDoubleLinkedList`, encapsulando la lógica de inicialización.
- **Método de Fábrica (+20):** 
  - Consejo: Usa el Método de Fábrica para encapsular la creación de nodos y listas, lo que puede reducir la complejidad y mejorar la flexibilidad del código.

#### Estructurales
- **Adaptador (+25):** 
  - Consejo: Implementa el patrón Adaptador para permitir que la lista circular funcione con diferentes interfaces de colecciones, facilitando la integración y el mantenimiento.
- **Compuesto (+30):** 
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de listas. Esto puede simplificar la gestión de colecciones de objetos similares.
- **Decorador (+25):** 
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de la lista de manera dinámica sin alterar su estructura básica.
- **Fachada (+20):** 
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces de listas y nodos, mejorando la usabilidad del código.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** 
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud de operación en la lista, reduciendo el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** 
  - Consejo: Aplica el patrón Comando para encapsular solicitudes de operaciones en la lista como objetos, lo que permite parametrizar clientes con colas y solicitudes.
- **Iterador (+15):** 
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de la lista sin exponer su representación subyacente.
- **Observador (+25):** 
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de la lista.
- **Estrategia (+20):** 
  - Consejo: Usa Estrategia para definir una familia de algoritmos de manipulación de listas, encapsular cada uno, y hacerlos intercambiables, mejorando la flexibilidad y la reutilización del código.
- **Método Plantilla (+25):** 
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo de operación en la lista, dejando algunos pasos a las subclases.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(2, 1, 0) = (5 + 2) + 30 + 0 = 37
\]

### Resumen
La clase `CircularDoubleLinkedList` presenta algunos malos olores de código, especialmente un método largo y comentarios generados automáticamente. También hay violaciones del Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 37 puntos.

Este repositorio fue obtenido de: https://github.com/rexman10/ED_Photos_P1
