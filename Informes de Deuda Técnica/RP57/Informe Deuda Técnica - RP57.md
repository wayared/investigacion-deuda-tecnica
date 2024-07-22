
# Informe de Análisis de Deuda Técnica

## Clase Analizada: `app.js`

### Identificación de Olores de Código

#### **Acaparadores**
- **Método Largo (+5)**: El método `app.use(function(err, req, res, next) {...}` tiene más de 20 líneas, lo que dificulta su lectura y comprensión.
- **Clase Grande (+6)**: La clase `app.js` maneja la configuración del servidor, la configuración del motor de vistas, la configuración de middlewares y la gestión de rutas, lo que sugiere múltiples responsabilidades.
- **Obsesión Primitiva (+3)**: Se utilizan tipos primitivos para representar datos complejos en varias partes del código.

#### **Preventores de Cambio**
- **Cambio divergente (+6)**: La clase `app.js` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la configuración del servidor o actualizar los middlewares.
- **Cirugía de escopeta (+8)**: Cambios pequeños en la lógica del servidor pueden requerir modificaciones en múltiples métodos y middlewares relacionados.

#### **Dispensables**
- **Comentarios (+2)**: Existen comentarios en el método `app.use(function(err, req, res, next) {...}` que podrían evitarse con un código más claro y autoexplicativo.

### Violaciones de los Principios SOLID

#### **Principio de Responsabilidad Única (SRP) (+30)**
La clase `app.js` tiene múltiples responsabilidades, como gestionar la configuración del servidor, la configuración del motor de vistas, la configuración de middlewares y la gestión de rutas.

#### **Principio Abierto/Cerrado (OCP) (+40)**
La clase `app.js` no es fácilmente extensible sin modificar su código fuente, especialmente en la configuración de middlewares.

#### **Principio de Inversión de Dependencias (DIP) (+45)**
La clase `app.js` depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la configuración de middlewares y rutas.

### Patrones de diseño no utilizados

#### **Creacionales**
- **Fábrica Abstracta (+20)**: Podría utilizarse para crear diferentes tipos de middlewares sin especificar sus clases concretas.
- **Constructor (+25)**: Utilizar un constructor para simplificar la creación de instancias complejas de `app.js`.
- **Método de Fábrica (+20)**: Podría usarse para encapsular la creación de middlewares y reducir la complejidad en `app.js`.

#### **Estructurales**
- **Adaptador (+25)**: Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de middlewares.
- **Compuesto (+30)**: Podría ser útil para representar jerarquías de middlewares.
- **Decorador (+25)**: Podría usarse para añadir responsabilidades a middlewares de manera dinámica.
- **Fachada (+20)**: Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de configuración.

#### **De comportamiento**
- **Cadena de Responsabilidad (+30)**: Podría permitir que múltiples objetos manejen una solicitud de middleware, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20)**: Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de middlewares.
- **Iterador (+15)**: Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de middlewares sin exponer su representación subyacente.
- **Mediador (+30)**: Podría reducir las dependencias caóticas entre objetos de la clase `app.js`.
- **Observador (+25)**: Podría permitir que un objeto `app.js` notifique a otros objetos sobre cambios en su estado.
- **Estado (+30)**: Podría permitir que un objeto `app.js` altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20)**: Podría definir una familia de algoritmos de configuración de middlewares, encapsular cada uno, y hacerlos intercambiables en `app.js`.
- **Método Plantilla (+25)**: Podría definir el esqueleto de un algoritmo de configuración de middlewares en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35)**: Podría separar un algoritmo de configuración de middlewares de la estructura de objeto `app.js` sobre la que opera.

## Clase Analizada: `index.js`

### Identificación de Olores de Código

#### **Acaparadores**
- **Clase Grande (+6)**: La clase `index.js` maneja la configuración de la conexión a la base de datos, la carga de modelos y la configuración de asociaciones entre modelos, lo que sugiere múltiples responsabilidades.
- **Obsesión Primitiva (+3)**: Se utilizan tipos primitivos para representar datos complejos en la configuración de la base de datos.

#### **Preventores de Cambio**
- **Cambio divergente (+6)**: La clase `index.js` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar la configuración de la conexión a la base de datos o actualizar los modelos.
- **Cirugía de escopeta (+8)**: Cambios pequeños en la configuración de la base de datos pueden requerir modificaciones en múltiples métodos y configuraciones relacionadas.

#### **Dispensables**
- **Código duplicado (+7)**: No se identifican duplicaciones significativas en esta clase.
- **Código muerto (+3)**: No se identifican métodos y variables no utilizados.

#### **Acopladores**
- **Envidia de características (+5)**: No se identifican casos en los que un método utilice intensivamente métodos de otra clase.
- **Intimidad inapropiada (+6)**: La clase `index.js` no accede frecuentemente a métodos y variables privadas de otra clase.

