
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `FiltradoComponent`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):**
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):**  Los datos están agrupados en arreglos simples, pero se podría considerar una mejor estructuración.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase tiene responsabilidad única pero podría necesitar ajustes si cambia la forma en que se reciben o procesan los datos.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** La clase realiza operaciones específicas relacionadas con el filtrado de rutas.

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):** Hay un pequeño grado de duplicación en la ordenación de rutas, que podría ser extraído a un método auxiliar.
- **Clase de datos (+5):** Los datos se manejan en listas simples en lugar de estructuras más complejas.
- **Código muerto (+3):**
- **Clase perezosa (+4):**
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):**
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** Los mensajes de error o advertencia no se manejan explícitamente.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificaciones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de HttpClient, lo que podría violar el DIP. Sin embargo, para un componente Angular, esto es aceptable si se usa la inyección de dependencias de manera adecuada.

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
* **Estrategia (+20)** La lógica de ordenación podría beneficiarse de un patrón estrategia.
* **Método Plantilla (+25)**
* **Visitante (+35)**

## Clase Analizada: `RutasserviceService`

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

- **Cambio divergente (+6):** La clase está enfocada en la interacción con servicios HTTP, lo que podría necesitar ajustes si los servicios cambian.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):**

#### Dispensables

- **Comentarios (+2):**
- **Código duplicado (+7):**
- **Clase de datos (+5):** Los datos se manejan como objetos simples en lugar de estructuras complejas.
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
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificaciones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de HttpClient. Aunque esto es común en servicios Angular, podría mejorarse con una capa de abstracción.
 
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

## Clase Analizada: `AddRoutesComponent`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5)****:**
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Los datos se agrupan en estructuras simples como FormGroup y arreglos.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase podría necesitar ajustes si las interfaces del backend cambian.
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
- **Intimidad inapropiada (+6):** La clase está acoplada a RutasserviceService para la interacción con el backend.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** No se observan cadenas de mensajes o manejo de errores.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificaciones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende de RutasserviceService, que podría ser mejorado con una capa de abstracción.

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

## Clase Analizada: `RutasComponent`

### Identificación de Olores de Código

#### Acaparadores

- **Méto****do Largo (+5):**
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

- **Cambio divergente (+6):** La clase podría necesitar ajustes si las interfaces del backend cambian.
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
- **Intimidad inapropiada (+6):** La clase está acoplada a RutasserviceService para la interacción con el backend.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):**
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificaciones.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende de RutasserviceService, que podría ser mejorado con una capa de abstracción.

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



Este repositorio fue obtenido de: https://github.com/AndresBorbor/LP-frontend