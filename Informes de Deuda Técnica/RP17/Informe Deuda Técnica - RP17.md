# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `ImagenController`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - `guardarImagen`: Este método es extenso y realiza múltiples tareas, como obtener la ruta de la foto, crear una instancia de `Camara`, agregar la imagen a álbumes y serializar objetos. La complejidad de este método dificulta su comprensión y mantenimiento.
  - `llenarCampos`: Este método también es largo y contiene lógica para cargar imágenes, configurar campos de texto, y actualizar la interfaz de usuario. Realiza demasiadas tareas en un solo método, lo que dificulta su comprensión.

- **Clase Grande (+6):**
  - `ImagenController` tiene múltiples responsabilidades, como la gestión de la interfaz de usuario, la manipulación de imágenes, y la interacción con álbumes y cámaras. Esta sobrecarga de responsabilidades hace que la clase sea difícil de mantener y propensa a errores.

- **Campos Temporales (+4):**
  - `InputStream input`: Utilizado temporalmente en el método `llenarCampos` para cargar una imagen. El uso de campos temporales puede complicar la depuración y el mantenimiento del código.

##### Dispensables

- **Comentarios (+2):**
  - Existen numerosos comentarios explicativos en el código que intentan aclarar la lógica, lo que sugiere que el código no es lo suficientemente claro por sí mismo. En lugar de comentarios, se podrían utilizar nombres de métodos y variables más descriptivos.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `ImagenController` viola este principio al tener múltiples responsabilidades. Maneja la carga y visualización de imágenes, la interacción con la interfaz de usuario, y la lógica de negocio relacionada con álbumes y cámaras. Cada una de estas responsabilidades debería estar en clases separadas para facilitar el mantenimiento y la evolución del código.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Por ejemplo, una fábrica abstracta podría crear diferentes tipos de cámaras o álbumes sin que `ImagenController` tenga que conocer las clases específicas.

- **Constructor (+25):**
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `ImagenController`, encapsulando la lógica de inicialización. Por ejemplo, el constructor podría inicializar todos los componentes de la interfaz y configurar las dependencias necesarias.

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos. Esto puede reducir la complejidad y mejorar la flexibilidad del código, permitiendo que `ImagenController` delegue la creación de imágenes, cámaras y álbumes a métodos de fábrica.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas. Por ejemplo, un adaptador podría permitir que la clase `Imagen` trabaje con diferentes tipos de almacenamiento o servicios de imagen.

- **Compuesto (+30):**
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Por ejemplo, los álbumes podrían ser compuestos que contengan múltiples imágenes y subálbumes, simplificando la gestión y visualización.

- **Decorador (+25):**
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica. Por ejemplo, se podría decorar una `Imagen` con filtros, efectos, o información adicional de manera flexible.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema. Por ejemplo, una fachada podría simplificar la interacción con el sistema de almacenamiento de imágenes, la base de datos de cámaras, y la lógica de álbumes.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor. Por ejemplo, la validación de datos de imagen podría pasar por una cadena de validadores.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes. Por ejemplo, las acciones del usuario en la interfaz gráfica podrían ser comandos que se pueden deshacer y rehacer.

- **Iterador (+15):**
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente. Esto sería útil para iterar sobre las imágenes de un álbum de manera uniforme.

- **Observador (+25):**
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto. Por ejemplo, las vistas de imágenes podrían observar cambios en los datos de `Imagen` y actualizarse automáticamente.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Por ejemplo, se podrían definir diferentes estrategias para ordenar y filtrar imágenes en la interfaz de usuario.

- **Método Plantilla (+25):**
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases. Por ejemplo, los procesos de carga y guardado de imágenes podrían seguir un método plantilla con pasos personalizables.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 1, 0) = (5 + 5 + 4 + 2) + 30 + 0 = 46
\]

La clase `ImagenController` presenta varios malos olores de código, como métodos largos y campos temporales, y también viola el Principio de Responsabilidad Única (SRP). No se han identificado patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 46 puntos.

