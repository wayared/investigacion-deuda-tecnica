# Informe de Análisis de Código Angular y TypeScript

## Clase Analizada: `CrearRutaComponent`

### Descripción General

La clase `CrearRutaComponent` permite a los usuarios crear una ruta especificando una dirección de inicio y una dirección de fin. El componente utiliza el servicio `HttpClient` para interactuar con una API y obtener las coordenadas geográficas correspondientes a las direcciones proporcionadas. Luego, estos datos se envían al servicio `MapasService` para agregar la nueva ruta.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - Las funciones `obtenerCoordenadasInicio` y `obtenerCoordenadasFin` contienen demasiada lógica, lo que dificulta su mantenimiento y comprensión.

2. **Código Duplicado (+1):**
   - Las funciones `obtenerCoordenadasInicio` y `obtenerCoordenadasFin` tienen código repetido. Ambas realizan solicitudes HTTP similares y manejan los mismos tipos de errores.

3. **Uso Excesivo de Literales (+1):**
   - La URL de la API está codificada directamente en las funciones, lo que dificulta su actualización en caso de cambios.

4. **Múltiples Responsabilidades (+1):**
   - El componente maneja tanto la lógica de la vista como la lógica de negocio, lo que va en contra del principio de responsabilidad única.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - El componente `CrearRutaComponent` tiene múltiples responsabilidades: manejar la lógica de la interfaz de usuario, interactuar con el servicio HTTP, y manejar los errores.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La clase depende directamente de la implementación de `HttpClient` en lugar de una abstracción.

#### Patrones de Diseño no Utilizados

1. **Facade (+10):**
   - Una clase fachada podría manejar la lógica de obtención de coordenadas, reduciendo la complejidad del componente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 1) = (1 + 1 + 1 + 1) + (10 + 10) + (10) = 34
\]

### Comentarios Adicionales

- **Validación de Datos:**
  - Actualmente, no hay validación para asegurarse de que las direcciones proporcionadas sean válidas antes de realizar las solicitudes HTTP.

- **Gestión de Errores:**
  - La gestión de errores se realiza de manera duplicada en las funciones `obtenerCoordenadasInicio` y `obtenerCoordenadasFin`.

- **Configuración de HTTP:**
  - La configuración de la solicitud HTTP podría mejorarse utilizando una clase de servicio dedicada.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de obtención de coordenadas en un servicio dedicado. Esto permitirá que el componente `CrearRutaComponent` se concentre en la lógica de la interfaz de usuario.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Facade para encapsular la lógica de interacción con la API.

3. **Encapsulamiento de Literales:**
   - Utilizar constantes o variables de configuración para la URL de la API.

4. **Mejora de la Gestión de Errores:**
   - Crear una función común para manejar errores y reutilizarla en las solicitudes HTTP.

## Clase Analizada: `RutasComponent`

### Descripción General

La clase `RutasComponent` se encarga de mostrar rutas en un mapa utilizando la librería Leaflet. El componente obtiene los datos de las rutas desde un servicio y los renderiza en el mapa, permitiendo también filtrar las rutas mostradas.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - La función `crearMapa` contiene demasiada lógica, incluyendo la inicialización del mapa, la configuración de capas, la creación de marcadores y líneas, y el manejo de eventos.

2. **Código Duplicado (+1):**
   - La creación de marcadores para `restaurantes` y `restaurantes1` es similar y podría consolidarse en una función reutilizable.

3. **Uso Excesivo de Literales (+1):**
   - Las URLs de los iconos de los marcadores están codificadas directamente en el código.

4. **Múltiples Responsabilidades (+1):**
   - El componente maneja tanto la lógica de la interfaz de usuario como la lógica de negocio, lo que va en contra del principio de responsabilidad única.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - El componente `RutasComponent` tiene múltiples responsabilidades: manejar la lógica de la interfaz de usuario, interactuar con el servicio de mapas, y manejar la lógica de renderizado del mapa.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La clase depende directamente de la implementación de `HttpClient` en lugar de una abstracción.

#### Patrones de Diseño no Utilizados

1. **Facade (+10):**
   - Una clase fachada podría manejar la lógica de creación de marcadores y líneas, reduciendo la complejidad del componente.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 1) = (1 + 1 + 1 + 1) + (10 + 10) + (10) = 34
\]

### Comentarios Adicionales

- **Validación de Datos:**
  - Actualmente, no hay validación para asegurarse de que las coordenadas obtenidas sean válidas antes de agregarlas al mapa.

- **Gestión de Errores:**
  - La gestión de errores se realiza de manera mínima y podría mejorarse para proporcionar retroalimentación al usuario en caso de fallos.

- **Configuración de HTTP:**
  - La configuración de la solicitud HTTP podría mejorarse utilizando una clase de servicio dedicada para manejar las peticiones.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de creación de marcadores y líneas en un servicio dedicado. Esto permitirá que el componente `RutasComponent` se concentre en la lógica de la interfaz de usuario.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Facade para encapsular la lógica de creación y manipulación de marcadores y líneas en el mapa.

3. **Encapsulamiento de Literales:**
   - Utilizar constantes o variables de configuración para las URLs de los iconos de los marcadores.

4. **Mejora de la Gestión de Errores:**
   - Crear una función común para manejar errores y reutilizarla en las solicitudes HTTP.

