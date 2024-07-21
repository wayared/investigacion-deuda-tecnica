# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clases Analizadas: `MainComponent`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `MainComponent` maneja múltiples responsabilidades, incluyendo la gestión de libros, la búsqueda, la edición y la eliminación de registros. Debería dividirse en componentes más pequeños y especializados.

- **Método Largo (+5):**
  - Los métodos `ngOnInit`, `search`, `guardarLibro` y `eliminarLibro` realizan múltiples operaciones que podrían dividirse en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - Existen operaciones repetitivas de manejo de solicitudes HTTP en varios métodos (`search`, `guardarLibro`, `eliminarLibro`, `editarValoracionLibro`).

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase utiliza métodos *getter* y *setter* para acceder a los datos, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `MainComponent` viola este principio al manejar tanto la lógica de la interfaz de usuario como la lógica de acceso a datos. Debería dividirse en diferentes servicios y componentes con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+20):**
  - La clase está directamente acoplada al servicio `HttpClient`, lo que dificulta el cambio de la lógica de acceso a datos sin modificar la clase.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de servicios HTTP con configuraciones personalizadas de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de instancias de servicios HTTP con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los datos de los libros, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los datos de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de manejo de solicitudes HTTP (e.g., búsqueda, adición, eliminación de libros) permitiendo cambiar fácilmente la estrategia de manejo de solicitudes.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de manejo de solicitudes HTTP y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + (30 + 20) + (20 + 25 + 30) = 142
\]

La clase `MainComponent` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 142 puntos.

### Clases Analizadas: `AboutComponent`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+6):**
  - La clase `AboutComponent` maneja múltiples responsabilidades, incluyendo la gestión de reservas de libros, la obtención de listas de estudiantes y libros, y la edición de la disponibilidad de libros. Debería dividirse en componentes más pequeños y especializados.

- **Método Largo (+5):**
  - Los métodos `ngOnInit`, `guardarReserva`, `obtenerListaEstudiantes`, `obtenerListaLibrosDisponibles`, y `editarDispLibro` realizan múltiples operaciones que podrían dividirse en métodos más pequeños y especializados.

##### Dispensables

- **Código duplicado (+4):**
  - Existen operaciones repetitivas de manejo de solicitudes HTTP en varios métodos (`guardarReserva`, `obtenerListaEstudiantes`, `obtenerListaLibrosDisponibles`, `editarDispLibro`).

##### Abusadores de Orientación a Objetos

- **Métodos *getter* y *setter* (+2):**
  - La clase utiliza métodos *getter* y *setter* para acceder a los datos, lo cual puede ser una señal de un diseño pobre orientado a objetos.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+30):**
  - La clase `AboutComponent` viola este principio al manejar tanto la lógica de la interfaz de usuario como la lógica de acceso a datos. Debería dividirse en diferentes servicios y componentes con responsabilidades únicas.

- **Principio de Inversión de Dependencias (DIP) (+20):**
  - La clase está directamente acoplada al servicio `HttpClient`, lo que dificulta el cambio de la lógica de acceso a datos sin modificar la clase.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+20):**
  - Podría usarse para crear instancias de servicios HTTP con configuraciones personalizadas de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de instancias de servicios HTTP con configuraciones personalizadas.

#### Estructurales

- **Composite (+25):**
  - Podría implementarse para manejar la estructura de los datos de los libros, permitiendo tratar tanto a los elementos individuales como a las estructuras compuestas de manera uniforme.

    **Consejo:** Implementar el patrón Composite para gestionar la estructura de los datos de manera más flexible y escalable.

#### De comportamiento

- **Strategy (+30):**
  - Podría utilizarse para encapsular las diferentes estrategias de manejo de solicitudes HTTP (e.g., búsqueda, adición, eliminación de reservas) permitiendo cambiar fácilmente la estrategia de manejo de solicitudes.

    **Consejo:** Utilizar el patrón Strategy para encapsular las estrategias de manejo de solicitudes HTTP y permitir cambiar la estrategia fácilmente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 1, 0) = (6 + 5 + 4 + 2) + (30 + 20) + (20 + 25 + 30) = 142
