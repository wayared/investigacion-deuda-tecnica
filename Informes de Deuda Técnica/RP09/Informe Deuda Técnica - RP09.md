# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `InterfazAdministradorController`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - `initialize`: Este método es extenso y realiza múltiples tareas como poner mesas en los paneles, iniciar hilos para actualizar comensales y facturación, y configurar las tablas de ventas. La complejidad de este método dificulta su comprensión y mantenimiento.
  - `ponerMesas`: Este método también es largo y contiene lógica para crear mesas, configurar su apariencia, agregar manejadores de eventos y actualizar su ubicación. La longitud y complejidad de este método dificultan su comprensión.

##### Dispensables

- **Comentarios (+2):**
  - Existen numerosos comentarios generados automáticamente por la herramienta y algunos que intentan aclarar la lógica del código, lo que sugiere que el código no es lo suficientemente claro por sí mismo. En lugar de comentarios, se podrían utilizar nombres de métodos y variables más descriptivos.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - Aunque no se encuentran directamente sentencias *switch*, el uso de múltiples condicionales (`if-else`) en métodos como `ponerMesas` y `setOnMouseClicked` para manejar el estado y la interacción de las mesas podría beneficiarse de una refactorización utilizando el patrón de diseño Estado o Estrategia.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `InterfazAdministradorController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de interfaz de usuario, actualizar datos de ventas, y manejar eventos de interacción con mesas.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de interfaz de usuario requieren modificaciones en múltiples métodos y clases relacionadas, lo que aumenta el riesgo de introducir errores.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - La clase `InterfazAdministradorController` accede frecuentemente a métodos y variables privadas de otras clases como `Mesa`, `Comida`, y `VentasData`, lo que aumenta el acoplamiento y dificulta el mantenimiento.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `InterfazAdministradorController` viola este principio al tener múltiples responsabilidades. Maneja la actualización y visualización de mesas, la interacción con la interfaz de usuario, la lógica de ventas y reportes, y la gestión del menú. Cada una de estas responsabilidades debería estar en clases separadas para facilitar el mantenimiento y la evolución del código.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `InterfazAdministradorController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de datos de mesas, comidas y ventas. Debería depender de interfaces o clases abstractas para reducir el acoplamiento y aumentar la flexibilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Por ejemplo, una fábrica abstracta podría crear diferentes tipos de mesas o comidas sin que `InterfazAdministradorController` tenga que conocer las clases específicas.

- **Constructor (+25):**
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `InterfazAdministradorController`, encapsulando la lógica de inicialización. Por ejemplo, el constructor podría inicializar todos los componentes de la interfaz y configurar las dependencias necesarias.

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos. Esto puede reducir la complejidad y mejorar la flexibilidad del código, permitiendo que `InterfazAdministradorController` delegue la creación de mesas, comidas y ventas a métodos de fábrica.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas. Por ejemplo, un adaptador podría permitir que la clase `Mesa` trabaje con diferentes tipos de almacenamiento o servicios.

- **Compuesto (+30):**
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Por ejemplo, las mesas y sus ubicaciones podrían ser compuestos que contengan múltiples mesas y submesas, simplificando la gestión y visualización.

- **Decorador (+25):**
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica. Por ejemplo, se podría decorar una `Mesa` con información adicional como estado o capacidad de manera flexible.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema. Por ejemplo, una fachada podría simplificar la interacción con el sistema de gestión de mesas, comidas y ventas.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor. Por ejemplo, la validación de datos de ventas podría pasar por una cadena de validadores.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes. Por ejemplo, las acciones del usuario en la interfaz gráfica podrían ser comandos que se pueden deshacer y rehacer.

- **Iterador (+15):**
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente. Esto sería útil para iterar sobre los elementos de las mesas y las comidas de manera uniforme.

- **Observador (+25):**
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto. Por ejemplo, las vistas de mesas podrían observar cambios en los datos de `Mesa` y actualizarse automáticamente.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Por ejemplo, se podrían definir diferentes estrategias para ordenar y filtrar elementos en las tablas de ventas y comidas.

- **Método Plantilla (+25):**
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases. Por ejemplo, los procesos de actualización y manipulación de mesas podrían seguir un método plantilla con pasos personalizables.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 0) = (5 + 6 + 6 + 2 + 5 + 8) + (30 + 45) + 0 = 107
\]

La clase `InterfazAdministradorController` presenta varios malos olores de código, como métodos largos, uso de múltiples condicionales, y acoplamiento inapropiado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). No se han identificado patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 107 puntos.

### Clase Analizada: `PedidosController`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - `initialize`: Este método es extenso y realiza múltiples tareas como la configuración de la interfaz de usuario, la carga de datos de comidas y la configuración de manejadores de eventos. La complejidad y longitud de este método dificultan su comprensión y mantenimiento.

- **Clase Grande (+6):**
  - La clase `PedidosController` tiene múltiples responsabilidades, como la gestión de la interfaz de usuario, la manipulación de pedidos, y la lógica de eventos. Esta sobrecarga de responsabilidades hace que la clase sea difícil de mantener y propensa a errores.

