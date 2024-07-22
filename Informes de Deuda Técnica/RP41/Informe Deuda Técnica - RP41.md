# Informe de Análisis de Código PHP

## Clase Analizada: `LpBackend.php`

### Descripción General

El archivo `LpBackend.php` contiene una función `postDenuncia` que se encarga de recibir datos de una denuncia, validarlos, asignarles un nuevo ID, y luego enviar estos datos a una base de datos Firebase usando cURL. También incluye configuraciones de encabezados HTTP para manejar CORS.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - La función `postDenuncia` realiza múltiples tareas, incluyendo la validación de datos, configuración y ejecución de cURL, y la manipulación de datos.

2. **Código Duplicado (+1):**
   - La URL del endpoint de Firebase se utiliza varias veces en la función.

3. **Comentarios Innecesarios (+1):**
   - Algunos comentarios explican operaciones simples que podrían entenderse fácilmente con nombres de variables y funciones bien elegidos.

4. **Variables Temporales Innecesarias (+1):**
   - Las variables temporales como `$response` y `$existingData` podrían manejarse directamente en las operaciones.

5. **Uso Excesivo de Literales (+1):**
   - Varios valores están codificados directamente en la función, como la URL de Firebase y los nombres de los campos de la denuncia.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - La función `postDenuncia` tiene múltiples responsabilidades: validación de datos, asignación de ID, y comunicación con la base de datos. Debería dividirse en funciones más pequeñas con responsabilidades específicas.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La función depende directamente de cURL para la comunicación HTTP. Sería mejor utilizar una abstracción para la comunicación HTTP que permita cambiar fácilmente la implementación subyacente.

#### Patrones de Diseño no Utilizados

1. **Factory Method (+10):**
   - Podría usarse para la creación de instancias de cURL con configuraciones personalizadas de manera más flexible y clara.

2. **Facade (+10):**
   - La interacción con la base de datos de Firebase podría encapsularse dentro de una clase fachada que oculte la complejidad de las llamadas cURL.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 2) = (1 + 1 + 1 + 1) + (10 + 10) + (10 + 10) = 44
\]

### Comentarios Adicionales

- **Validación de Datos:**
  - La función valida que ciertos campos no estén vacíos, pero no verifica otros posibles errores en los datos.

- **Gestión de Errores:**
  - La función maneja errores de cURL, pero no otros posibles errores que puedan ocurrir en el proceso.

- **Configuración de cURL:**
  - La configuración de cURL se repite varias veces en la función. Podría beneficiarse de una función auxiliar que maneje esta configuración.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Dividir la función `postDenuncia` en varias funciones más pequeñas, cada una con una responsabilidad única, como `validarDatos`, `asignarId`, `configurarCurl`, y `enviarDatosFirebase`.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Factory Method para la creación de instancias de cURL.
   - Crear una clase fachada para manejar todas las interacciones con Firebase.

3. **Encapsulamiento de Literales:**
   - Utilizar constantes o variables de configuración para valores como la URL de Firebase y los nombres de los campos.

4. **Mejora de la Gestión de Errores:**
   - Implementar una mejor gestión de errores que incluya la validación de datos y otros posibles errores en el proceso.

## Clase Analizada: `lpCambiarEstado.php`

### Descripción General

El archivo `lpCambiarEstado.php` contiene una función `cambiarEstado` que se encarga de cambiar el estado de una denuncia en una base de datos Firebase. Utiliza cURL para realizar las operaciones de red. También incluye configuraciones de encabezados HTTP para manejar CORS.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - La función `cambiarEstado` realiza múltiples tareas, incluyendo la configuración de cURL, la obtención de datos, la actualización del estado y la conversión a JSON.

2. **Código Duplicado (+1):**
   - La URL del endpoint de Firebase se utiliza varias veces en la función.

3. **Comentarios Innecesarios (+1):**
   - Algunos comentarios explican operaciones simples que podrían entenderse fácilmente con nombres de variables y funciones bien elegidos.

4. **Uso Excesivo de Literales (+1):**
   - Varios valores están codificados directamente en la función, como la URL de Firebase y los nombres de los estados.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - La función `cambiarEstado` tiene múltiples responsabilidades: obtención de datos, actualización del estado y comunicación con la base de datos. Debería dividirse en funciones más pequeñas con responsabilidades específicas.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La función depende directamente de cURL para la comunicación HTTP. Sería mejor utilizar una abstracción para la comunicación HTTP que permita cambiar fácilmente la implementación subyacente.

#### Patrones de Diseño no Utilizados

1. **Factory Method (+10):**
   - Podría usarse para la creación de instancias de cURL con configuraciones personalizadas de manera más flexible y clara.

2. **Facade (+10):**
   - La interacción con la base de datos de Firebase podría encapsularse dentro de una clase fachada que oculte la complejidad de las llamadas cURL.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 2) = (1 + 1 + 1 + 1) + (10 + 10) + (10 + 10) = 44
\]


### Comentarios Adicionales

- **Validación de Datos:**
  - La función valida que el ID esté presente en los datos de la solicitud, pero no verifica otros posibles errores en los datos.

- **Gestión de Errores:**
  - La función maneja errores de cURL, pero no otros posibles errores que puedan ocurrir en el proceso.

- **Configuración de cURL:**
  - La configuración de cURL se repite varias veces en la función. Podría beneficiarse de una función auxiliar que maneje esta configuración.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Dividir la función `cambiarEstado` en varias funciones más pequeñas, cada una con una responsabilidad única, como `obtenerDatos`, `actualizarEstado`, `configurarCurl`, y `enviarDatosFirebase`.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Factory Method para la creación de instancias de cURL.
   - Crear una clase fachada para manejar todas las interacciones con Firebase.

