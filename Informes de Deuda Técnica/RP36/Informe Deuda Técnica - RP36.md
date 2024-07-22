## Clase Analizada: parser_1.py

### Identificación de Olores de Código

#### Acaparadores
- **Clase Grande (+6):** La clase parser_1.py tiene múltiples responsabilidades, como el análisis sintáctico y la gestión de estructuras de datos, violando el principio de responsabilidad única.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos como los resultados del análisis y las líneas de código.
- **Grupos de Datos (+3):** Las variables relacionadas con el análisis sintáctico podrían encapsularse en una clase dedicada.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase parser_1.py tiene múltiples razones para cambiar debido a su alto número de responsabilidades.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica del análisis requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
- **Comentarios (+2):** Existen muchos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para el análisis sintáctico y la gestión de estructuras de datos se repite en varios lugares de la clase parser_1.py.
- **Clase de datos (+5):** La clase parser_1.py actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión del análisis sintáctico.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores
- **Envidia de características (+5):** El método `analisis_sintactico` utiliza intensivamente métodos de la clase `parser`.
- **Intimidad inapropiada (+6):** La clase parser_1.py accede frecuentemente a métodos y variables privadas de la clase `parser`.
- **Cadenas de mensajes (+7):** El método `analisis_sintactico` realiza varias llamadas en cadena a métodos de la clase `parser`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase parser_1.py tiene múltiples responsabilidades, como el análisis sintáctico y la gestión de estructuras de datos.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase parser_1.py no es fácilmente extensible sin modificar su código fuente, especialmente en el método `analisis_sintactico`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase parser_1.py depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión del análisis sintáctico.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de análisis sintáctico sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de parser_1.py.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de análisis sintáctico y reducir la complejidad en parser_1.py.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el análisis sintáctico.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de análisis sintáctico.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de análisis sintáctico de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de análisis sintáctico.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de análisis sintáctico, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de análisis sintáctico.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de reglas de análisis sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase parser_1.py.
- **Observador (+25):** Podría permitir que un objeto parser_1.py notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto parser_1.py altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de análisis sintáctico, encapsular cada uno, y hacerlos intercambiables en parser_1.py.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de análisis en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de análisis de la estructura de objeto sobre la que opera.

## Clase Analizada: parser2.py

### Identificación de Olores de Código

#### Acaparadores
- **Clase Grande (+6):** La clase parser2.py tiene múltiples responsabilidades, como el análisis sintáctico y la gestión de estructuras de datos, violando el principio de responsabilidad única.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos como los resultados del análisis y las líneas de código.
- **Grupos de Datos (+3):** Las variables relacionadas con el análisis sintáctico podrían encapsularse en una clase dedicada.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase parser2.py tiene múltiples razones para cambiar debido a su alto número de responsabilidades.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica del análisis requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
- **Comentarios (+2):** Existen muchos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para el análisis sintáctico y la gestión de estructuras de datos se repite en varios lugares de la clase parser2.py.
- **Clase de datos (+5):** La clase parser2.py actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión del análisis sintáctico.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores
- **Envidia de características (+5):** El método `analisis_sintactico` utiliza intensivamente métodos de la clase `parser`.
- **Intimidad inapropiada (+6):** La clase parser2.py accede frecuentemente a métodos y variables privadas de la clase `parser`.
- **Cadenas de mensajes (+7):** El método `analisis_sintactico` realiza varias llamadas en cadena a métodos de la clase `parser`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase parser2.py tiene múltiples responsabilidades, como el análisis sintáctico y la gestión de estructuras de datos.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase parser2.py no es fácilmente extensible sin modificar su código fuente, especialmente en el método `analisis_sintactico`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase parser2.py depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión del análisis sintáctico.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de análisis sintáctico sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de parser2.py.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de análisis sintáctico y reducir la complejidad en parser2.py.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el análisis sintáctico.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de análisis sintáctico.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de análisis sintáctico de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de análisis sintáctico.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de análisis sintáctico, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de análisis sintáctico.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de reglas de análisis sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase parser2.py.
- **Observador (+25):** Podría permitir que un objeto parser2.py notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto parser2.py altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de análisis sintáctico, encapsular cada uno, y hacerlos intercambiables en parser2.py.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de análisis en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de análisis de la estructura de objeto sobre la que opera.

## Clase Analizada: lexer.txt

### Identificación de Olores de Código

#### Acaparadores
- **Clase Grande (+6):** La clase lexer.txt tiene múltiples responsabilidades, como el análisis léxico y la gestión de expresiones regulares, violando el principio de responsabilidad única.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos como los resultados del análisis léxico.
- **Grupos de Datos (+3):** Las variables relacionadas con el análisis léxico podrían encapsularse en una clase dedicada.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase lexer.txt tiene múltiples razones para cambiar debido a su alto número de responsabilidades.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica del análisis requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
- **Comentarios (+2):** Existen muchos comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para el análisis léxico y la gestión de expresiones regulares se repite en varios lugares de la clase lexer.txt.
- **Clase de datos (+5):** La clase lexer.txt actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión del análisis léxico.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores
- **Envidia de características (+5):** El método `analisis_lexico` utiliza intensivamente métodos de la clase `validador`.
- **Intimidad inapropiada (+6):** La clase lexer.txt accede frecuentemente a métodos y variables privadas de la clase `validador`.
- **Cadenas de mensajes (+7):** El método `analisis_lexico` realiza varias llamadas en cadena a métodos de la clase `validador`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase lexer.txt tiene múltiples responsabilidades, como el análisis léxico y la gestión de expresiones regulares.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase lexer.txt no es fácilmente extensible sin modificar su código fuente, especialmente en el método `analisis_lexico`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase lexer.txt depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión del análisis léxico.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de análisis léxico sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de lexer.txt.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de análisis léxico y reducir la complejidad en lexer.txt.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el análisis léxico.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de análisis léxico.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de análisis léxico de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de análisis léxico.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de análisis léxico, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de análisis léxico.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de reglas de análisis sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase lexer.txt.
- **Observador (+25):** Podría permitir que un objeto lexer.txt notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto lexer.txt altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de análisis léxico, encapsular cada uno, y hacerlos intercambiables en lexer.txt.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de análisis en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de análisis de la estructura de objeto sobre la que opera.


