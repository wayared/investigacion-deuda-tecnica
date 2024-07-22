# Informe de Análisis de Deuda Técnica

## Clase Analizada: `AlertBoxes`

### Identificación de Olores de Código

#### Acaparadores
**Método Largo (+5)**
- `multiButtons` y `inputTextAlert`: Ambos métodos contienen más de 20 líneas, dificultando su lectura y comprensión.

**Clase Grande (+6)**
- `AlertBoxes`: La clase maneja múltiples tipos de alertas y contiene varios métodos, lo que sugiere que tiene múltiples responsabilidades.

**Obsesión Primitiva (+3)**
- `infoAlert`, `warnningAlert`, `errorAlert`, `confirmAlert`, `multiButtons`, `inputTextAlert`: Uso de tipos primitivos para representar datos complejos, como el título, encabezado y contenido de las alertas.

**Lista de Parámetros Largos (+4)**
- `infoAlert`, `warnningAlert`, `errorAlert`, `confirmAlert`, `multiButtons`, `inputTextAlert`: Estos métodos tienen una lista de parámetros larga.

**Grupos de Datos (+3)**
- Las variables `title`, `header` y `content` siempre se usan juntas y podrían encapsularse en una clase `AlertData`.

#### Abusadores de Orientación a Objetos
**Sentencias Switch (+5)**
- `multiButtons`: Utiliza varias sentencias switch para manejar diferentes tipos de botones.

#### Preventores de Cambio
**Cambio divergente (+6)**
- `AlertBoxes`: La clase tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de alertas o actualizar la interfaz de usuario.

**Cirugía de escopeta (+8)**
- Cambios pequeños en la lógica de alertas requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
**Comentarios (+2)**
- Existen muchos comentarios en los métodos que podrían evitarse con un código más claro y autoexplicativo.

**Código duplicado (+7)**
- El código para configurar y mostrar alertas se repite en varios métodos de la clase `AlertBoxes`.

**Clase de datos (+5)**
- La clase `AlertBoxes` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de constantes de tipo de alerta.

**Código muerto (+3)**
- Existen variables y comentarios no utilizados (e.g., `CONSTANTS` no se usa en la lógica del código).

#### Acopladores
**Envidia de características (+5)**
- La clase `AlertBoxes` depende intensamente de la clase `Alert` de JavaFX.

#### Violaciones de los Principios SOLID
**Principio de Responsabilidad Única (SRP) (+30)**
- La clase `AlertBoxes` tiene múltiples responsabilidades, como gestionar diferentes tipos de alertas.

**Principio Abierto/Cerrado (OCP) (+40)**
- La clase `AlertBoxes` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos que manejan diferentes tipos de alertas.

**Principio de Inversión de Dependencias (DIP) (+45)**
- La clase `AlertBoxes` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de alertas.

### Patrones de diseño no utilizados

#### Creacionales
**Fábrica Abstracta (+20)**
- Podría utilizarse para crear diferentes tipos de alertas sin especificar sus clases concretas.

**Constructor (+25)**
- Utilizar un constructor para simplificar la creación de instancias complejas de `AlertBoxes`.

**Método de Fábrica (+20)**
- Podría usarse para encapsular la creación de alertas y reducir la complejidad en `AlertBoxes`.

#### Estructurales
**Adaptador (+25)**
- Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la creación de alertas.

**Decorador (+25)**
- Podría usarse para añadir responsabilidades a objetos de alerta de manera dinámica.

**Fachada (+20)**
- Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de alertas.

#### De comportamiento
**Cadena de Responsabilidad (+30)**
- Podría permitir que múltiples objetos manejen una solicitud de alerta, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20)**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de alerta.

**Mediador (+30)**
- Podría reducir las dependencias caóticas entre objetos de la clase `AlertBoxes`.

**Observador (+25)**
- Podría permitir que un objeto `AlertBoxes` notifique a otros objetos sobre cambios en su estado.

**Estrategia (+20)**
- Podría definir una familia de algoritmos de alerta, encapsular cada uno, y hacerlos intercambiables en `AlertBoxes`.

**Método Plantilla (+25)**
- Podría definir el esqueleto de un algoritmo de alerta en una operación, dejando algunos pasos a las subclases.

**Visitante (+35)**
- Podría separar un algoritmo de alerta de la estructura de objeto `Alert` sobre la que opera.

## Clase Analizada: `EstadisticasController`

### Identificación de Olores de Código

#### Acaparadores
**Método Largo (+5)**
- El método `initialize` contiene más de 20 líneas, dificultando su lectura y comprensión.

**Clase Grande (+6)**
- `EstadisticasController`: La clase maneja múltiples responsabilidades, como la configuración de la interfaz de usuario y la lógica de conteo de palabras.

**Obsesión Primitiva (+3)**
- `initialize`, `cantidad_palabras`, `contar_palabras`, `regresar`, `letras`: Uso de tipos primitivos para representar datos complejos, como el título, encabezado y contenido de las columnas de la tabla.