### Violaciones de los Principios SOLID

#### **Principio de Responsabilidad Única (SRP) (+30)**
La clase `index.js` tiene múltiples responsabilidades, como gestionar la configuración de la conexión a la base de datos, la carga de modelos y la configuración de asociaciones entre modelos.

#### **Principio Abierto/Cerrado (OCP) (+40)**
La clase `index.js` no es fácilmente extensible sin modificar su código fuente, especialmente en la gestión de la configuración de la base de datos y la carga de modelos.

### Patrones de diseño no utilizados

#### **Creacionales**
- **Fábrica Abstracta (+20)**: Podría utilizarse para crear diferentes tipos de configuraciones de base de datos sin especificar sus clases concretas.
- **Método de Fábrica (+20)**: Podría usarse para encapsular la creación de configuraciones de base de datos y reducir la complejidad en `index.js`.

#### **Estructurales**
- **Adaptador (+25)**: Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de la conexión a la base de datos.
- **Fachada (+20)**: Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de configuración.

#### **De comportamiento**
- **Cadena de Responsabilidad (+30)**: Podría permitir que múltiples objetos manejen una solicitud de configuración de la base de datos, evitando el acoplamiento entre el emisor y el receptor.
- **Estrategia (+20)**: Podría definir una familia de algoritmos de configuración de la base de datos, encapsular cada uno, y hacerlos intercambiables en `index.js`.
- **Método Plantilla (+25)**: Podría definir el esqueleto de un algoritmo de configuración en una operación, dejando algunos pasos a las subclases.

## Clase Analizada: `MedicallService`

### Identificación de Olores de Código

#### **Acaparadores**
- **Clase Grande (+6)**: La clase `MedicallService` tiene responsabilidades relacionadas con la obtención de datos de diferentes endpoints, lo que sugiere una posible sobrecarga de responsabilidades.
- **Obsesión Primitiva (+3)**: Se utilizan tipos primitivos (`Number`) para representar identificadores, lo cual podría ser manejado con un tipo más específico.

#### **Preventores de Cambio**
- **Cambio divergente (+6)**: La clase `MedicallService` tiene múltiples razones para cambiar debido a su alto número de responsabilidades, como modificar los endpoints o la lógica de obtención de datos.
- **Cirugía de escopeta (+8)**: Cambios pequeños en la lógica de obtención de datos pueden requerir modificaciones en múltiples métodos relacionados.

### Violaciones de los Principios SOLID

#### **Principio de Responsabilidad Única (SRP) (+30)**
La clase `MedicallService` tiene múltiples responsabilidades, como la obtención de títulos, citas y médicos de diferentes endpoints.

#### **Principio Abierto/Cerrado (OCP) (+40)**
La clase `MedicallService` no es fácilmente extensible sin modificar su código fuente, especialmente en la gestión de los diferentes endpoints.

### Patrones de diseño no utilizados

#### **Creacionales**
- **Fábrica Abstracta (+20)**: Podría utilizarse para crear diferentes tipos de servicios de obtención de datos sin especificar sus clases concretas.
- **Método de Fábrica (+20)**: Podría usarse para encapsular la creación de servicios de obtención de datos y reducir la complejidad en `MedicallService`.

#### **Estructurales**
- **Adaptador (+25)**: Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de los servicios de obtención de datos.
- **Fachada (+20)**: Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de obtención de datos.

#### **De comportamiento**
- **Cadena de Responsabilidad (+30)**: Podría permitir que múltiples objetos manejen una solicitud de obtención de datos, evitando el acoplamiento entre el emisor y el receptor.
- **Estrategia (+20)**: Podría definir una familia de algoritmos de obtención de datos, encapsular cada uno, y hacerlos intercambiables en `MedicallService`.
- **Método Plantilla (+25)**: Podría definir el esqueleto de un algoritmo de obtención de datos en una operación, dejando algunos pasos a las subclases.

## Clase Analizada: `cita.component.spec.ts`

### Identificación de Olores de Código

#### **Dispensables**
- **Código duplicado (+7)**: No se identifican duplicaciones significativas en esta clase.
- **Código muerto (+3)**: No se identifican métodos y variables no utilizados.

### Violaciones de los Principios SOLID

#### **Principio de Responsabilidad Única (SRP) (+30)**
La clase `cita.component.spec.ts` tiene una única responsabilidad, que es realizar pruebas unitarias del componente `CitaComponent`.

### Patrones de diseño no utilizados

#### **De comportamiento**
- **Método Plantilla (+25)**: Podría definir el esqueleto de las pruebas unitarias, dejando algunos pasos a las subclases para facilitar la creación de nuevas pruebas.

---


Este repositorio fue obtenido de: https://github.com/JairoAb/Proyecto_DAWM-2022-1