\]

La clase `AboutComponent` presenta varios malos olores de código, como métodos largos y código duplicado. También viola el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 142 puntos.

### Clases Analizadas: `RegistroServService`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+1):**
  - La clase `RegistroServService` es relativamente pequeña y manejable, pero aún se puede considerar la posible expansión de métodos futuros.

##### Abusadores de Orientación a Objetos

- **Métodos getter y setter (+2):**
  - La clase tiene un método `getResponse` que actúa como un getter para realizar una solicitud HTTP. Aunque esto es común en servicios de Angular, es algo a tener en cuenta si la clase crece en complejidad.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+10):**
  - La clase `RegistroServService` cumple con el SRP al enfocarse únicamente en las operaciones relacionadas con el manejo de registros de estudiantes.

- **Principio de Inversión de Dependencias (DIP) (+10):**
  - La clase depende directamente de `HttpClient`, lo que puede limitar la capacidad de realizar pruebas unitarias aisladas. Se puede considerar la inyección de dependencias más flexibles o interfaces para mejorar la testabilidad.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+10):**
  - Podría usarse para la creación de instancias de `HttpClient` con configuraciones personalizadas de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de instancias de `HttpClient` con configuraciones personalizadas.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(1, 1, 1) = (1 + 2) + (10 + 10) + (10) = 33
\]

La clase `RegistroServService` presenta pocos malos olores de código, como el método getter y setter. También se puede mejorar con respecto al Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 33 puntos.

### Clases Analizadas: `LibrosserviceService`

#### Identificación de Olores de Código

##### Acaparadores

- **Clase Grande (+1):**
  - La clase `LibrosserviceService` maneja múltiples responsabilidades relacionadas con libros y rutas, lo que puede llevar a una clase grande si no se gestiona adecuadamente.

##### Abusadores de Orientación a Objetos

- **Uso excesivo de literales (+2):**
  - La clase tiene múltiples URLs como literales. Aunque esto es común en servicios HTTP, puede ser un problema si las URLs cambian con frecuencia.

##### Falta de Encapsulamiento

- **Exposición de detalles internos (+2):**
  - La clase expone directamente los métodos HTTP sin encapsular la lógica de negocio, lo que puede llevar a problemas de mantenimiento y evolución del código.

#### Violaciones de los Principios SOLID

- **Principio de Responsabilidad Única (SRP) (+10):**
  - La clase `LibrosserviceService` maneja tanto operaciones de libros como de rutas y estudiantes, violando el SRP. 

    **Consejo:** Dividir la clase en servicios más pequeños y especializados, como `LibrosService`, `EstudiantesLibrosService` y `RutasService`.

- **Principio de Inversión de Dependencias (DIP) (+10):**
  - La clase depende directamente de `HttpClient`, lo que puede limitar la capacidad de realizar pruebas unitarias aisladas. Se puede considerar la inyección de dependencias más flexibles o interfaces para mejorar la testabilidad.

#### Patrones de diseño no utilizados

#### Creacionales

- **Factory Method (+10):**
  - Podría usarse para la creación de instancias de `HttpClient` con configuraciones personalizadas de manera más flexible y clara.

    **Consejo:** Utilizar el patrón Factory Method para la creación de instancias de `HttpClient` con configuraciones personalizadas.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(5, 2, 1) = (1 + 2 + 2) + (10 + 10) + (10) = 35
\]

La clase `LibrosserviceService` presenta varios malos olores de código, como la clase grande y el uso excesivo de literales. También se puede mejorar con respecto al Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP). El esfuerzo estimado para refactorizar esta clase es de 35 puntos.


Este repositorio fue obtenido de: https://github.com/damm2001/LP-Project---FrontEnd
