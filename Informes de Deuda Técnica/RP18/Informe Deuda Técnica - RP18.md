# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `Emoji`

#### Identificación de Olores de Código

##### Dispensables

- **Código Duplicado (+7):**
  - Los métodos `setImageCuerpo`, `setImageOjos`, `setImageBoca`, `setImageAccesorios` y `setImageCejas` tienen código muy similar. La única diferencia es el campo que se está evaluando y el tamaño de la imagen que se establece. Esta duplicación puede ser refactorizada para reducir el tamaño del código y hacerlo más mantenible. La repetición de lógica en estos métodos incrementa la probabilidad de errores y dificulta el mantenimiento.

##### Acopladores

- **Envidia de características (+5):**
  - La clase `Emoji` accede y manipula intensamente objetos de la clase `ImageView`, lo cual podría sugerir que parte de esta funcionalidad debería pertenecer a una clase relacionada con la presentación de la imagen. La clase `Emoji` debería centrarse únicamente en la lógica de negocio, dejando la lógica de presentación a otra clase.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Emoji` tiene múltiples responsabilidades: almacenar datos de partes del emoji y manejar la visualización de imágenes de esas partes. Esta clase podría beneficiarse de una separación de responsabilidades, creando una clase específica para manejar la lógica de visualización de las imágenes. Actualmente, cualquier cambio en la lógica de presentación afectará esta clase.

- **Principio de Abierto/Cerrado (OCP) (+40):**
  - La clase `Emoji` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `settearPartes`. Si se quisiera añadir una nueva parte del emoji, sería necesario modificar este método. Esto va en contra del principio de que las clases deben estar abiertas para la extensión, pero cerradas para la modificación.

### Patrones de diseño no utilizados

#### Creacionales

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de `ImageView` en un método separado, permitiendo crear instancias de `ImageView` basadas en diferentes partes del emoji sin duplicar el código.

    **Consejo:** Utilizar un Método de Fábrica para centralizar la creación de los objetos `ImageView` y así evitar la duplicación de código.

#### Estructurales

- **Adaptador (+25):**
  - Podría utilizarse para permitir que `Emoji` y `ImageView` trabajen juntos de manera más efectiva, especialmente si `ImageView` proviene de una biblioteca de terceros y no se puede modificar directamente.

    **Consejo:** Implementar un Adaptador para que la clase `Emoji` pueda interactuar de manera más flexible con `ImageView`.


[E(o,s,p)=E(1,2,0)=(7+5)+(30+40)+(20+25)=127]

La clase Emoji presenta varios malos olores de código, como código duplicado y envidia de características. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Abierto/Cerrado (OCP). El esfuerzo estimado para refactorizar esta clase es de 127 puntos.

### Clase Analizada: `Seleccionador`

#### Identificación de Olores de Código

##### Dispensables

- **Comentarios (+2):**
  - Hay comentarios en el código que podrían ser eliminados si el código fuera más claro y autoexplicativo.

- **Código Duplicado (+7):**
  - Los métodos `seleccionarComponente`, `cargarEmoji`, `guardarEmoji` y `exportarEmoji` contienen lógica repetitiva para manejar la selección de archivos y directorios. Esta duplicación puede ser refactorizada para mejorar la mantenibilidad.

##### Acopladores

- **Dependencia de Implementación (+5):**
  - La clase depende directamente de implementaciones concretas de `FileChooser`, `DirectoryChooser`, `ObjectInputStream`, `ObjectOutputStream`, `FileOutputStream`, y `BufferedImage`. Esto dificulta la extensión y modificación de la clase.

##### Cambiadores

- **Métodos que Cambian Estado Externo (+5):**
  - Los métodos `seleccionarComponente`, `cargarEmoji`, `guardarEmoji` y `exportarEmoji` realizan operaciones de entrada/salida que pueden cambiar el estado externo del sistema, como el sistema de archivos. Estos métodos podrían beneficiarse de una separación de la lógica de negocio de las operaciones de E/S.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Seleccionador` tiene múltiples responsabilidades, incluyendo la selección de archivos, carga y guardado de objetos `Emoji`, y la exportación de imágenes. Esta clase debería dividirse en varias clases con responsabilidades únicas.

- **Principio de Abierto/Cerrado (OCP) (+40):**
  - La clase `Seleccionador` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos relacionados con la selección y exportación de archivos. Si se quisiera añadir soporte para nuevos tipos de archivos, sería necesario modificar esta clase, lo que va en contra del principio OCP.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de `FileChooser` y `DirectoryChooser`, permitiendo crear instancias de estos objetos de manera más flexible y sin duplicación de código.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de objetos `FileChooser` y `DirectoryChooser`.

#### Estructurales

- **Facade (+25):**
  - Podría implementarse para proporcionar una interfaz simplificada para la selección de archivos y directorios, y la gestión de objetos `Emoji`.

    **Consejo:** Implementar un patrón Facade para manejar la lógica de selección de archivos y directorios, y la carga/guardado de objetos `Emoji`.

#### De comportamiento