3. **Encapsulamiento de Literales:**
   - Utilizar constantes o variables de configuración para valores como la URL de Firebase y los nombres de los estados.

4. **Mejora de la Gestión de Errores:**
   - Implementar una mejor gestión de errores que incluya la validación de datos y otros posibles errores en el proceso.

## Clase Analizada: `lpVotar.php`

### Descripción General

El archivo `lpVotar.php` contiene una función `incrementarVoto` que se encarga de incrementar el conteo de votos para una denuncia específica en una base de datos Firebase. Utiliza cURL para realizar las operaciones de red. También incluye configuraciones de encabezados HTTP para manejar CORS.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - La función `incrementarVoto` realiza múltiples tareas, incluyendo la configuración de cURL, la obtención de datos, la actualización del voto y la conversión a JSON.

2. **Código Duplicado (+1):**
   - La URL del endpoint de Firebase se utiliza varias veces en la función.

3. **Uso Excesivo de Literales (+1):**
   - Varios valores están codificados directamente en la función, como la URL de Firebase.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - La función `incrementarVoto` tiene múltiples responsabilidades: obtención de datos, actualización del voto y comunicación con la base de datos. Debería dividirse en funciones más pequeñas con responsabilidades específicas.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La función depende directamente de cURL para la comunicación HTTP. Sería mejor utilizar una abstracción para la comunicación HTTP que permita cambiar fácilmente la implementación subyacente.

#### Patrones de Diseño no Utilizados

1. **Factory Method (+10):**
   - Podría usarse para la creación de instancias de cURL con configuraciones personalizadas de manera más flexible y clara.

2. **Facade (+10):**
   - La interacción con la base de datos de Firebase podría encapsularse dentro de una clase fachada que oculte la complejidad de las llamadas cURL.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 2) = (1 + 1 + 1) + (10 + 10) + (10 + 10) = 43
\]

### Comentarios Adicionales

- **Validación de Datos:**
  - La función valida que el ID esté presente en los datos de la solicitud, pero no verifica otros posibles errores en los datos.

- **Gestión de Errores:**
  - La función maneja errores de cURL, pero no otros posibles errores que puedan ocurrir en el proceso.

- **Configuración de cURL:**
  - La configuración de cURL se repite varias veces en la función. Podría beneficiarse de una función auxiliar que maneje esta configuración.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Dividir la función `incrementarVoto` en varias funciones más pequeñas, cada una con una responsabilidad única, como `obtenerDatos`, `actualizarVoto`, `configurarCurl`, y `enviarDatosFirebase`.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Factory Method para la creación de instancias de cURL.
   - Crear una clase fachada para manejar todas las interacciones con Firebase.

3. **Encapsulamiento de Literales:**
   - Utilizar constantes o variables de configuración para valores como la URL de Firebase.

4. **Mejora de la Gestión de Errores:**
   - Implementar una mejor gestión de errores que incluya la validación de datos y otros posibles errores en el proceso.

## Clase Analizada: `lpRanking.php`

### Descripción General

El archivo `lpRanking.php` contiene código que realiza las siguientes tareas:

1. Configura los encabezados HTTP para manejar CORS.
2. Obtiene los datos existentes de una base de datos Firebase.
3. Ordena los datos por el atributo `voto` en orden descendente.
4. Retorna los 10 primeros resultados como un JSON.

### Identificación de Olores de Código

#### Olores de Código

1. **Función Grande (+1):**
   - Todo el proceso se maneja dentro de un único bloque, lo que hace que la función sea difícil de mantener y extender.

2. **Código Duplicado (+1):**
   - La URL del endpoint de Firebase se utiliza varias veces.

3. **Uso Excesivo de Literales (+1):**
   - La URL de Firebase está codificada directamente en el código.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - El archivo actual tiene múltiples responsabilidades: configuración de CORS, obtención de datos, ordenación de datos y retorno de resultados.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La lógica depende directamente de cURL para realizar las solicitudes HTTP. Utilizar una abstracción para manejar estas solicitudes podría mejorar la flexibilidad.

#### Patrones de Diseño no Utilizados

1. **Facade (+10):**
   - La interacción con Firebase podría encapsularse dentro de una clase fachada, mejorando la modularidad y la legibilidad.

2. **Factory Method (+10):**
   - Podría utilizarse para crear instancias de cURL con configuraciones personalizadas de manera más flexible.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 2) = (1 + 1 + 1) + (10 + 10) + (10 + 10) = 43
\]

### Comentarios Adicionales

- **Validación de Datos:**
  - No hay validación para asegurarse de que los datos obtenidos de Firebase sean válidos y contengan el campo `voto`.

- **Gestión de Errores:**
  - Solo se maneja el error de cURL, pero no se manejan otros posibles errores que pueden ocurrir durante el proceso.

- **Configuración de cURL:**
  - La configuración de cURL se realiza varias veces y podría encapsularse en una función auxiliar para mejorar la legibilidad y el mantenimiento.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Dividir el código en funciones más pequeñas, cada una con una responsabilidad única, como `configurarCors`, `obtenerDatos`, `ordenarDatos`, y `retornarResultados`.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Factory Method para la creación de instancias de cURL.
   - Crear una clase fachada para manejar todas las interacciones con Firebase.

3. **Encapsulamiento de Literales:**
   - Utilizar constantes o variables de configuración para valores como la URL de Firebase.

4. **Mejora de la Gestión de Errores:**
   - Implementar una mejor gestión de errores que incluya la validación de datos y otros posibles errores en el proceso.



Este repositorio fue obtenido de: https://github.com/CarlosLoorB/LP2PARCIAL