## Clase Analizada: Main

### Identificación de Olores de Código

#### Acaparadores
- **Método Largo (+5):** El método `ev_archivo()` tiene una longitud considerable, lo que podría dificultar su lectura y mantenimiento. Podría dividirse en métodos más pequeños y manejables.
- **Clase Grande (+6):** La clase Main tiene múltiples responsabilidades, como la gestión de la interfaz de usuario, el análisis léxico y sintáctico, y la manipulación de archivos, violando el principio de responsabilidad única.
- **Obsesión Primitiva (+3):** Uso de tipos primitivos para representar datos complejos como los resultados del análisis léxico y sintáctico.
- **Grupos de Datos (+3):** Las variables relacionadas con los resultados del análisis podrían encapsularse en una clase dedicada.

#### Preventores de Cambio
- **Cambio divergente (+6):** La clase Main tiene múltiples razones para cambiar debido a su alto número de responsabilidades.
- **Cirugía de escopeta (+8):** Cambios pequeños en la lógica del análisis o la interfaz de usuario requieren modificaciones en múltiples métodos y clases relacionadas.

#### Dispensables
- **Comentarios (+2):** Existen comentarios en el código que podrían evitarse con un código más claro y autoexplicativo.
- **Código duplicado (+7):** El código para el análisis léxico y sintáctico se repite en varios lugares de la clase Main.
- **Clase de datos (+5):** La clase Main actúa como una estructura de datos sin comportamiento significativo en algunos aspectos, especialmente en la gestión del análisis léxico y sintáctico.
- **Código muerto (+3):** Existen métodos y variables no utilizados.

#### Acopladores
- **Envidia de características (+5):** El método `ev_sintactico()` utiliza intensivamente métodos de la clase `analisis_sintactico2`.
- **Intimidad inapropiada (+6):** La clase Main accede frecuentemente a métodos y variables privadas de la clase `analisis_lexico` y `analisis_sintactico2`.
- **Cadenas de mensajes (+7):** El método `ev_sintactico()` realiza varias llamadas en cadena a métodos de la clase `analisis_sintactico2`.

### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):** La clase Main tiene múltiples responsabilidades, como la gestión de la interfaz de usuario, el análisis léxico y sintáctico, y la manipulación de archivos.
- **Principio Abierto/Cerrado (OCP) (+40):** La clase Main no es fácilmente extensible sin modificar su código fuente, especialmente en los métodos `ev_lexico()` y `ev_sintactico()`.
- **Principio de Inversión de Dependencias (DIP) (+45):** La clase Main depende directamente de implementaciones concretas en lugar de abstracciones, especialmente en la gestión del análisis léxico y sintáctico.

### Patrones de diseño no utilizados

#### Creacionales
- **Fábrica Abstracta (+20):** Podría utilizarse para crear diferentes tipos de análisis léxico y sintáctico sin especificar sus clases concretas.
- **Constructor (+25):** Utilizar un constructor para simplificar la creación de instancias complejas de Main.
- **Método de Fábrica (+20):** Podría usarse para encapsular la creación de análisis léxico y sintáctico y reducir la complejidad en Main.

#### Estructurales
- **Adaptador (+25):** Podría utilizarse para permitir que clases con interfaces incompatibles trabajen juntas, especialmente en el análisis léxico y sintáctico.
- **Compuesto (+30):** Podría ser útil para representar jerarquías de análisis léxico y sintáctico.
- **Decorador (+25):** Podría usarse para añadir responsabilidades a objetos de análisis léxico y sintáctico de manera dinámica.
- **Fachada (+20):** Podría proporcionar una interfaz simplificada a un conjunto de interfaces en un subsistema de análisis léxico y sintáctico.

#### De comportamiento
- **Cadena de Responsabilidad (+30):** Podría permitir que múltiples objetos manejen una solicitud de análisis léxico o sintáctico, evitando el acoplamiento entre el emisor y el receptor.
- **Comando (+20):** Podría encapsular una solicitud como un objeto, permitiendo parametrizar clientes con colas, solicitudes y operaciones de análisis léxico y sintáctico.
- **Iterador (+15):** Podría proporcionar una forma de acceder secuencialmente a los elementos de una colección de reglas de análisis sin exponer su representación subyacente.
- **Mediador (+30):** Podría reducir las dependencias caóticas entre objetos de la clase Main.
- **Observador (+25):** Podría permitir que un objeto Main notifique a otros objetos sobre cambios en su estado.
- **Estado (+30):** Podría permitir que un objeto Main altere su comportamiento cuando su estado interno cambia.
- **Estrategia (+20):** Podría definir una familia de algoritmos de análisis léxico y sintáctico, encapsular cada uno, y hacerlos intercambiables en Main.
- **Método Plantilla (+25):** Podría definir el esqueleto de un algoritmo de análisis en una operación, dejando algunos pasos a las subclases.
- **Visitante (+35):** Podría separar un algoritmo de análisis de la estructura de objeto sobre la que opera.



Este repositorio fue obtenido de: https://github.com/meiyincr3/analizador-proyecto