##### Dispensables

- **Comentarios (+2):**
  - Existen comentarios que intentan aclarar la lógica del código, lo que sugiere que el código no es lo suficientemente claro por sí mismo. En lugar de comentarios, se podrían utilizar nombres de métodos y variables más descriptivos.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - Aunque no se encuentran directamente sentencias *switch*, el uso de múltiples condicionales (`if-else`) en métodos como `initialize` para manejar diferentes tipos de comidas podría beneficiarse de una refactorización utilizando el patrón de diseño Estrategia.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `PedidosController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de interfaz de usuario, actualizar datos de comidas, y manejar eventos de interacción con pedidos.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de interfaz de usuario requieren modificaciones en múltiples métodos y clases relacionadas, lo que aumenta el riesgo de introducir errores.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - La clase `PedidosController` accede frecuentemente a métodos y variables privadas de otras clases como `Comida` y `ComidaData`, lo que aumenta el acoplamiento y dificulta el mantenimiento.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `PedidosController` viola este principio al tener múltiples responsabilidades. Maneja la actualización y visualización de pedidos, la interacción con la interfaz de usuario, y la lógica de eventos. Cada una de estas responsabilidades debería estar en clases separadas para facilitar el mantenimiento y la evolución del código.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `PedidosController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de datos de comidas y pedidos. Debería depender de interfaces o clases abstractas para reducir el acoplamiento y aumentar la flexibilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Por ejemplo, una fábrica abstracta podría crear diferentes tipos de comidas o pedidos sin que `PedidosController` tenga que conocer las clases específicas.

- **Constructor (+25):**
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `PedidosController`, encapsulando la lógica de inicialización. Por ejemplo, el constructor podría inicializar todos los componentes de la interfaz y configurar las dependencias necesarias.

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos. Esto puede reducir la complejidad y mejorar la flexibilidad del código, permitiendo que `PedidosController` delegue la creación de comidas y pedidos a métodos de fábrica.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas. Por ejemplo, un adaptador podría permitir que la clase `Comida` trabaje con diferentes tipos de almacenamiento o servicios.

- **Compuesto (+30):**
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Por ejemplo, los pedidos y sus detalles podrían ser compuestos que contengan múltiples elementos de pedido, simplificando la gestión y visualización.

- **Decorador (+25):**
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica. Por ejemplo, se podría decorar un `Pedido` con información adicional como descuentos o impuestos de manera flexible.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema. Por ejemplo, una fachada podría simplificar la interacción con el sistema de gestión de comidas y pedidos.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor. Por ejemplo, la validación de datos de pedidos podría pasar por una cadena de validadores.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes. Por ejemplo, las acciones del usuario en la interfaz gráfica podrían ser comandos que se pueden deshacer y rehacer.

- **Iterador (+15):**
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente. Esto sería útil para iterar sobre los elementos de las comidas y los pedidos de manera uniforme.

- **Observador (+25):**
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto. Por ejemplo, las vistas de pedidos podrían observar cambios en los datos de `Pedido` y actualizarse automáticamente.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Por ejemplo, se podrían definir diferentes estrategias para ordenar y filtrar elementos en las tablas de pedidos y comidas.

- **Método Plantilla (+25):**
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases. Por ejemplo, los procesos de actualización y manipulación de pedidos podrían seguir un método plantilla con pasos personalizables.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 0) = (5 + 6 + 6 + 2 + 5 + 8) + (30 + 45) + 0 = 107
\]

La clase `PedidosController` presenta varios malos olores de código, como métodos largos, uso de múltiples condicionales, y acoplamiento inapropiado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). No se han identificado patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 107 puntos.

### Clase Analizada: `MesaData`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - `cargarMesasArchivo`: Este método es extenso y realiza múltiples tareas, incluyendo la apertura de un archivo, la lectura de líneas, el procesamiento de datos y la creación de objetos `Mesa`. La longitud y complejidad de este método dificultan su comprensión y mantenimiento.

##### Dispensables

- **Comentarios (+2):**
  - Existen algunos comentarios que intentan aclarar la lógica del código, lo que sugiere que el código no es lo suficientemente claro por sí mismo. En lugar de comentarios, se podrían utilizar nombres de métodos y variables más descriptivos.

#### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `MesaData` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de lectura/escritura de archivos, la manipulación de datos de mesas, y la gestión de excepciones.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - Aunque no se encuentran directamente sentencias *switch*, el uso de múltiples condicionales (`if-else`) en métodos como `cargarMesasArchivo` para manejar diferentes estados y datos de mesas podría beneficiarse de una refactorización utilizando el patrón de diseño Estrategia.

#### Acopladores