## Clase Analizada: `RegisterComponent`

### Descripción General

La clase `RegisterComponent` es responsable de manejar la lógica del formulario de registro de usuarios. Permite a los usuarios crear una cuenta proporcionando un nombre de usuario, una contraseña y un rol. Utiliza servicios para interactuar con una API backend y redirigir al usuario a una página específica una vez registrado.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - La función `onSubmit` contiene múltiples responsabilidades, incluyendo la validación de usuarios y la lógica de envío del formulario.

2. **Acoplamiento Fuerte (+1):**
   - La lógica de enrutamiento y manejo de mensajes de éxito está acoplada directamente en la función `onSubmit`, lo que dificulta la reutilización y el mantenimiento.

3. **Manejo de Errores Mínimo (+1):**
   - El manejo de errores en la solicitud HTTP es básico y no proporciona retroalimentación adecuada al usuario en caso de fallos.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - La función `onSubmit` realiza múltiples tareas: validación de usuarios, envío de datos, y manejo de redirección y mensajes de éxito.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La clase depende directamente de la implementación de `Router`, `AuthenticationService`, y `DataService` en lugar de interfaces o abstracciones.

#### Patrones de Diseño no Utilizados

1. **Facade (+10):**
   - Un patrón Facade podría encapsular la lógica de interacción con los servicios y el enrutador, simplificando el componente y mejorando la separación de responsabilidades.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 1) = (1 + 1 + 1) + (10 + 10) + (10) = 33
\]


### Comentarios Adicionales

- **Validación de Datos:**
  - La validación de la existencia del usuario se realiza en el cliente, lo que puede ser ineficiente y propenso a condiciones de carrera si múltiples usuarios se registran simultáneamente.

- **Gestión de Estado:**
  - La gestión del estado del formulario podría beneficiarse del uso de un formulario reactivo (`ReactiveFormsModule`) para mejorar la validación y manejo del estado del formulario.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de validación de usuarios y la lógica de envío del formulario en funciones distintas. Considerar la creación de un servicio dedicado para la gestión del registro de usuarios.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Facade para encapsular la lógica de interacción con `DataService` y `Router`, mejorando la mantenibilidad y la prueba del código.

3. **Mejora del Manejo de Errores:**
   - Mejorar el manejo de errores en la solicitud HTTP para proporcionar retroalimentación adecuada al usuario en caso de fallos, y considerar el uso de un servicio de notificación para manejar mensajes de éxito y error.

4. **Uso de Formularios Reactivos:**
   - Considerar el uso de `ReactiveFormsModule` para mejorar la gestión del estado y la validación del formulario.


## Clase Analizada: `LoginComponent`

### Descripción General

La clase `LoginComponent` maneja la lógica del formulario de inicio de sesión. Permite a los usuarios iniciar sesión proporcionando un nombre de usuario y una contraseña. Utiliza servicios para interactuar con una API backend y para redirigir al usuario a la página de perfil una vez autenticado.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - La función `onSubmit` contiene múltiples responsabilidades, incluyendo la validación de usuarios y la lógica de redirección.

2. **Acoplamiento Fuerte (+1):**
   - La lógica de enrutamiento y manejo de mensajes de error está acoplada directamente en la función `onSubmit`, lo que dificulta la reutilización y el mantenimiento.

3. **Manejo de Errores Mínimo (+1):**
   - El manejo de errores en la autenticación es básico y no proporciona retroalimentación adecuada al usuario en caso de fallos.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - La función `onSubmit` realiza múltiples tareas: validación de usuarios, autenticación, y manejo de redirección y mensajes de error.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La clase depende directamente de la implementación de `Router`, `AuthenticationService`, y `SessionService` en lugar de interfaces o abstracciones.

#### Patrones de Diseño no Utilizados

1. **Facade (+10):**
   - Un patrón Facade podría encapsular la lógica de interacción con los servicios y el enrutador, simplificando el componente y mejorando la separación de responsabilidades.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 1) = (1 + 1 + 1) + (10 + 10) + (10) = 33
\]


### Comentarios Adicionales

- **Validación de Datos:**
  - La validación de la existencia del usuario se realiza en el cliente, lo que puede ser ineficiente y propenso a condiciones de carrera si múltiples usuarios intentan iniciar sesión simultáneamente.

- **Gestión de Estado:**
  - La gestión del estado del formulario podría beneficiarse del uso de un formulario reactivo (`ReactiveFormsModule`) para mejorar la validación y manejo del estado del formulario.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de validación de usuarios y la lógica de redirección en funciones distintas. Considerar la creación de un servicio dedicado para la gestión de la autenticación de usuarios.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Facade para encapsular la lógica de interacción con `AuthenticationService`, `SessionService` y `Router`, mejorando la mantenibilidad y la prueba del código.

3. **Mejora del Manejo de Errores:**
   - Mejorar el manejo de errores en la autenticación para proporcionar retroalimentación adecuada al usuario en caso de fallos, y considerar el uso de un servicio de notificación para manejar mensajes de error.

4. **Uso de Formularios Reactivos:**
   - Considerar el uso de `ReactiveFormsModule` para mejorar la gestión del estado y la validación del formulario.


Este repositorio fue obtenido de: https://github.com/JosueRodriguezr/LP_Final
