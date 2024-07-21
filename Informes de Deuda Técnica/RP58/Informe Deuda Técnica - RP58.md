
## Clase Analizada: sb-admin-2.js

### Identificación de Olores de Código

#### Acaparadores

**Método Largo (+5):**
- El método anónimo dentro de la función principal contiene múltiples responsabilidades y líneas de código, especialmente el bloque para "Toggle the side navigation" y "Close any open menu accordions when window is resized below 768px", dificultando su lectura y comprensión.

**Clase Grande (+6):**
- La clase `sb-admin-2.js` tiene múltiples responsabilidades, como gestionar la navegación lateral, manejar eventos de scroll, y aplicar efectos de scroll suave.

**Obsesión Primitiva (+3):**
- Uso de tipos primitivos en varios lugares para manejar la lógica, como `scrollDistance` y `delta`.

**Grupos de Datos (+3):**
- Las variables `sidebarToggle` y `sidebarToggleTop` siempre se usan juntas y podrían encapsularse en una clase `SidebarToggle`.

#### Preventores de Cambio

**Cambio divergente (+6):**
- La clase `sb-admin-2.js` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de navegación o actualizar el comportamiento del scroll.

**Cirugía de escopeta (+8):**
- Cambios pequeños en la lógica de navegación requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

**Comentarios (+2):**
- Existen muchos comentarios explicativos que podrían evitarse con un código más claro y autoexplicativo.

**Código duplicado (+7):**
- El código para manejar el evento de scroll y la lógica de toggle de la barra lateral se repite en varias partes de la clase.

**Clase de datos (+5):**
- La clase `sb-admin-2.js` actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión de eventos de scroll.

### Acopladores

**Envidia de características (+5):**
- El método para manejar el evento de scroll utiliza intensivamente métodos de la clase `window`.

**Intimidad inapropiada (+6):**
- La clase `sb-admin-2.js` accede frecuentemente a métodos y variables privadas de la clase `window`.

**Cadenas de mensajes (+7):**
- El método para manejar el evento de scroll realiza varias llamadas en cadena a métodos de la clase `window`.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**
- La clase `sb-admin-2.js` tiene múltiples responsabilidades, como gestionar la navegación lateral y manejar eventos de scroll.

**Principio Abierto/Cerrado (OCP) (+40):**
- La clase `sb-admin-2.js` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos que manejan la lógica de navegación.

**Principio de Inversión de Dependencias (DIP) (+45):**
- La clase `sb-admin-2.js` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de navegación y eventos de scroll.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**
- Podría utilizarse para crear diferentes tipos de eventos de navegación sin especificar sus clases concretas.

**Constructor (+25):**
- Utilizar un constructor para simplificar la creación de instancias complejas de `sb-admin-2.js`.

**Método de Fábrica (+20):**
- Podría usarse para encapsular la creación de eventos de navegación y reducir la complejidad en `sb-admin-2.js`.

#### Estructurales

**Adaptador (+25):**
- Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de eventos de scroll.

**Compuesto (+30):**
- Podría ser útil para representar jerarquías de eventos de navegación.

**Decorador (+25):**
- Podría usarse para añadir responsabilidades a objetos de eventos de navegación de manera dinámica.

**Fachada (+20):**
- Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de navegación.

#### De comportamiento

**Cadena de Responsabilidad (+30):**
- Podría permitir que múltiples objetos manejen una solicitud de evento de scroll, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de navegación.

**Iterador (+15):**
- Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de eventos de navegación sin exponer su representación subyacente.

**Mediador (+30):**
- Podría reducir las dependencias caóticas entre objetos de la clase `sb-admin-2.js`.

**Observador (+25):**
- Podría permitir que un objeto `sb-admin-2.js` notifique a otros objetos sobre cambios en su estado.

**Estado (+30):**
- Podría permitir que un objeto `sb-admin-2.js` altere su comportamiento cuando su estado interno cambia.

**Estrategia (+20):**
- Podría definir una familia de algoritmos de navegación, encapsular cada uno, y hacerlos intercambiables en `sb-admin-2.js`.

**Método Plantilla (+25):**
- Podría definir el esqueleto de un algoritmo de navegación en una operación, dejando algunos pasos a las subclases.

