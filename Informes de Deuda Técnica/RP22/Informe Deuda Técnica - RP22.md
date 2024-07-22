
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `PrimaryController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** El método crearCuadrosRecursivo es bastante largo y maneja múltiples responsabilidades, incluyendo la creación de nodos y la aplicación de estilos.
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):** La variable tipoNodo se usa para alternar entre VBox y HBox, lo cual puede causar confusión y errores si no se maneja adecuadamente.

#### Preventores de Cambio

- **Cambio divergente (+6):** La lógica para crear y configurar nodos de la interfaz está distribuida en varios métodos, lo que hace difícil modificar una parte sin afectar a otras.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables
 
- **Comentarios (+2):** Algunos comentarios son innecesarios y podrían ser eliminados para hacer el código más legible.
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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase PrimaryController maneja la inicialización de la interfaz, la creación de nodos, y la aplicación de estilos, lo cual viola el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)**

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)**
- **Método de Fábrica (+20)** La creación de VBox y HBox podría beneficiarse de un método de fábrica para encapsular la lógica de creación.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** Una fachada podría simplificar la interacción con la interfaz, encapsulando la lógica de creación de nodos y la aplicación de estilos.
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

## Clase Analizada: `treemapg3`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** El método getInfo y sumaCarpeta contienen bastante lógica que podría ser dividida en métodos más pequeños y manejables.
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

- **Cambio divergente (+6):** La lógica para obtener información de archivos y carpetas está distribuida en varios métodos, lo que dificulta la modificación de una parte sin afectar a otras.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase treemapg3 maneja la obtención de información de archivos, la suma del tamaño de carpetas y la representación de nodos en un treemap, lo cual viola el SRP.
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
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `ClasePrueba`

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

- **Cambio divergente (+6):**
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):**
- **Clase de datos (+5):** La clase ClasePrueba es principalmente una clase de datos sin mucha lógica asociada.
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

- **Principio de Responsabilidad Única (SRP) (+30)** Aplicable. La clase ClasePrueba podría considerarse una clase de datos pura, lo cual puede ser aceptable, pero cualquier lógica adicional debería estar en otra clase.
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
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `App`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):**
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

- **Cambio divergente (+6):**
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

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

- **Principio de Responsabilidad Única (SRP) (+30)** La clase se encarga de iniciar la aplicación y cargar las vistas, cumpliendo con una única responsabilidad.
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
* **Observador (+25)**
* **Estado (+30)**
* **Estrategia (+20)**
* **Método Plantilla (+25)**
* **Visitante (+35)**



Este repositorio fue obtenido de: https://github.com/jppluas/Proyecto-2P-EDD-Grupo-3