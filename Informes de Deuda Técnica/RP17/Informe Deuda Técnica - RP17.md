
# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `ImagenController`

#### Identificación de Olores de Código

##### Acaparadores
- **Método Largo (+5):** 
  - `guardarImagen` (es largo y realiza múltiples tareas)
  - `llenarCampos` (realiza muchas tareas y contiene lógica compleja)
- **Clase Grande (+6):** No
- **Obsesión Primitiva (+3):** No
- **Lista de Parámetros Largos (+4):** No
- **Grupos de Datos (+3):** No

##### Abusadores de Orientación a Objetos
- **Clases Alternativas con Diferentes Interfaces (+7):** No
- **Legado Rechazado (+6):** No
- **Sentencias Switch (+5):** No
- **Campos Temporales (+4):** 
  - `InputStream input` (en `llenarCampos` se utiliza temporalmente)

##### Preventores de Cambio
- **Cambio divergente (+6):** No
- **Jerarquías de herencia paralela (+7):** No
- **Cirugía de escopeta (+8):** No

##### Dispensables
- **Comentarios (+2):** 
  - Comentarios explicativos en diversas partes del código en lugar de utilizar nombres de métodos y variables más claros.
- **Código duplicado (+7):** No
- **Clase de datos (+5):** No
- **Código muerto (+3):** No
- **Clase perezosa (+4):** No
- **Generalidad especulativa (+5):** No

##### Acopladores
- **Envidia de características (+5):** No
- **Intimidad inapropiada (+6):** No
- **Clase de biblioteca incompleta (+4):** No
- **Cadenas de mensajes (+7):** No
- **Hombre medio (+6):** No

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30):** 
  - La clase `ImagenController` maneja múltiples responsabilidades como cargar imágenes, guardar datos, y manejar la interfaz de usuario.
- **Principio Abierto/Cerrado (OCP) (+40):** No
- **Principio de Sustitución de Liskov (LSP) (+35):** No
- **Principio de Segregación de Interfaces (ISP) (+25):** No
- **Principio de Inversión de Dependencias (DIP) (+45):** No

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** No
  - Consejo: Utiliza el patrón de Fábrica Abstracta para crear diferentes tipos de objetos relacionados sin especificar sus clases concretas. Esto facilita la extensión y el mantenimiento del código.
- **Constructor (+25):** No
  - Consejo: Emplea un Constructor para simplificar la creación de instancias complejas de `ImagenController`, encapsulando la lógica de inicialización.
- **Método de Fábrica (+20):** No
  - Consejo: Usa el Método de Fábrica para encapsular la creación de objetos, lo que puede reducir la complejidad y mejorar la flexibilidad del código.

#### Estructurales
- **Adaptador (+25):** No
  - Consejo: Implementa el patrón Adaptador para permitir que clases con interfaces incompatibles trabajen juntas, facilitando la integración y el mantenimiento.
- **Puente (+35):** No
- **Compuesto (+30):** No
  - Consejo: Aplica el patrón Compuesto para representar jerarquías de objetos. Esto puede simplificar la gestión de colecciones de objetos similares.
- **Decorador (+25):** No
  - Consejo: Usa el patrón Decorador para añadir responsabilidades a los objetos de manera dinámica sin alterar su estructura básica.
- **Fachada (+20):** No
  - Consejo: Implementa una Fachada para proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema, mejorando la usabilidad del código.
- **Peso Ligero (+40):** No
- **Proxy (+30):** No

#### De comportamiento
- **Cadena de Responsabilidad (+30):** No
  - Consejo: Utiliza Cadena de Responsabilidad para permitir que múltiples objetos manejen una solicitud, reduciendo el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** No
  - Consejo: Aplica el patrón Comando para encapsular solicitudes como objetos, lo que permite parametrizar clientes con colas y solicitudes.
- **Intérprete (+40):** No
- **Iterador (+15):** No
  - Consejo: Emplea un Iterador para proporcionar una forma secuencial de acceder a los elementos de una colección sin exponer su representación subyacente.
- **Mediador (+30):** No
- **Memento (+35):** No
- **Observador (+25):** No
  - Consejo: Implementa el patrón Observador para notificar automáticamente a otros objetos sobre cambios en el estado de un objeto.
- **Estado (+30):** No
- **Estrategia (+20):** No
  - Consejo: Usa Estrategia para definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables, mejorando la flexibilidad y la reutilización del código.
- **Método Plantilla (+25):** No
  - Consejo: Aplica Método Plantilla para definir el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** No

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 1, 0) = (5 + 5 + 4 + 2) + 30 + 0 = 46
\]

### Resumen
La clase `ImagenController` presenta algunos malos olores de código, especialmente métodos largos y campos temporales. También hay violaciones del Principio de Responsabilidad Única (SRP). No se identificaron patrones de diseño faltantes significativos. El esfuerzo estimado para refactorizar esta clase es de 46 puntos.





Este repositorio fue obtenido de: https://github.com/rexman10/ED_Photos_P1
