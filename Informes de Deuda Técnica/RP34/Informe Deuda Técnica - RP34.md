# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clases Analizadas: `GestorEstudiante` y Endpoints de Sinatra

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `GestorEstudiante` maneja múltiples responsabilidades, incluyendo la lectura, escritura y gestión de datos de estudiantes. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - Los métodos `write_data_to_csv` y `read_data_from_csv` realizan múltiples operaciones que podrían dividirse en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - En los endpoints de `POST`, `PUT` y `DELETE`, hay repetición de código para la lectura y escritura de datos en el archivo CSV.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase `GestorEstudiante` utiliza métodos *getter* y *setter* para acceder a los datos de los estudiantes, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `GestorEstudiante` viola este principio al manejar tanto la lógica de acceso a datos como la gestión de los estudiantes. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+20):**
  - Los endpoints de la API están directamente acoplados a la clase `GestorEstudiante`, lo que hace difícil cambiar la lógica de almacenamiento sin modificar los endpoints.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de `GestorEstudiante` con diferentes fuentes de datos de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de objetos `GestorEstudiante` con fuentes de datos personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los datos de los estudiantes, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los datos de los estudiantes de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de almacenamiento de datos (e.g., almacenamiento en CSV, almacenamiento en bases de datos) permitiendo cambiar fácilmente la estrategia de almacenamiento.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de almacenamiento de datos y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + (30 + 20) + (20 + 25 + 30) = 142
\]

La clase `GestorEstudiante` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 142 puntos.

### Clases Analizadas: `GestorEstudianteLibros` y Endpoints de Sinatra

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `GestorEstudianteLibros` maneja múltiples responsabilidades, incluyendo la lectura, escritura y gestión de datos de estudiantes y libros. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - Los métodos `write_data_to_csv` y `read_data_from_csv` realizan múltiples operaciones que podrían dividirse en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - En los endpoints de `POST` y `DELETE`, hay repetición de código para la lectura y escritura de datos en el archivo CSV.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase `GestorEstudianteLibros` utiliza métodos *getter* y *setter* para acceder a los datos de los estudiantes y libros, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `GestorEstudianteLibros` viola este principio al manejar tanto la lógica de acceso a datos como la gestión de los estudiantes y libros. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+20):**
  - Los endpoints de la API están directamente acoplados a la clase `GestorEstudianteLibros`, lo que hace difícil cambiar la lógica de almacenamiento sin modificar los endpoints.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de `GestorEstudianteLibros` con diferentes fuentes de datos de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de objetos `GestorEstudianteLibros` con fuentes de datos personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los datos de los estudiantes y libros, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los datos de los estudiantes y libros de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de almacenamiento de datos (e.g., almacenamiento en CSV, almacenamiento en bases de datos) permitiendo cambiar fácilmente la estrategia de almacenamiento.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de almacenamiento de datos y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + (30 + 20) + (20 + 25 + 30) = 142
\]

La clase `GestorEstudianteLibros` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 142 puntos.

### Clases Analizadas: `GestorLibros` y Endpoints de Sinatra

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `GestorLibros` maneja múltiples responsabilidades, incluyendo la lectura, escritura y gestión de datos de libros. Debería dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - Los métodos `write_data_to_csv` y `read_data_from_csv` realizan múltiples operaciones que podrían dividirse en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - En los endpoints de `POST`, `PUT` y `DELETE`, hay repetición de código para la lectura y escritura de datos en el archivo CSV.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase `GestorLibros` utiliza métodos *getter* y *setter* para acceder a los datos de los libros, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `GestorLibros` viola este principio al manejar tanto la lógica de acceso a datos como la gestión de los libros. Debería dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+20):**
  - Los endpoints de la API están directamente acoplados a la clase `GestorLibros`, lo que hace difícil cambiar la lógica de almacenamiento sin modificar los endpoints.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de `GestorLibros` con diferentes fuentes de datos de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de objetos `GestorLibros` con fuentes de datos personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los datos de los libros, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los datos de los libros de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de almacenamiento de datos (e.g., almacenamiento en CSV, almacenamiento en bases de datos) permitiendo cambiar fácilmente la estrategia de almacenamiento.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de almacenamiento de datos y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + (30 + 20) + (20 + 25 + 30) = 142
\]

La clase `GestorLibros` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 142 puntos.

### Clases Analizadas: `GestorEstudiante`, `GestorLibros`, `GestorEstudianteLibros` y Endpoints de Sinatra

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - Las clases `GestorEstudiante`, `GestorLibros` y `GestorEstudianteLibros` manejan múltiples responsabilidades, incluyendo la lectura, escritura y gestión de datos. Deberían dividirse en clases más pequeñas y especializadas.

- **Método Largo (+5):**
  - Los métodos `write_data_to_csv` y `read_data_from_csv` realizan múltiples operaciones que podrían dividirse en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - En los endpoints de `POST`, `PUT` y `DELETE`, hay repetición de código para la lectura y escritura de datos en el archivo CSV.

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - Las clases `GestorEstudiante`, `GestorLibros` y `GestorEstudianteLibros` utilizan métodos *getter* y *setter* para acceder a los datos, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - Las clases `GestorEstudiante`, `GestorLibros` y `GestorEstudianteLibros` violan este principio al manejar tanto la lógica de acceso a datos como la gestión de los mismos. Deberían dividirse en diferentes clases con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+20):**
  - Los endpoints de la API están directamente acoplados a las clases de gestores, lo que hace difícil cambiar la lógica de almacenamiento sin modificar los endpoints.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de `GestorEstudiante`, `GestorLibros` y `GestorEstudianteLibros` con diferentes fuentes de datos de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de objetos gestores con fuentes de datos personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los datos, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los datos de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de almacenamiento de datos (e.g., almacenamiento en CSV, almacenamiento en bases de datos) permitiendo cambiar fácilmente la estrategia de almacenamiento.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de almacenamiento de datos y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + (30 + 20) + (20 + 25 + 30) = 142
\]

Las clases `GestorEstudiante`, `GestorLibros` y `GestorEstudianteLibros` presentan varios malos olores de código, como métodos largos y código duplicado. También violan el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar estas clases es de 142 puntos.

Este repositorio fue obtenido de: https://github.com/damm2001/LP-Project---Backend