**Visitante (+35):**
- Podría separar un algoritmo de navegación de la estructura de objeto `window` sobre la que opera.

## Clase Analizada: api.js

### Identificación de Olores de Código

#### Acaparadores

**Método Largo (+5):**
- El método `getStatisticsByBeer` contiene múltiples responsabilidades y líneas de código, especialmente el bloque para manipulación del DOM y procesamiento de datos, dificultando su lectura y comprensión.

**Clase Grande (+6):**
- La clase `api.js` tiene múltiples responsabilidades, como manejar las llamadas a la API, procesar datos, actualizar gráficos y manipular el DOM.

**Obsesión Primitiva (+3):**
- Uso de tipos primitivos en varios lugares para manejar la lógica, como las listas de `abvs`, `ibus`, `atts`, `beerNames` y `beerImages`.

**Grupos de Datos (+3):**
- Las variables `abvs`, `ibus`, `atts`, `beerNames` y `beerImages` siempre se usan juntas y podrían encapsularse en una clase `Beer`.

#### Preventores de Cambio

**Cambio divergente (+6):**
- La clase `api.js` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de manipulación del DOM o actualizar las llamadas a la API.

**Cirugía de escopeta (+8):**
- Cambios pequeños en la lógica de manipulación del DOM requieren modificaciones en múltiples métodos y partes de la clase.

#### Dispensables

**Comentarios (+2):**
- No se identificaron comentarios innecesarios en el código proporcionado.

**Código duplicado (+7):**
- El código para manejar las llamadas a la API y manipulación del DOM se repite en varias partes de la clase.

### Acopladores

**Envidia de características (+5):**
- El método `setStatisticsByBeer` utiliza intensivamente métodos de la biblioteca `Chart.js`.

**Intimidad inapropiada (+6):**
- La clase `api.js` accede frecuentemente a métodos y variables privadas de los elementos del DOM.

**Cadenas de mensajes (+7):**
- El método `getStatisticsByBeer` realiza varias llamadas en cadena a métodos de la biblioteca `Chart.js` y manipulación del DOM.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**
- La clase `api.js` tiene múltiples responsabilidades, como manejar las llamadas a la API, procesar datos, actualizar gráficos y manipular el DOM.

**Principio Abierto/Cerrado (OCP) (+40):**
- La clase `api.js` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos que manejan la lógica de manipulación del DOM y gráficos.

**Principio de Inversión de Dependencias (DIP) (+45):**
- La clase `api.js` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de manipulación del DOM y gráficos.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**
- Podría utilizarse para crear diferentes tipos de gráficos sin especificar sus clases concretas.

**Constructor (+25):**
- Utilizar un constructor para simplificar la creación de instancias complejas de `api.js`.

**Método de Fábrica (+20):**
- Podría usarse para encapsular la creación de gráficos y reducir la complejidad en `api.js`.

#### Estructurales

**Adaptador (+25):**
- Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de gráficos.

**Decorador (+25):**
- Podría usarse para añadir responsabilidades a objetos de gráficos de manera dinámica.

**Fachada (+20):**
- Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de gráficos y manipulación del DOM.

#### De comportamiento

**Cadena de Responsabilidad (+30):**
- Podría permitir que múltiples objetos manejen una solicitud de manipulación del DOM, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de manipulación del DOM.

**Iterador (+15):**
- Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de datos de gráficos sin exponer su representación subyacente.

**Mediador (+30):**
- Podría reducir las dependencias caóticas entre objetos de la clase `api.js`.

**Observador (+25):**
- Podría permitir que un objeto `api.js` notifique a otros objetos sobre cambios en su estado.

**Estado (+30):**
- Podría permitir que un objeto `api.js` altere su comportamiento cuando su estado interno cambia.

**Estrategia (+20):**
- Podría definir una familia de algoritmos de manipulación del DOM y gráficos, encapsular cada uno, y hacerlos intercambiables en `api.js`.

**Método Plantilla (+25):**
- Podría definir el esqueleto de un algoritmo de manipulación del DOM y gráficos en una operación, dejando algunos pasos a las subclases.

**Visitante (+35):**
- Podría separar un algoritmo de manipulación del DOM de la estructura de objeto `document` sobre la que opera.

# Informe de Análisis de Deuda Técnica
## Clase Analizada: gulpfile.js