**Lista de Parámetros Largos (+4)**
- No se observan métodos con listas de parámetros largas en esta clase específica.

**Grupos de Datos (+3)**
- Las variables `title`, `header` y `content` en métodos similares a los de `AlertBoxes` no están presentes, pero las configuraciones de las columnas podrían encapsularse.

#### Abusadores de Orientación a Objetos
**Sentencias Switch (+5)**
- El método `contar_palabras` utiliza un bucle para manejar diferentes letras del alfabeto, que podría beneficiarse de una estructura más orientada a objetos.

#### Preventores de Cambio
**Cambio divergente (+6)**
- `EstadisticasController`: La clase tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de conteo de palabras o actualizar la interfaz de usuario.

**Cirugía de escopeta (+8)**
- Cambios pequeños en la lógica de conteo de palabras requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
**Comentarios (+2)**
- Existen comentarios mínimos en los métodos que podrían evitarse con un código más claro y autoexplicativo.

**Código duplicado (+7)**
- El código para configurar y mostrar las columnas de la tabla se repite en varios lugares de la clase `EstadisticasController`.

**Clase de datos (+5)**
- La clase `EstadisticasController` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de constantes de tipo de columna.

**Código muerto (+3)**
- No se observa código muerto en esta clase específica.

#### Acopladores
**Envidia de características (+5)**
- La clase `EstadisticasController` depende intensamente de la clase `TableView` de JavaFX.

