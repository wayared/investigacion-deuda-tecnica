
# Informe de Análisis de Deuda Técnica
## Clase Analizada: `app`

### Identificación de Olores de Código

#### Acaparadores

**Método Largo (+5):**  
El método anónimo usado como manejador de errores (`app.use(function(err, req, res, next) {...}`) tiene más de 20 líneas, dificultando su lectura y comprensión.

**Clase Grande (+6):**  
La clase `app` tiene múltiples responsabilidades, como gestionar la configuración del servidor, manejar rutas y gestionar errores.

**Lista de Parámetros Largos (+4):**  
El método anónimo utilizado para manejar errores (`app.use(function(err, req, res, next) {...}`) tiene una lista de parámetros larga.

#### Preventores de Cambio

**Cambio divergente (+6):**  
La clase `app` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de configuración del servidor o actualizar rutas.

**Cirugía de escopeta (+8):**  
Cambios pequeños en la lógica de configuración del servidor requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables

**Comentarios (+2):**  
Existen muchos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

**Código duplicado (+7):**  
El código para configurar middlewares como `app.use(cors())` y `app.use(logger('dev'))` podría centralizarse en una función dedicada.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**  
La clase `app` tiene múltiples responsabilidades, como gestionar la configuración del servidor y manejar rutas.

**Principio Abierto/Cerrado (OCP) (+40):**  
La clase `app` no es fácilmente extensible sin modificar su código fuente, especialmente en la configuración de middlewares.

**Principio de Inversión de Dependencias (DIP) (+45):**  
La clase `app` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión de la lógica de configuración.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**  
Podría utilizarse para crear diferentes tipos de middlewares sin especificar sus clases concretas.

**Constructor (+25):**  
Utilizar un constructor para simplificar la creación de instancias complejas de `app`.

**Método de Fábrica (+20):**  
Podría usarse para encapsular la creación de middlewares y reducir la complejidad en `app`.

#### Estructurales

**Adaptador (+25):**  
Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de middlewares.

**Decorador (+25):**  
Podría usarse para añadir responsabilidades a objetos de middlewares de manera dinámica.

**Fachada (+20):**  
Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de configuración del servidor.

#### De comportamiento

**Cadena de Responsabilidad (+30):**  
Podría permitir que múltiples objetos manejen una solicitud de configuración de middlewares, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**  
Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de configuración.

**Mediador (+30):**  
Podría reducir las dependencias caóticas entre objetos de la clase `app`.

**Observador (+25):**  
Podría permitir que un objeto `app` notifique a otros objetos sobre cambios en su estado.

**Estrategia (+20):**  
Podría definir una familia de algoritmos de configuración, encapsular cada uno, y hacerlos intercambiables en `app`.

## Clase Analizada: `rest_cliente`

### Identificación de Olores de Código

#### Acaparadores

**Clase Grande (+6):**  
La clase `rest_cliente` tiene múltiples responsabilidades, como gestionar las rutas y manejar la lógica de CRUD para `cliente`.

#### Preventores de Cambio

**Cambio divergente (+6):**  
La clase `rest_cliente` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la lógica de las rutas o actualizar la lógica de CRUD.

**Cirugía de escopeta (+8):**  
Cambios pequeños en la lógica de CRUD requieren modificaciones en múltiples métodos y rutas relacionadas.

#### Dispensables

**Comentarios (+2):**  
Existen algunos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

**Código duplicado (+7):**  
El código para manejar errores y enviar respuestas se repite en varios métodos de la clase `rest_cliente`.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**  
La clase `rest_cliente` tiene múltiples responsabilidades, como gestionar las rutas y manejar la lógica de CRUD para `cliente`.

**Principio Abierto/Cerrado (OCP) (+40):**  
La clase `rest_cliente` no es fácilmente extensible sin modificar su código fuente, especialmente en la configuración de rutas y la lógica de CRUD.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**  
Podría utilizarse para crear diferentes tipos de rutas sin especificar sus clases concretas.

**Método de Fábrica (+20):**  
Podría usarse para encapsular la creación de rutas y reducir la complejidad en `rest_cliente`.

#### Estructurales

**Adaptador (+25):**  
Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de rutas.

**Decorador (+25):**  
Podría usarse para añadir responsabilidades a objetos de rutas de manera dinámica.

**Fachada (+20):**  
Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de configuración de rutas.

#### De comportamiento

**Cadena de Responsabilidad (+30):**  
Podría permitir que múltiples objetos manejen una solicitud de configuración de rutas, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**  
Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de configuración.

**Mediador (+30):**  
Podría reducir las dependencias caóticas entre objetos de la clase `rest_cliente`.

**Observador (+25):**  
Podría permitir que un objeto `rest_cliente` notifique a otros objetos sobre cambios en su estado.

**Estrategia (+20):**  
Podría definir una familia de algoritmos de configuración, encapsular cada uno, y hacerlos intercambiables en `rest_cliente`.

