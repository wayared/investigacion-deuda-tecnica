
# Informe de Análisis de Deuda Técnica

# Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `MesaJuegoController`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo** **(+5):** Métodos como repartirCartas y robarCartaMesa realizan múltiples tareas y podrían ser divididos en métodos más pequeños para mejorar la claridad.
- **Clase Grande (+6):** La clase maneja varias responsabilidades: inicialización de la vista, manejo de cartas y eventos, y la lógica del juego. Esto puede ser dividido en varias clases.
- **Obsesión Primitiva (+3):** Los datos sobre cartas y estado del juego se manejan a través de arrays y listas de objetos sin encapsular en una estructura más adecuada.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Datos relacionados a las cartas y sus imágenes se gestionan a través de listas y variables sin encapsular en objetos específicos.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase está acoplada a múltiples aspectos del juego, lo que significa que un cambio en la lógica del juego o en la interfaz puede requerir cambios en la clase.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Cambios en la lógica del juego pueden requerir modificaciones en múltiples métodos de esta clase.

#### Dispensables

- **Comentarios (+2):** La clase tiene comentarios mínimos y podría beneficiarse de comentarios más detallados sobre la lógica y propósito de los métodos.
- **Código duplicado (+7):** La lógica para manejar imágenes y cartas se repite en múltiples lugares, como en la creación de VBox para cada carta.
- **Clase de datos (+5):** Los datos se gestionan directamente a través de arrays y listas, en lugar de usar objetos o estructuras más organizadas.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase maneja múltiples responsabilidades, lo cual puede considerarse pereza en la separación de responsabilidades.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase accede y manipula directamente los recursos multimedia (imágenes de cartas) y datos del juego, lo que puede ser mejorado utilizando servicios dedicados.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** La lógica de manejo de cartas y eventos se encuentra dispersa, lo que puede ser considerado como una cadena de mensajes.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase maneja múltiples responsabilidades como la inicialización de la vista, manejo de cartas, y lógica del juego, violando el SRP.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificar el código existente. Cambios en la lógica del juego o en la interfaz requieren modificaciones en la clase.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de recursos específicos como imágenes y datos de cartas, en lugar de utilizar servicios o repositorios que abstraigan estos detalles.

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

## Clase Analizada: `Carta`

### Identificación de Olores de Código

#### Acaparadores

- **Método Largo (+5):** Los métodos loadCartasPoker, loadCartasEspanolas, y loadCartasEspanolasV2 realizan múltiples tareas de manera extensa. Podrían beneficiarse de ser divididos en métodos más pequeños.
- **Clase Grande (+6):** La clase Carta tiene un tamaño moderado con múltiples responsabilidades relacionadas con la creación y carga de cartas. Aunque no es excesivamente grande, puede ser mejorada para una mayor claridad y funcionalidad.
- **Obsesión Primitiva (+3):** Se utiliza el tipo primitivo int para el valor de la carta y el String para otras propiedades. Podría beneficiarse de una mejor representación y encapsulación.
- **Lista de Parámetros Largos (+4):**
- **Grupos de Datos (+3):** Datos relacionados con la carta están encapsulados en variables, pero se podrían mejorar utilizando objetos o estructuras más organizadas.

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase Carta podría ser más flexible y menos dependiente de detalles específicos de implementación, lo que permitiría una mejor adaptación a cambios.
- **Jerarquías de herencia paralela (+7):**
- **Cirugía de escopeta (+8):** Los cambios en la lógica de carga y en las representaciones de cartas pueden requerir modificaciones en múltiples métodos.

#### Dispensables

- **Comentarios (+2):** La clase tiene algunos comentarios, pero podría beneficiarse de comentarios más detallados y descriptivos.
- **Código duplicado (+7):** El código para crear las cartas es similar en los métodos de carga, lo que puede ser refactorizado para eliminar duplicación.
- **Clase de datos (+5):** La clase maneja datos de cartas, pero la lógica de carga y representación podría estar más separada.
- **Código muerto (+3):**
- **Clase perezosa (+4):** La clase maneja varias responsabilidades relacionadas con cartas, lo que puede considerarse una falta de separación de responsabilidades.
- **Generalidad especulativa (+5):**

