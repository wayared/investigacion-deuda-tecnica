# Informe de Análisis de Deuda Técnica
## Clase Analizada: Admin

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** 
  - El método de configuración del gráfico (Chart constructor) es extenso y tiene múltiples responsabilidades, como definir datos, etiquetas y opciones del gráfico.
  
- **Clase Grande (+6):** 
  - La configuración de la clase myChart contiene tanto la definición de datos como la configuración de la apariencia y comportamiento del gráfico.

- **Obsesión Primitiva (+3):** 
  - Uso de tipos primitivos y literales para definir colores y datos directamente en la configuración del gráfico.

- **Lista de Parámetros Largos (+4):** 
  - La configuración de `datasets` incluye múltiples propiedades que podrían encapsularse mejor.

#### Abusadores de Orientación a Objetos

- **Sentencias Switch (+5):** 
  - No aplica.

#### Preventores de Cambio

- **Cambio Divergente (+6):** 
  - La clase `myChart` tiene múltiples razones para cambiar, como modificar el tipo de gráfico, actualizar los datos o cambiar la apariencia.

- **Cirugía de Escopeta (+8):** 
  - Cambios en la apariencia del gráfico (como colores y bordes) están dispersos a lo largo de la configuración, lo que requiere modificaciones en múltiples lugares.

#### Dispensables

- **Comentarios (+2):** 
  - No se observan comentarios excesivos en el código proporcionado.

- **Código Duplicado (+7):** 
  - No se observa código duplicado en el ejemplo proporcionado.

- **Clase de Datos (+5):** 
  - La configuración actúa más como una estructura de datos sin comportamiento significativo.

- **Código Muerto (+3):** 
  - No se observa código muerto en el ejemplo proporcionado.

#### Acopladores

- **Envidia de Características (+5):** 
  - No aplica.

- **Intimidad Inapropiada (+6):** 
  - No aplica.

- **Cadenas de Mensajes (+7):** 
  - No aplica.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** 
  - La configuración del gráfico tiene múltiples responsabilidades, como definir datos, etiquetas y opciones del gráfico.

- **Principio Abierto/Cerrado (OCP) (+40):** 
  - La clase no es fácilmente extensible sin modificar el código fuente, especialmente si se desea cambiar el tipo de gráfico o la configuración de opciones.

- **Principio de Inversión de Dependencias (DIP) (+45):** 
  - La clase depende directamente de implementaciones concretas de configuración de gráficos en lugar de abstracciones.

### Patrones de Diseño no Utilizados

#### Creacionales

- **Fábrica Abstracta (+20):** 
  - Podría utilizarse para crear diferentes tipos de gráficos sin especificar sus clases concretas.

- **Constructor (+25):** 
  - Utilizar un constructor para simplificar la creación de instancias complejas de gráficos.

- **Método de Fábrica (+20):** 
  - Podría usarse para encapsular la creación de diferentes configuraciones de gráficos y reducir la complejidad.

#### Estructurales

- **Adaptador (+25):** 
  - Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en la configuración de diferentes librerías de gráficos.

- **Compuesto (+30):** 
  - Podría ser útil para representar jerarquías de configuraciones de gráficos.

- **Decorador (+25):** 
  - Podría usarse para añadir responsabilidades a objetos de configuración de gráficos de manera dinámica.

- **Fachada (+20):** 
  - Podría proporcionar una interfaz simplificada a un conjunto de configuraciones de gráficos.

#### De Comportamiento

- **Cadena de Responsabilidad (+30):** 
  - Podría permitir que múltiples objetos manejen una solicitud de configuración de gráficos, evitando el acoplamiento entre el emisor y el receptor.

- **Comando (+20):** 
  - Podría encapsular una solicitud de configuración de gráficos como un objeto, permitiendo parametrizar clientes con colas y operaciones.

- **Iterador (+15):** 
  - Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de configuraciones de gráficos sin exponer su representación subyacente.

- **Mediador (+30):** 
  - Podría reducir las dependencias caóticas entre objetos de configuración de gráficos.

- **Observador (+25):** 
  - Podría permitir que un objeto de configuración de gráficos notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):** 
  - Podría permitir que un objeto de configuración de gráficos altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):** 
  - Podría definir una familia de algoritmos de configuración de gráficos, encapsular cada uno, y hacerlos intercambiables.

- **Método Plantilla (+25):** 
  - Podría definir el esqueleto de una configuración de gráficos en una operación, dejando algunos pasos a las subclases.

- **Visitante (+35):** 
  - Podría separar un algoritmo de configuración de gráficos de la estructura de datos sobre la que opera.

## Clase Analizada: Dashboard

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
  - El método `load()` es extenso y maneja múltiples responsabilidades como la configuración del gráfico, la manipulación del DOM y el manejo de eventos.

- **Clase Grande (+6):**
  - La clase anónima que contiene los métodos `plot()`, `load()`, `loadInocar()` y la función autoejecutable IIFE tiene múltiples responsabilidades, incluyendo la obtención de datos, actualización de la UI y la creación de gráficos.

#### Preventores de Cambio

- **Cambio Divergente (+6):**
  - La clase tiene múltiples razones para cambiar, como modificar la configuración del gráfico, actualizar la UI o cambiar la lógica de obtención de datos.

- **Cirugía de Escopeta (+8):**
  - Cambios en la apariencia del gráfico o en la lógica de obtención de datos están dispersos a lo largo de la configuración, lo que requiere modificaciones en múltiples lugares.

#### Dispensables

- **Comentarios (+2):**
  - Existen comentarios en el código, pero podrían evitarse con un código más claro y autoexplicativo.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase tiene múltiples responsabilidades, como la configuración del gráfico, la manipulación del DOM y el manejo de eventos.

- **Principio Abierto/Cerrado (OCP) (+40):**
  - La clase no es fácilmente extensible sin modificar el código fuente, especialmente si se desea cambiar la configuración del gráfico o la lógica de obtención de datos.

- **Principio de Inversión de Dependencias (DIP) (+45):**
  - La clase depende directamente de implementaciones concretas de configuración de gráficos y manipulación del DOM en lugar de abstracciones.

### Patrones de Diseño no Utilizados

#### Creacionales

- **Constructor (+25):**
  - Utilizar un constructor para simplificar la creación de instancias complejas de gráficos y la configuración de la UI.

- **Método de Fábrica (+20):**
  - Podría usarse para encapsular la creación de diferentes configuraciones de gráficos y reducir la complejidad.

#### Estructurales

- **Fachada (+20):**
  - Podría proporcionar una interfaz simplificada a un conjunto de configuraciones de gráficos y manipulación del DOM.

#### De Comportamiento

- **Observador (+25):**
  - Podría permitir que un objeto de configuración de gráficos notifique a otros objetos sobre cambios en su estado.

- **Estado (+30):**
  - Podría permitir que un objeto de configuración de gráficos altere su comportamiento cuando su estado interno cambia.

- **Estrategia (+20):**
  - Podría definir una familia de algoritmos de configuración de gráficos y manipulación del DOM, encapsular cada uno, y hacerlos intercambiables.

- **Método Plantilla (+25):**
  - Podría definir el esqueleto de una configuración de gráficos en una operación, dejando algunos pasos a las subclases.



Este repositorio fue obtenido de: https://github.com/CristopherVilla20/Dashboard-clima