## Clase Analizada: `rest_pedido`

### Identificación de Olores de Código

#### Acaparadores

**Clase Grande (+6):**  
La clase `rest_pedido` tiene responsabilidades de gestión de rutas y lógica de negocio para pedidos, aunque en menor medida comparado con clases más grandes.

#### Preventores de Cambio

**Cambio divergente (+6):**  
La clase `rest_pedido` tiene múltiples razones para cambiar debido a sus responsabilidades de gestión de rutas y lógica de negocio.

**Cirugía de escopeta (+8):**  
Cambios pequeños en la lógica de manejo de pedidos podrían requerir modificaciones en múltiples métodos relacionados.

#### Dispensables

**Comentarios (+2):**  
Existen comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**  
La clase `rest_pedido` tiene responsabilidades tanto de gestión de rutas como de manejo de lógica de negocio para pedidos.

**Principio Abierto/Cerrado (OCP) (+40):**  
La clase `rest_pedido` no es fácilmente extensible sin modificar su código fuente, especialmente en la configuración de rutas y lógica de negocio.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**  
Podría utilizarse para crear diferentes tipos de rutas sin especificar sus clases concretas.

**Método de Fábrica (+20):**  
Podría usarse para encapsular la creación de rutas y reducir la complejidad en `rest_pedido`.

#### Estructurales

**Adaptador (+25):**  
Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de rutas.

**Decorador (+25):**  
Podría usarse para añadir responsabilidades a objetos de rutas de manera dinámica.

**Fachada (+20):**  
Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de configuración de rutas.

#### De comportamiento

**Cadena de Responsabilidad (+30):**  
Podría permitir que múltiples objetos manejen una solicitud de configuración de rutas, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**  
Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de configuración.

**Mediador (+30):**  
Podría reducir las dependencias caóticas entre objetos de la clase `rest_pedido`.

**Observador (+25):**  
Podría permitir que un objeto `rest_pedido` notifique a otros objetos sobre cambios en su estado.

**Estrategia (+20):**  
Podría definir una familia de algoritmos de configuración, encapsular cada uno, y hacerlos intercambiables en `rest_pedido`.

## Clase Analizada: `index`

### Identificación de Olores de Código

#### Acaparadores

**Clase Grande (+6):**  
La clase `index` tiene múltiples responsabilidades, como configurar la conexión a la base de datos, cargar modelos y asociar modelos.

**Método Largo (+5):**  
El bloque de código dentro de `fs.readdirSync(__dirname).filter(...).forEach(...)` es largo y contiene lógica compleja, lo que dificulta su lectura y mantenimiento.

#### Preventores de Cambio

**Cambio divergente (+6):**  
La clase `index` tiene múltiples razones para cambiar debido a sus responsabilidades de configuración de la base de datos y carga de modelos.

**Cirugía de escopeta (+8):**  
Cambios pequeños en la configuración de la base de datos o en la carga de modelos podrían requerir modificaciones en múltiples partes del archivo.

#### Dispensables

**Código duplicado (+7):**  
El patrón de carga de archivos `.js` y la exclusión de archivos de prueba podrían centralizarse en una función dedicada.

### Violaciones de los Principios SOLID

**Principio de Responsabilidad Única (SRP) (+30):**  
La clase `index` tiene responsabilidades tanto de configuración de la base de datos como de carga y asociación de modelos.

**Principio Abierto/Cerrado (OCP) (+40):**  
La clase `index` no es fácilmente extensible sin modificar su código fuente, especialmente en la configuración de la base de datos y la carga de modelos.

### Patrones de diseño no utilizados

#### Creacionales

**Fábrica Abstracta (+20):**  
Podría utilizarse para crear diferentes configuraciones de la base de datos sin especificar sus clases concretas.

**Método de Fábrica (+20):**  
Podría usarse para encapsular la creación de instancias de `Sequelize` y reducir la complejidad en `index`.

#### Estructurales

**Adaptador (+25):**  
Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración y carga de modelos.

**Fachada (+20):**  
Podría proporcionar una interfaz simplificada a un conjunto de interfaces en el subsistema de configuración de la base de datos y carga de modelos.

#### De comportamiento

**Cadena de Responsabilidad (+30):**  
Podría permitir que múltiples objetos manejen una solicitud de configuración y carga de modelos, evitando el acoplamiento entre el emisor y el receptor.

**Comando (+20):**  
Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de configuración.

**Mediador (+30):**  
Podría reducir las dependencias caóticas entre objetos de la clase `index`.

**Observador (+25):**  
Podría permitir que un objeto `index` notifique a otros objetos sobre cambios en su estado.

**Estrategia (+20):**  
Podría definir una familia de algoritmos de configuración, encapsular cada uno, y hacerlos intercambiables en `index`.



Este repositorio fue obtenido de: https://github.com/RicardoMolinaCoronel/backDMPA