#### Acopladores

- **Envidia de características (+5):**
- **Intimidad inapropiada (+6):** La clase maneja la creación y carga de cartas directamente, lo que puede ser mejorado separando las responsabilidades.
- **Clase de biblioteca incompleta (+4):**
- **Cadenas de mensajes (+7):** La lógica de carga de cartas puede estar dispersa y no encapsulada, lo que puede ser mejorado.
- **Hombre medio (+6):**

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30)** La clase Carta maneja tanto la representación de una carta como la lógica para cargar diferentes tipos de cartas. Esto puede ser dividido en clases separadas.
- **Principio Abierto/Cerrado (OCP) (+40)** La clase no está diseñada para ser extendida sin modificar el código existente, especialmente en los métodos de carga de cartas.
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende directamente de las rutas de imágenes y de los detalles específicos de las cartas, en lugar de utilizar una abstracción.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)** El constructor de la clase es simple y no utiliza el patrón Constructor para crear objetos complejos.
- **Método de Fábrica (+20)** La clase tiene métodos de carga que podrían beneficiarse del patrón Método de Fábrica.
- **Prototipo (+30)**
- **Singleton (+15)**

#### Estructurales

* **Adaptador (+25)**
* **Puente (+35)**
* **Compuesto (+30)**
* **Decorador (+25)**
* **Fachada (+20)** No se utiliza el patrón Fachada para simplificar la creación y manejo de cartas.
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

- **Método Largo (+5):** Los métodos start, setRoot, loadFXML, y switchScenes no son excesivamente largos. Sin embargo, el método switchScenes hace varias cosas que podrían ser simplificadas.
- **Clase Grande (+6):** 
- **Obsesión Primitiva (+3):** La clase utiliza primitivos y cadenas para definir el tamaño de la ventana y el nombre del archivo FXML. No se observa una obsesión significativa con primitivos.
- **Lista de Parámetros Largos (+4):** 
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase no parece estar muy afectada por cambios, aunque el método switchScenes podría beneficiarse de una mayor flexibilidad.
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
- **Singleton (+15)** La clase App podría beneficiarse del patrón Singleton para asegurar una única instancia de la aplicación.

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

## Clase Analizada: `PartidaJugada`

### Identificación de Olores de Código

#### Acaparadores

- **Méto****do Largo (+5):**
- **Clase Grande (+6):**
- **Obsesión Primitiva (+3):**
- **Lista de Parámetros Largos (+4):** El constructor con muchos parámetros puede ser difícil de mantener. Este es un problema común cuando se tiene un gran número de atributos.
- **Grupos de Datos (+3):**

#### Abusadores de Orientación a Objetos

- **Clases Alternativas con Diferentes Interfaces (+7):**
- **Legado Rechazado (+6):**
- **Sentencias *Switch* (+5):**
- **Campos Temporales (+4):**

#### Preventores de Cambio

- **Cambio divergente (+6):** La clase parece bien estructurada para cambios. Sin embargo, el constructor con muchos parámetros puede ser una fuente de problemas si se requieren cambios en los atributos.
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

- **Principio de Responsabilidad Única (SRP) (+30)**
- **Principio Abierto/Cerrado (OCP) (+40)**
- **Principio de Sustitución de Liskov (LSP) (+35)**
- **Principio de Segregación de Interfaces (ISP) (+25)**
- **Principio de Inversión de Dependencias (DIP) (+45)** La clase depende de detalles de implementación (como BufferedReader), lo cual puede ser una oportunidad para mejorar la flexibilidad.

### Patrones de diseño no utilizados

#### Creacionales

- **Fábrica Abstracta (+20)**
- **Constructor (+25)** La clase PartidaJugada utiliza un constructor con muchos parámetros, que puede ser simplificado.
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



Este repositorio fue obtenido de: https://github.com/SebastRivera/ProyectoSegundoParcial