### Identificación de Olores de Código

#### Acaparadores

**Método Largo (+5):**
- Los métodos `modules`, `css`, y `js` contienen múltiples responsabilidades y líneas de código, dificultando su lectura y comprensión.

**Clase Grande (+6):**
- La clase `gulpfile.js` tiene múltiples responsabilidades, como gestionar la construcción de CSS, JavaScript, mover dependencias de `node_modules` a `vendor`, y configurar `BrowserSync`.

**Obsesión Primitiva (+3):**
- Uso de tipos primitivos en varios lugares para manejar la lógica, como las listas de rutas de archivos.

**Grupos de Datos (+3):**
- Las rutas de archivos usadas en el método `modules` siempre se usan juntas y podrían encapsularse en una clase `FilePath`.

#### Preventores de Cambio

**Cambio divergente (+6):**
- La clase `gulpfile.js` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de construcción de CSS o actualizar las dependencias de `node_modules`.

**Cirugía de escopeta (+8):**
- Cambios pequeños en la lógica de construcción requieren modificaciones en múltiples métodos y partes de la clase.

#### Dispensables

**Código duplicado (+7):**
- El código para mover dependencias de `node_modules` a `vendor` se repite en varias partes del método `modules`.

### Acopladores

**Envidia de características (+5):**
- Los métodos `css` y `js` utilizan intensivamente métodos de las bibliotecas `gulp`, `sass`, `autoprefixer`, `uglify`, y `browsersync`.

**Intimidad inapropiada (+6):**
- La clase `gulpfile.js` accede frecuentemente a métodos y variables privadas de las bibliotecas `gulp` y `browsersync`.

**Cadenas de mensajes (+7):**
- El método `css` realiza varias llamadas en cadena a métodos de las bibliotecas `gulp`, `sass`, `autoprefixer`, y `cleanCSS`.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**
- La clase `gulpfile.js` tiene múltiples responsabilidades, como gestionar la construcción de CSS, JavaScript, mover dependencias de `node_modules` a `vendor`, y configurar `BrowserSync`.

**Principio Abierto/Cerrado (OCP) (+40):**
- La clase `gulpfile.js` no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos que manejan la lógica de construcción y movimiento de dependencias.

**Principio de Inversión de Dependencias (DIP) (+45):**
- La clase `gulpfile.js` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de construcción y movimiento de dependencias.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**
- Podría utilizarse para crear diferentes tipos de tareas de construcción sin especificar sus clases concretas.

**Constructor (+25):**
- Utilizar un constructor para simplificar la creación de instancias complejas de `gulpfile.js`.

**Método de Fábrica (+20):**
- Podría usarse para encapsular la creación de tareas de construcción y reducir la complejidad en `gulpfile.js`.

#### Estructurales

**Adaptador (+25):**
- Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la gestión de tareas de construcción.

**Decorador (+25):**
- Podría usarse para añadir responsabilidades a objetos de tareas de construcción de manera dinámica.

**Fachada (+20):**
- Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de tareas de construcción y gestión de dependencias.

#### De comportamiento

**Cadena de Responsabilidad (+30):**
- Podría permitir que múltiples objetos manejen una solicitud de construcción, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**
- Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de construcción.

**Iterador (+15):**
- Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de tareas de construcción sin exponer su representación subyacente.

**Mediador (+30):**
- Podría reducir las dependencias caóticas entre objetos de la clase `gulpfile.js`.

**Observador (+25):**
- Podría permitir que un objeto `gulpfile.js` notifique a otros objetos sobre cambios en su estado.

**Estado (+30):**
- Podría permitir que un objeto `gulpfile.js` altere su comportamiento cuando su estado interno cambia.

**Estrategia (+20):**
- Podría definir una familia de algoritmos de construcción y gestión de dependencias, encapsular cada uno, y hacerlos intercambiables en `gulpfile.js`.

**Método Plantilla (+25):**
- Podría definir el esqueleto de un algoritmo de construcción en una operación, dejando algunos pasos a las subclases.

**Visitante (+35):**
- Podría separar un algoritmo de construcción de la estructura de objeto `gulp` sobre la que opera.




Este repositorio fue obtenido de: https://github.com/codeswax/Proyecto-DAWM
