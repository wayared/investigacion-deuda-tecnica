# Informe de Análisis de Deuda Técnica

### Clase Analizada: `PanelP`

## Identificación de Olores de Código

### Acaparadores

- **Método Largo (+5):**
  - El método `PanelPrincipal()` tiene más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6):**
  - La clase `PanelP` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica de archivo y construir representaciones gráficas.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos complejos, como los detalles de los archivos y parámetros de la interfaz.

- **Lista de Parámetros Largos (+4):**
  - El método `buildRectangules(Pane pane, Tree<Archivo> tree, double ancho, double largo, int direccion, double coordenadaX, double coordenadaY)` tiene una lista de parámetros larga.

- **Grupos de Datos (+3):**
  - Las variables `ancho`, `largo`, `direccion`, `coordenadaX` y `coordenadaY` en el método `buildRectangules` siempre se usan juntas y podrían encapsularse en una clase `Dimensiones`.

### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - El método `buildRectangules` utiliza sentencias condicionales anidadas para manejar diferentes condiciones.

### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `PanelP` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de archivo o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de archivo requieren modificaciones en múltiples métodos y clases relacionadas.

### Dispensables

- **Comentarios (+2):**
  - Existen muchos comentarios en el método `PanelPrincipal()` que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):**
  - El código para manejar archivos y directorios se repite en varios lugares de la clase `PanelP`.

- **Código muerto (+3):**
  - Existen métodos y variables no utilizados.

### Acopladores

- **Envidia de características (+5):**
  - El método `buildRectangules` utiliza intensivamente métodos de la clase `Tree`.

- **Intimidad inapropiada (+6):**
  - La clase `PanelP` accede frecuentemente a métodos y variables privadas de la clase `Tree`.

- **Cadenas de mensajes (+7):**
  - El método `buildRectangules` realiza varias llamadas en cadena a métodos de la clase `Tree`.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `PanelP` tiene múltiples responsabilidades, como gestionar la interfaz de usuario, manejar la lógica de archivo y construir representaciones gráficas.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `PanelP` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `buildRectangules`.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `PanelP` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de archivo.

## Patrones de diseño no utilizados

### Creacionales

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes tipos de representaciones gráficas sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `PanelP`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de representaciones gráficas y reducir la complejidad en `PanelP`.

### Estructurales

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de archivos.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de archivos y directorios.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de archivo de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de archivos.

### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de archivo, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de archivo.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de archivos sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `PanelP`.

- **Observador (+25):**
  - Podría permitir que un objeto `PanelP` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `PanelP` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de representación gráfica, encapsular cada uno, y hacerlos intercambiables en `PanelP`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de representación gráfica en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
  - Podría separar un algoritmo de representación gráfica de la estructura de objeto `Archivo` sobre la que opera.

### Clase Analizada: `CrearMapa`

## Identificación de Olores de Código

### Acaparadores

- **Método Largo (+5):**
  - El método `buildRectangules` tiene más de 20 líneas, dificultando su lectura y comprensión.

- **Clase Grande (+6):**
  - La clase `CrearMapa` tiene múltiples responsabilidades, como gestionar la lógica de archivos y construir representaciones gráficas.

- **Obsesión Primitiva (+3):**
  - Uso de tipos primitivos para representar datos complejos, como los detalles de los archivos y parámetros de la interfaz.

- **Lista de Parámetros Largos (+4):**
  - El método `buildRectangules(Pane pane, Tree<Archivo> tree, double ancho, double largo, int direccion, double coordenadaX, double coordenadaY)` tiene una lista de parámetros larga.

- **Grupos de Datos (+3):**
  - Las variables `ancho`, `largo`, `direccion`, `coordenadaX` y `coordenadaY` en el método `buildRectangules` siempre se usan juntas y podrían encapsularse en una clase `Dimensiones`.

### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):**
  - El método `buildRectangules` utiliza sentencias condicionales anidadas para manejar diferentes condiciones.

### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `CrearMapa` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de archivo o actualizar la interfaz de usuario.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de archivo requieren modificaciones en múltiples métodos y clases relacionadas.

### Dispensables

- **Comentarios (+2):**
  - Existen muchos comentarios en el método `createContent()` que podrían evitarse con un código más claro y autoexplicativo.

- **Código duplicado (+7):**
  - El código para manejar archivos y directorios se repite en varios lugares de la clase `CrearMapa`.

- **Código muerto (+3):**
  - Existen métodos y variables no utilizados.

### Acopladores

- **Envidia de características (+5):**
  - El método `buildRectangules` utiliza intensivamente métodos de la clase `Tree`.

- **Intimidad inapropiada (+6):**
  - La clase `CrearMapa` accede frecuentemente a métodos y variables privadas de la clase `Tree`.