- **Intimidad inapropiada (+6):**
  - La clase `MesaData` accede frecuentemente a métodos y variables privadas de otras clases como `Mesa` y `UbicacionesMesas`, lo que aumenta el acoplamiento y dificulta el mantenimiento.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `MesaData` viola este principio al tener múltiples responsabilidades. Maneja la lectura y escritura de archivos, la creación y manipulación de objetos `Mesa`, y la gestión de excepciones. Cada una de estas responsabilidades debería estar en clases separadas para facilitar el mantenimiento y la evolución del código.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `MesaData` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de datos de mesas y la interacción con el sistema de archivos. Debería depender de interfaces o clases abstractas para reducir el acoplamiento y aumentar la flexibilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20):**
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Por ejemplo, una fábrica abstracta podría crear diferentes tipos de `Mesa` sin que `MesaData` tenga que conocer las clases específicas.

- **Método de Fábrica (+20):**
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos. Esto puede reducir la complejidad y mejorar la flexibilidad del código, permitiendo que `MesaData` delegue la creación de mesas a métodos de fábrica.

#### Estructurales

- **Adaptador (+25):**
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas. Por ejemplo, un adaptador podría permitir que la clase `Mesa` trabaje con diferentes tipos de almacenamiento o servicios.

- **Fachada (+20):**
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema. Por ejemplo, una fachada podría simplificar la interacción con el sistema de gestión de datos de mesas.

#### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor. Por ejemplo, la validación de datos de mesas podría pasar por una cadena de validadores.

- **Comando (+20):**
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes. Por ejemplo, las acciones de lectura y escritura de datos podrían ser comandos que se pueden deshacer y rehacer.

- **Iterador (+15):**
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente. Esto sería útil para iterar sobre los elementos de las mesas de manera uniforme.

- **Observador (+25):**
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto. Por ejemplo, las vistas de mesas podrían observar cambios en los datos de `Mesa` y actualizarse automáticamente.

- **Estrategia (+20):**
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Por ejemplo, se podrían definir diferentes estrategias para ordenar y filtrar elementos en las listas de mesas.

- **Método Plantilla (+25):**
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases. Por ejemplo, los procesos de lectura y manipulación de datos de mesas podrían seguir un método plantilla con pasos personalizables.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 0) = (5 + 6 + 2 + 6) + (30 + 45) + 0 = 94
\]

La clase `MesaData` presenta varios malos olores de código, como métodos largos, uso de múltiples condicionales, y acoplamiento inapropiado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). No se han identificado patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 94 puntos.

### Clase Analizada: `ComidaData`

#### Identificación de Olores de Código

##### Acaparadores

- **Método Largo (+5):**
  - El método `cargarComidasArchivo` realiza múltiples tareas, como abrir un archivo, leer datos, dividir líneas y crear instancias de `Comida`. Este método debería dividirse en métodos más pequeños y específicos para mejorar la legibilidad y el mantenimiento.

##### Dispensables

- **Comentarios (+2):**
  - Existen comentarios que describen el código en lugar de explicar el porqué del código. Estos comentarios podrían evitarse si el código fuera más claro y autoexplicativo.

- **Código duplicado (+7):**
  - Los métodos `registrarComida`, `eliminarComida` y `sobreescribirArchivoComida` tienen estructuras similares y contienen código repetido. Estos métodos podrían ser refactorizados para eliminar duplicación.

##### Acopladores

- **Cadenas de mensajes (+7):**
  - El método `cargarComidasArchivo` y otros métodos dependen fuertemente en varias clases y métodos para completar sus tareas, lo que aumenta el acoplamiento y reduce la flexibilidad del código.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `ComidaData` viola este principio al manejar múltiples responsabilidades, como la gestión de datos de comidas y la lectura/escritura de archivos. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `ComidaData` depende directamente de la implementación concreta de `BufferedReader`, `BufferedWriter`, `FileReader` y `FileWriter`. En su lugar, debería depender de abstracciones que puedan ser fácilmente sustituidas.

### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Consejo: Usa un Factory Method para la creación de instancias de `Comida`. Esto podría simplificar el código y mejorar la extensibilidad.

#### Estructurales

- **Adapter (+25):**
  - Consejo: Implementa el patrón Adapter para adaptar la lectura y escritura de archivos a una interfaz común, permitiendo cambiar fácilmente la implementación subyacente sin afectar al resto del código.

#### De comportamiento

- **Command (+20):**
  - Consejo: Usa el patrón Command para encapsular todas las solicitudes de acción en un objeto, lo que permite parametrizar los métodos `registrarComida`, `eliminarComida` y `sobreescribirArchivoComida`.

- **Observer (+25):**
  - Consejo: Implementa el patrón Observer para notificar automáticamente a las listas de comidas cuando se agregan, editan o eliminan comidas.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(21, 75, 90) = (5 + 2 + 7 + 7) + (30 + 45) + (20 + 25 + 20 + 25) = 166
\]

La clase `ComidaData` presenta varios malos olores de código, como métodos largos, código duplicado y cadenas de mensajes. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 166 puntos.


Este repositorio fue obtenido de: https://github.com/CristopherVilla20/Proyecto2Parcial
