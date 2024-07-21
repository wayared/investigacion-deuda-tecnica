
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `Service Worker`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** register(config) es bastante largo y contiene múltiples responsabilidades, como verificar si está en producción, manejar URLs, y registrar el service worker.
- **Clase Grande (+6):** La clase no es explícitamente una clase en el sentido de OOP, pero el archivo contiene múltiples funciones que manejan diferentes responsabilidades, lo que sugiere que podría beneficiarse de ser refactorizado en varias clases o módulos más pequeños.
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** Si se requiere cambiar la lógica de registro o manejo del service worker, se deben modificar múltiples lugares en el archivo.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):** Hay varios comentarios que explican el propósito del código, lo cual es útil. Sin embargo, algunos comentarios podrían eliminarse si se mejora la claridad del código.
- **Código duplicado (+7):** No hay duplicación directa de código, pero algunas funciones realizan tareas similares, lo que sugiere una posible refactorización para consolidar la lógica común.
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** Hay algunas cadenas de mensajes entre las funciones que registran y validan el service worker.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** Los métodos register, registerValidSW y checkValidServiceWorker manejan múltiples responsabilidades.
- **Principio Abierto/Cerrado (OCP) (+40)** Las funciones actuales no están diseñadas para ser fácilmente extensibles sin modificar el código existente.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Podría considerarse implementar una fachada para simplificar las interacciones con el service worker y encapsular la complejidad.
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `AppWidgetSummary`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)****:**
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La lógica y los estilos están estrechamente acoplados, lo que puede hacer que los cambios sean más difíciles de manejar.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cualquier cambio en el estilo o la estructura del componente podría requerir cambios en varios lugares.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):**
- **Clase de datos (+5):** El componente maneja datos pero no de una manera que sugiera que es solo una clase de datos.
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** El componente depende de funciones y componentes específicos como Iconify, pero está bien modularizado y no viola este principio.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)**
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)** Podría aplicarse si el componente necesitara reaccionar a cambios externos más complejos.
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `BlogPostCard`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El componente BlogPostCard contiene un método que es relativamente largo debido a la cantidad de lógica de renderizado y estilos que maneja.
- **Clase Grande (+6):** La clase maneja múltiples responsabilidades, incluyendo el renderizado de información del post, estilos dinámicos, y lógica de disposición.
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La lógica y los estilos están estrechamente acoplados, lo que puede dificultar los cambios en la apariencia o comportamiento del componente.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cualquier cambio en el estilo o la estructura del componente podría requerir cambios en varios lugares.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):**
- **Clase de datos (+5):**
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)**
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)** Podría aplicarse si el componente necesitara reaccionar a cambios externos más complejos.
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `DashboardAppPage`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método DashboardAppPage es relativamente largo debido a la cantidad de componentes que se renderizan.
- **Clase Grande (+6):** La clase maneja múltiples responsabilidades, incluyendo la configuración del tema, renderizado de componentes de resumen y gráficos.
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La lógica y los estilos están estrechamente acoplados, lo que puede dificultar los cambios en la apariencia o comportamiento del componente.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cualquier cambio en el estilo o la estructura del componente podría requerir cambios en varios lugares.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):**
- **Clase de datos (+5):** El componente maneja datos pero no de una manera que sugiera que es solo una clase de datos.
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)**
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)**
* **Peso Ligero (+40)**
* **Proxy (+30)**

#### De comportamiento

* **Cadena de Responsabilidad (+30)**
* **Comando (+20)**
* **Intérprete (+40)**
* **Iterador (+15)**
* **Mediador (+30)**
* **Memento (+35)**
* **Observador (+25)** Podría aplicarse si el componente necesitara reaccionar a cambios externos más complejos.
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**



Este repositorio fue obtenido de: https://github.com/dpaulsoria/DAWM