### Clase Analizada: `PrincipalMenuController`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):** 
  - `initialize`: Este método es extenso y realiza múltiples tareas como actualizar álbumes, crear una galería de imágenes, y configurar la vista inicial. La complejidad y longitud de este método dificultan su comprensión y mantenimiento.
  - `setearDatosInterfaz`: Este método también es largo y contiene lógica para actualizar varios elementos de la interfaz de usuario con los datos de una imagen seleccionada. Maneja múltiples aspectos de la imagen, como etiquetas, comentarios, y detalles de la cámara.

- **Clase Grande (+6):**
  - La clase `PrincipalMenuController` tiene múltiples responsabilidades, incluyendo la gestión de la interfaz de usuario, la manipulación de imágenes y álbumes, y la lógica de filtros y búsqueda. Esta sobrecarga de responsabilidades hace que la clase sea difícil de mantener y propensa a errores.

- **Campos Temporales (+4):**
  - `InputStream input`: Utilizado temporalmente en varios métodos para cargar imágenes. El uso de campos temporales puede complicar la depuración y el mantenimiento del código.

##### Dispensables

- **Comentarios (+2):** 
  - Existen numerosos comentarios explicativos generados automáticamente por la herramienta en el código, lo que sugiere que el código no es lo suficientemente claro por sí mismo. En lugar de comentarios, se podrían utilizar nombres de métodos y variables más descriptivos.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** 
  - La clase `PrincipalMenuController` viola este principio al tener múltiples responsabilidades. Maneja la actualización y visualización de álbumes, la interacción con la interfaz de usuario, y la lógica de búsqueda y filtrado de imágenes. Cada una de estas responsabilidades debería estar en clases separadas para facilitar el mantenimiento y la evolución del código.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Por ejemplo, una fábrica abstracta podría crear diferentes tipos de álbumes o vistas sin que `PrincipalMenuController` tenga que conocer las clases específicas.

- **Constructor (+25):**
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `PrincipalMenuController`, encapsulando la lógica de inicialización. Por ejemplo, el constructor podría inicializar todos los componentes de la interfaz y configurar las dependencias necesarias.

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos. Esto puede reducir la complejidad y mejorar la flexibilidad del código, permitiendo que `PrincipalMenuController` delegue la creación de álbumes, imágenes y vistas a métodos de fábrica.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas. Por ejemplo, un adaptador podría permitir que la clase `Imagen` trabaje con diferentes tipos de almacenamiento o servicios de imagen.

- **Compuesto (+30):**
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Por ejemplo, los álbumes podrían ser compuestos que contengan múltiples imágenes y subálbumes, simplificando la gestión y visualización.

- **Decorador (+25):**
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica. Por ejemplo, se podría decorar una `Imagen` con filtros, efectos, o información adicional de manera flexible.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema. Por ejemplo, una fachada podría simplificar la interacción con el sistema de almacenamiento de imágenes, la base de datos de cámaras, y la lógica de álbumes.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor. Por ejemplo, la validación de datos de imagen podría pasar por una cadena de validadores.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes. Por ejemplo, las acciones del usuario en la interfaz gráfica podrían ser comandos que se pueden deshacer y rehacer.

- **Iterador (+15):**
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente. Esto sería útil para iterar sobre las imágenes de un álbum de manera uniforme.

- **Observador (+25):**
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto. Por ejemplo, las vistas de imágenes podrían observar cambios en los datos de `Imagen` y actualizarse automáticamente.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Por ejemplo, se podrían definir diferentes estrategias para ordenar y filtrar imágenes en la interfaz de usuario.

- **Método Plantilla (+25):**
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases. Por ejemplo, los procesos de carga y guardado de imágenes podrían seguir un método plantilla con pasos personalizables.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (5 + 6 + 4 + 2) + 30 + 0 = 47
\]