- **Cadenas de mensajes (+7):**
  - El método `buildRectangules` realiza varias llamadas en cadena a métodos de la clase `Tree`.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `CrearMapa` tiene múltiples responsabilidades, como gestionar la lógica de archivos y construir representaciones gráficas.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `CrearMapa` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `buildRectangules`.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `CrearMapa` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de archivo.

## Patrones de diseño no utilizados

### Creacionales

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes tipos de representaciones gráficas sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `CrearMapa`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de representaciones gráficas y reducir la complejidad en `CrearMapa`.

### Estructurales

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de archivos.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de archivos y directorios.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de archivo de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de archivos.

### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de archivo, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de archivo.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de archivos sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `CrearMapa`.

- **Observador (+25):**
  - Podría permitir que un objeto `CrearMapa` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `CrearMapa` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de representación gráfica, encapsular cada uno, y hacerlos intercambiables en `CrearMapa`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de representación gráfica en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
  - Podría separar un algoritmo de representación gráfica de la estructura de objeto `Archivo` sobre la que opera.


### Clase Analizada: `ED2G9`

## Identificación de Olores de Código

### Acaparadores

- **Método Largo (+5):**
  - El método `start` tiene una longitud considerable, aunque no supera las 20 líneas, la cantidad de configuraciones iniciales podría dificultar su lectura y comprensión si crece en el futuro.

- **Clase Grande (+6):**
  - La clase `ED2G9` tiene la responsabilidad de inicializar la aplicación y manejar la lógica de la interfaz gráfica, lo cual puede hacerla crecer en tamaño.

### Preventores de Cambio

- **Cambio divergente (+6):**
  - La clase `ED2G9` podría necesitar cambios frecuentes debido a su responsabilidad de inicializar la aplicación, configurar la interfaz gráfica y gestionar eventos.

- **Cirugía de escopeta (+8):**
  - Cambios pequeños en la lógica de inicialización podrían requerir modificaciones en múltiples métodos y clases relacionadas.

### Acopladores

- **Envidia de características (+5):**
  - El método `start` utiliza intensivamente métodos de la clase `PanelP`.

- **Cadenas de mensajes (+7):**
  - El método `start` realiza llamadas en cadena a métodos de la clase `PanelP` para la configuración de la interfaz.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `ED2G9` tiene múltiples responsabilidades, como inicializar la aplicación y configurar la interfaz gráfica, lo que viola este principio.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase `ED2G9` no es fácilmente extensible sin modificar su código fuente, especialmente en el método `start`.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `ED2G9` depende directamente de implementaciones concretas, como `PanelP`, en lugar de abstracciones.

## Patrones de diseño no utilizados

### Creacionales

- **Fábrica Abstracta (+20):**
  - Podría utilizarse para crear diferentes configuraciones de interfaz gráfica sin especificar sus clases concretas.

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de `ED2G9`.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de configuraciones de interfaz gráfica y reducir la complejidad en `ED2G9`.

### Estructurales

- **Adaptador (+25):**
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de configuraciones de interfaz.

- **Compuesto (+30):**
  - Podría ser útil para representar jerarquías de componentes de la interfaz gráfica.

- **Decorador (+25):**
  - Podría usarse para añadir responsabilidades a objetos de configuración de interfaz de manera dinámica.

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de configuración de interfaz gráfica.

### De comportamiento

- **Cadena de Responsabilidad (+30):**
  - Podría permitir que múltiples objetos manejen una solicitud de configuración de interfaz, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):**
  - Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de configuración de interfaz.

- **Iterador (+15):**
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de configuraciones de interfaz sin exponer su representación subyacente.

- **Mediador (+30):**
  - Podría reducir las dependencias caóticas entre objetos de la clase `ED2G9`.

- **Observador (+25):**
  - Podría permitir que un objeto `ED2G9` notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto `ED2G9` altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de configuración de interfaz gráfica, encapsular cada uno, y hacerlos intercambiables en `ED2G9`.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de un algoritmo de configuración de interfaz gráfica en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):**
  - Podría separar un algoritmo de configuración de interfaz gráfica de la estructura de objeto `PanelP` sobre la que opera.


### Clase Analizada: `Pintura`

## Identificación de Olores de Código

### Acaparadores

- **Obsesión Primitiva (+3):**
  - La clase `Pintura` utiliza tipos primitivos (`double`) para representar los componentes de color (`red`, `green`, `blue`) en lugar de encapsularlos en una estructura más significativa.

## Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `Pintura` se centra exclusivamente en representar un color y no tiene múltiples responsabilidades, por lo que no viola este principio.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase `Pintura` no depende de implementaciones concretas y utiliza tipos primitivos, por lo que no viola este principio.




Este repositorio fue obtenido de: https://github.com/RicardoMolinaCoronel/PROYECTOED2