#### Violaciones de los Principios SOLID
**Principio de Responsabilidad Única (SRP) (+30)**
- La clase `EstadisticasController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario y manejar la lógica de conteo de palabras.

**Principio Abierto/Cerrado (OCP) (+40)**
- La clase `EstadisticasController` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos que manejan diferentes tipos de conteo de palabras.

**Principio de Inversión de Dependencias (DIP) (+45)**
- La clase `EstadisticasController` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la interfaz de usuario y lógica de conteo de palabras.

### Patrones de diseño no utilizados

#### Creacionales
**Fábrica Abstracta (+20)**
- Podría utilizarse para crear diferentes tipos de columnas sin especificar sus clases concretas.

**Constructor (+25)**
- Utilizar un constructor para simplificar la creación de instancias complejas de `EstadisticasController`.

**Método de Fábrica (+20)**
- Podría usarse para encapsular la creación de columnas y reducir la complejidad en `EstadisticasController`.

#### Estructurales
**Adaptador (+25)**
- Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la creación de tablas.

**Decorador (+25)**
- Podría usarse para añadir responsabilidades a objetos de tabla de manera dinámica.

**Fachada (+20)**
- Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de conteo de palabras.

#### De comportamiento
**Cadena de Responsabilidad (+30)**
- Podría permitir que múltiples objetos manejen una solicitud de conteo de palabras, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20)**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de conteo de palabras.

**Mediador (+30)**
- Podría reducir las dependencias caóticas entre objetos de la clase `EstadisticasController`.

**Observador (+25)**
- Podría permitir que un objeto `EstadisticasController` notifique a otros objetos sobre cambios en su estado.

**Estrategia (+20)**
- Podría definir una familia de algoritmos de conteo de palabras, encapsular cada uno, y hacerlos intercambiables en `EstadisticasController`.

**Método Plantilla (+25)**
- Podría definir el esqueleto de un algoritmo de conteo de palabras en una operación, dejando algunos pasos a las subclases.

**Visitante (+35)**
- Podría separar un algoritmo de conteo de palabras de la estructura de objeto `TableView` sobre la que opera.


## Clase Analizada: `Data`

### Identificación de Olores de Código

#### Acaparadores
**Clase Grande**
- No aplica, ya que la clase `Data` es pequeña y tiene una responsabilidad clara.

**Método Largo**
- No aplica, ya que ninguno de los métodos supera las 20 líneas.

**Obsesión Primitiva**
- La clase utiliza tipos primitivos (`String` e `int`) apropiadamente para representar datos.

**Lista de Parámetros Largos**
- No aplica, ya que los métodos no tienen listas de parámetros largas.

**Grupos de Datos**
- No se identifican grupos de datos que se usen frecuentemente juntos fuera del contexto de los constructores y getters/setters.

#### Abusadores de Orientación a Objetos
**Sentencias Switch**
- No aplica, ya que no se utilizan sentencias switch en la clase.

#### Preventores de Cambio
**Cambio divergente**
- No aplica, ya que la clase tiene una responsabilidad específica y clara.

**Cirugía de escopeta**
- No aplica, ya que cambios en la clase no implicarían modificaciones extensivas en otros lugares.

#### Dispensables
**Comentarios**
- No hay comentarios innecesarios. La clase está suficientemente documentada.

**Código duplicado**
- No hay código duplicado identificado.

**Clase de datos**
- La clase `Data` actúa principalmente como una estructura de datos, lo cual es apropiado para su propósito.

**Código muerto**
- No se identifica código muerto en la clase.

#### Acopladores
**Envidia de características**
- No se observa envidia de características, ya que la clase no depende intensamente de métodos de otras clases.

### Violaciones de los Principios SOLID
**Principio de Responsabilidad Única (SRP)**
- La clase sigue el principio de responsabilidad única, ya que solo almacena y gestiona datos.

**Principio Abierto/Cerrado (OCP)**
- La clase podría ser extendida sin modificar su código actual.

**Principio de Inversión de Dependencias (DIP)**
- La clase no depende de implementaciones concretas, ya que maneja tipos primitivos.

### Patrones de diseño no utilizados

#### Creacionales
**Fábrica Abstracta**
- No aplica, ya que la clase no necesita crear diferentes tipos de objetos de una manera abstracta.

**Constructor**
- No se necesita un constructor complejo para esta clase simple.

**Método de Fábrica**
- No aplica, ya que la clase no necesita encapsular la creación de instancias de sí misma o de otros objetos.

#### Estructurales
**Adaptador**
- No aplica, ya que la clase no necesita permitir que clases con interfaces incompatibles trabajen juntas.

**Decorador**
- No se necesita añadir responsabilidades a objetos de manera dinámica para esta clase simple.

**Fachada**
- No aplica, ya que la clase no necesita proporcionar una interfaz simplificada a un conjunto de interfaces.

#### De comportamiento
**Cadena de Responsabilidad**
- No aplica, ya que la clase no maneja solicitudes que puedan ser procesadas por diferentes objetos.

**Comando**
- No es necesario encapsular solicitudes como objetos para esta clase.

**Mediador**
- No se requiere reducir dependencias entre objetos en esta clase simple.

**Observador**
- No aplica, ya que la clase no necesita notificar a otros objetos sobre cambios en su estado.

**Estrategia**
- No aplica, ya que la clase no necesita definir una familia de algoritmos intercambiables.

**Método Plantilla**
- No aplica, ya que no hay algoritmos complejos que requieran una estructura de plantilla.

**Visitante**
- No es necesario separar un algoritmo de la estructura de objeto sobre la que opera para esta clase.

  
## Clase Analizada: `FXMLController`

### Identificación de Olores de Código

#### Acaparadores
**Método Largo (+5)**
- `initialize` y `gameMode` contienen más de 20 líneas, dificultando su lectura y comprensión.

**Clase Grande (+6)**
- La clase `FXMLController` maneja múltiples responsabilidades, como la configuración de la interfaz de usuario, la gestión de datos y la lógica de un juego.

**Obsesión Primitiva (+3)**
- Uso de tipos primitivos para representar datos complejos, como las palabras y puntuaciones en el juego.

**Grupos de Datos (+3)**
- Las variables `txtField`, `load`, `eliminar`, `estadisticas`, `buscar`, `insertar`, `game`, `check`, `fillTable`, `hbox`, `score`, `puntosLabel`, `table` y `tableTwo` podrían agruparse en una estructura para facilitar su gestión.

#### Preventores de Cambio
**Cambio divergente (+6)**
- La clase `FXMLController` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica del juego o actualizar la interfaz de usuario.

**Cirugía de escopeta (+8)**
- Cambios pequeños en la lógica de gestión de datos y juego requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
**Comentarios (+2)**
- No hay comentarios innecesarios. La clase está suficientemente documentada.

**Código duplicado (+7)**
- El código para cargar palabras en `loadTrieTree` y `insertarPalabra` tiene lógica similar que podría refactorizarse.

#### Acopladores
**Envidia de características (+5)**
- La clase `FXMLController` depende intensamente de la clase `Tree` y `AlertBoxes` para manejar su lógica.

### Violaciones de los Principios SOLID
**Principio de Responsabilidad Única (SRP) (+30)**
- La clase `FXMLController` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica del juego y la gestión de datos.

**Principio Abierto/Cerrado (OCP) (+40)**
- La clase podría ser extendida sin modificar su código actual en algunos casos, pero en otros no, debido a la mezcla de lógica de diferentes responsabilidades.

**Principio de Inversión de Dependencias (DIP) (+45)**
- La clase no sigue completamente este principio, ya que depende directamente de implementaciones concretas como `Tree` y `AlertBoxes`.

### Patrones de diseño no utilizados

#### Estructurales
**Adaptador (+25)**
- Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de datos.

**Fachada (+20)**
- Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gestión de datos y juego.

#### De comportamiento
**Comando (+20)**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de gestión de datos.

**Mediador (+30)**
- Podría reducir las dependencias caóticas entre objetos de la clase `FXMLController`.

**Estrategia (+20)**
- Podría definir una familia de algoritmos de gestión de datos, encapsular cada uno, y hacerlos intercambiables en `FXMLController`.

**Método Plantilla (+25)**
- Podría definir el esqueleto de un algoritmo de gestión de datos en una operación, dejando algunos pasos a las subclases.


Este repositorio fue obtenido de: https://github.com/wayared/Proyecto2-EDD