La clase `PrincipalMenuController` presenta varios malos olores de código, como métodos largos y campos temporales, y también viola el Principio de Responsabilidad Única (SRP). No se han identificado patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 47 puntos.

### Clase Analizada: `CircularDoubleLinkedList`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - `listIterator`: Este método es largo y realiza múltiples tareas para iterar sobre la lista. La lógica para avanzar y retroceder en la lista, así como para manejar índices y nodos, está toda en este método, lo que dificulta su comprensión y mantenimiento.

##### Dispensables

- **Comentarios (+2):**
  - Existen numerosos comentarios generados automáticamente por la herramienta en el código, lo que sugiere que el código no es lo suficientemente claro por sí mismo. En lugar de comentarios, se podrían utilizar nombres de métodos y variables más descriptivos.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `CircularDoubleLinkedList` viola este principio al tener múltiples responsabilidades. Maneja la gestión de nodos, la iteración sobre la lista, y las excepciones de lista vacía y fuera de límites. Cada una de estas responsabilidades debería estar en clases separadas para facilitar el mantenimiento y la evolución del código.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de nodos y listas sin especificar sus clases concretas. Esto facilita la extensión y el mantenimiento del código, permitiendo la creación de diferentes implementaciones de listas enlazadas.

- **Constructor (+25):**
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `CircularDoubleLinkedList`, encapsulando la lógica de inicialización. Por ejemplo, el constructor podría inicializar la lista con ciertos nodos predefinidos o configuraciones.

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de nodos y listas. Esto puede reducir la complejidad y mejorar la flexibilidad del código, permitiendo que `CircularDoubleLinkedList` delegue la creación de nodos y listas a métodos de fábrica.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que la lista circular funcione con diferentes interfaces de colecciones, facilitando la integración y el mantenimiento. Esto podría permitir que `CircularDoubleLinkedList` se use en contextos donde se espera una lista estándar.

- **Compuesto (+30):**
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de listas. Esto puede simplificar la gestión de colecciones de objetos similares, permitiendo que las listas contengan otras listas de manera recursiva.

- **Decorador (+25):**
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de la lista de manera dinámica sin alterar su estructura básica. Por ejemplo, se podría decorar una lista con funcionalidad adicional como filtrado o transformación de datos.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces de listas y nodos, mejorando la usabilidad del código. Una fachada podría simplificar la interacción con las operaciones complejas de la lista.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud de operación en la lista, reduciendo el acoplamiento entre el emisor y el receptor. Por ejemplo, diferentes manejadores podrían procesar operaciones específicas como adición, eliminación o búsqueda en la lista.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes de operaciones en la lista como objetos, lo que permite parametrizar clientes con colas y solicitudes. Por ejemplo, las operaciones de adición, eliminación y actualización podrían ser comandos que se pueden deshacer y rehacer.

- **Iterador (+15):**
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de la lista sin exponer su representación subyacente. Esto sería útil para iterar sobre los elementos de la lista de manera uniforme y segura.

- **Observador (+25):**
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de la lista. Por ejemplo, otras partes del sistema podrían observar cambios en la lista y reaccionar en consecuencia.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos de manipulación de listas, encapsular cada uno, y hacerlos intercambiables. Por ejemplo, se podrían definir diferentes estrategias para ordenar y filtrar elementos en la lista.

- **Método Plantilla (+25):**
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo de operación en la lista, dejando algunos pasos a las subclases. Por ejemplo, los procesos de iteración y manipulación de nodos podrían seguir un método plantilla con pasos personalizables.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(2, 1, 0) = (5 + 2) + 30 + 0 = 37
\]

La clase `CircularDoubleLinkedList` presenta algunos malos olores de código, especialmente un método largo y comentarios generados automáticamente. También hay violaciones del Principio de Responsabilidad Única (SRP). El esfuerzo estimado para refactorizar esta clase es de 37 puntos.

Este repositorio fue obtenido de: https://github.com/rexman10/ED_Photos_P1