- **Command (+30):**
  - Podría utilizarse para encapsular las solicitudes de selección, carga, guardado y exportación en objetos de comando, permitiendo una mayor flexibilidad en la ejecución de estas operaciones.

    **Consejo:** Utilizar el patrón Command para encapsular las operaciones de selección, carga, guardado y exportación de `Emoji`.

[E(o,s,p)=E(2,2,0)=(2+7+5)+(30+40)+(20+25+30)=159]

La clase Seleccionador presenta varios malos olores de código, como comentarios innecesarios, código duplicado y dependencia de implementación concreta. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Abierto/Cerrado (OCP). El esfuerzo estimado para refactorizar esta clase es de 159 puntos.

### Clase Analizada: `BienvenidaController`

#### Identificación de Olores de Código

##### Dispensables

- **Comentarios (+2):**
  - Existen comentarios que podrían ser eliminados si el código fuera más claro y autoexplicativo.

##### Acopladores

- **Dependencia de Implementación (+5):**
  - La clase depende directamente de implementaciones concretas de `FileInputStream`, `Image`, y `Map.Entry`, lo que dificulta la extensión y modificación de la clase.

##### Cambiadores

- **Métodos que Cambian Estado Externo (+5):**
  - Los métodos `limpiarHistorial` y `cargarEmoji` realizan operaciones que cambian el estado externo del sistema, como la limpieza de la lista de emojis y la carga de archivos. Estos métodos podrían beneficiarse de una separación de la lógica de negocio de las operaciones de E/S.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `BienvenidaController` tiene múltiples responsabilidades, incluyendo la gestión de la interfaz de usuario, la carga y limpieza de emojis, y la navegación entre escenas. Esta clase debería dividirse en varias clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase depende directamente de implementaciones concretas en lugar de abstraer estas dependencias. Por ejemplo, en lugar de depender directamente de `FileInputStream`, podría depender de una interfaz que maneje la lectura de archivos.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de objetos `Image`, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de objetos `Image` y `ImageView`.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de la interfaz gráfica de usuario, permitiendo tratar tanto a los componentes individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar un patrón Composite para manejar los componentes de la interfaz gráfica de usuario.

#### De comportamiento

- **Observer (+30):**
  - Podría utilizarse para notificar automáticamente a la interfaz de usuario cuando se produce un cambio en los datos del modelo, en lugar de tener que actualizar manualmente la interfaz.

    **Consejo:** Utilizar el patrón Observer para actualizar automáticamente la interfaz de usuario cuando se cambian los datos del modelo.
    
####Cálculo del Esfuerzo de Refactorización

[E(o,s,p)=E(2,2,0)=(2+5+5)+(30+45)+(20+25+30)=164]

La clase BienvenidaController presenta varios malos olores de código, como comentarios innecesarios, dependencia de implementación concreta y métodos que cambian el estado externo. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 164 puntos.

### Clase Analizada: `SecondaryController`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `SecondaryController` maneja múltiples responsabilidades, incluyendo la gestión de eventos de interfaz de usuario, la carga de imágenes, la manipulación de partes de un emoji y la lógica de negocio para el guardado y la exportación. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - `initialize`: Este método realiza múltiples operaciones de inicialización, haciéndolo largo y difícil de mantener.

##### Dispensables

- **Comentarios (+2):**
  - Existen comentarios que podrían ser eliminados si el código fuera más claro y autoexplicativo.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+4):**
  - La clase tiene varios métodos *getter* y *setter* que no agregan lógica adicional, lo cual puede ser una señal de un diseño pobre orientado a objetos.

##### Cambiadores

- **Métodos que Cambian Estado Externo (+5):**
  - Los métodos `guardarEmoji`, `agregarComponentes` y `mostrarPartes` realizan operaciones que cambian el estado externo del sistema, como la manipulación de la interfaz de usuario y la escritura de archivos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `SecondaryController` tiene múltiples responsabilidades, incluyendo la gestión de la interfaz de usuario, la manipulación de partes del emoji, y la lógica de guardado y exportación. Esta clase debería dividirse en varias clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase depende directamente de implementaciones concretas en lugar de abstraer estas dependencias. Por ejemplo, en lugar de depender directamente de `File`, `Image`, y `ImageView`, podría depender de interfaces o abstracciones.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para encapsular la creación de objetos `ImageView`, permitiendo una creación más flexible y centralizada de estos objetos.

    **Consejo:** Utilizar el patrón Factory Method para centralizar la creación de objetos `ImageView`.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura del panel de emojis, permitiendo tratar tanto a los componentes individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar un patrón Composite para manejar los componentes del panel de emojis.

#### De comportamiento

- **Observer (+30):**
  - Podría utilizarse para notificar automáticamente a la interfaz de usuario cuando se produce un cambio en los datos del modelo, en lugar de tener que actualizar manualmente la interfaz.

    **Consejo:** Utilizar el patrón Observer para actualizar automáticamente la interfaz de usuario cuando se cambian los datos del modelo.

#### Cálculo del Esfuerzo de Refactorización
[E(o,s,p)=E(6,2,0)=(6+5+2+4+5)+(30+45)+(20+25+30)=172]

Este repositorio fue obtenido de: https://github.com/ZarateSofia/ProyectoEDD
