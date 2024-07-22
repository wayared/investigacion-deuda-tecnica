# Informe de Análisis de Código PHP

## Clase Analizada: `Producto`

### Descripción General

La clase `Producto` maneja la gestión de productos en una tienda en línea. Permite agregar, leer, y filtrar productos utilizando un archivo JSON para el almacenamiento de datos.

### Identificación de Olores de Código

#### Olores de Código

1. **Funciones Grandes (+1):**
   - Métodos como `addProducts` y `readProducts` contienen múltiples responsabilidades y podrían beneficiarse de la separación en funciones más pequeñas.

2. **Acoplamiento Fuerte (+1):**
   - La clase depende directamente de la estructura del archivo JSON y su ubicación específica (`../Datos/Productos.json`), lo que puede dificultar la modificación y pruebas del código.

3. **Código Repetitivo (+1):**
   - Varias operaciones de lectura del archivo JSON se repiten en múltiples métodos. Consolidar estas operaciones en un método separado podría mejorar la mantenibilidad.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - La clase `Producto` tiene múltiples responsabilidades, incluyendo la gestión de productos y el manejo de archivos JSON, lo cual debería estar separado en diferentes clases.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La clase depende directamente de la implementación del almacenamiento (archivo JSON) en lugar de una abstracción, lo que dificulta el cambio de la fuente de datos.

#### Patrones de Diseño no Utilizados

1. **Repository Pattern (+10):**
   - Implementar un patrón Repository para manejar la interacción con el almacenamiento de datos podría mejorar la separación de preocupaciones y facilitar el mantenimiento del código.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(3, 2, 1) = (1 + 1 + 1) + (10 + 10) + (10) = 33
\]

### Comentarios Adicionales

- **Gestión de Errores:**
  - Actualmente, el manejo de errores en la lectura y escritura del archivo JSON es mínimo. Mejorar el manejo de excepciones y errores podría aumentar la robustez del código.

- **Validación de Datos:**
  - Asegurarse de que los datos se validen adecuadamente antes de realizar operaciones de escritura o lectura en el archivo JSON para evitar inconsistencias.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de gestión de productos y la lógica de manejo de archivos en diferentes clases. Por ejemplo, una clase `Producto` para la entidad del producto y una clase `ProductoRepository` para la gestión de datos.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Repository para manejar la interacción con el almacenamiento de datos, mejorando la mantenibilidad y la separación de preocupaciones.

3. **Mejora del Manejo de Errores:**
   - Añadir manejo de excepciones y validación de datos para todas las operaciones de lectura y escritura en el archivo JSON.

## Archivo Analizado: `carritoapi.php`

### Descripción General

El archivo `carritoapi.php` maneja una API RESTful para la gestión de carritos de compras, permitiendo operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los carritos almacenados en un archivo JSON.

### Identificación de Olores de Código

#### Olores de Código

1. **Funciones Grandes (+1):**
   - Las funciones dentro de los casos del `switch` realizan múltiples operaciones, lo que dificulta la lectura y mantenimiento del código.

2. **Manipulación Directa de JSON (+1):**
   - La manipulación directa de archivos JSON puede llevar a problemas de concurrencia y corrupción de datos.

3. **Acoplamiento Fuerte (+1):**
   - El código depende fuertemente de la estructura del archivo JSON y de la clase `Carrito`, lo que dificulta el cambio de almacenamiento o estructura de datos.

4. **Código Duplicado (+1):**
   - La lógica para leer y escribir archivos JSON se repite en múltiples lugares.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - El manejo de solicitudes HTTP y la manipulación de archivos JSON están mezclados, lo que debería estar separado en diferentes responsabilidades.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - El código depende directamente de la implementación de almacenamiento en archivos JSON en lugar de depender de una abstracción, lo que dificulta la prueba y el mantenimiento.

#### Patrones de Diseño no Utilizados

1. **Repository Pattern (+10):**
   - Implementar un patrón Repository para manejar la interacción con el almacenamiento de datos mejoraría la separación de preocupaciones y la mantenibilidad del código.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 1) = (1 + 1 + 1 + 1) + (10 + 10) + (10) = 34
\]

### Comentarios Adicionales

- **Seguridad:**
  - Es crucial validar y sanitizar todos los datos de entrada para proteger la aplicación contra ataques como inyección de JSON y Cross-Site Scripting (XSS).

- **Manejo de Errores:**
  - Mejorar el manejo de errores para proporcionar retroalimentación más útil en caso de fallos, tanto en el servidor como en el cliente.

### Recomendaciones de Refactorización

1. **Separación de Responsabilidades:**
   - Separar la lógica de manejo de solicitudes HTTP de la lógica de manipulación de archivos JSON. Crear una clase o servicio dedicado para la interacción con el almacenamiento.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Repository para manejar las operaciones CRUD sobre los carritos, lo que permitirá cambiar fácilmente el backend de almacenamiento si es necesario en el futuro.

3. **Mejora del Manejo de Errores:**
   - Añadir manejo de excepciones y validación de datos para todas las operaciones de lectura y escritura del archivo JSON para mejorar la robustez del código.


#### FrontEnd
  
## Componente Analizado: `CarritoComponent`

### Descripción General

El componente `CarritoComponent` maneja la visualización y administración del carrito de compras del usuario. Proporciona funcionalidades para listar los productos en el carrito, eliminar productos y realizar una compra.

### Identificación de Olores de Código

#### Olores de Código

1. **Funciones Grandes (+1):**
   - Métodos como `ngOnInit` y `comprar` contienen múltiples responsabilidades, lo que dificulta la lectura y mantenimiento del código.

2. **Variables Sin Inicializar (+1):**
   - Varias variables como `p`, `c`, y `total` no se inicializan correctamente, lo que podría llevar a comportamientos inesperados.

3. **Acoplamiento Fuerte (+1):**
   - El componente tiene una fuerte dependencia de los servicios `ProductoService` y `CarritoService`, lo que dificulta la prueba y mantenimiento del código.

4. **Código Repetitivo (+1):**
   - La lógica para manejar productos y cantidades se repite en varios lugares del código, lo que podría beneficiarse de una abstracción.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - El método `ngOnInit` tiene múltiples responsabilidades: obtener el carrito, obtener los productos y calcular el total, lo que debería estar separado en diferentes métodos.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - El componente depende directamente de la implementación de los servicios en lugar de abstracciones, lo que dificulta el cambio y la prueba de estas dependencias.

#### Patrones de Diseño no Utilizados

1. **Observer Pattern (+10):**
   - Implementar un patrón Observer para notificar cambios en el carrito podría mejorar la separación de preocupaciones y la mantenibilidad del código.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 1) = (1 + 1 + 1 + 1) + (10 + 10) + (10) = 34
\]

### Comentarios Adicionales

- **Gestión de Errores:**
  - Actualmente, el manejo de errores en las solicitudes HTTP es mínimo. Mejorar el manejo de excepciones y errores podría aumentar la robustez del código.

- **Validación de Datos:**
  - Asegurarse de que los datos se validen adecuadamente antes de realizar operaciones en el carrito y los productos para evitar inconsistencias.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de obtención de datos, manejo de productos y cálculo del total en diferentes métodos. Por ejemplo, crear métodos específicos para obtener productos y calcular el total.

2. **Uso de Patrones de Diseño:**
   - Implementar el patrón Observer para manejar cambios en el carrito y notificar al componente de manera eficiente.

3. **Mejora del Manejo de Errores:**
   - Añadir manejo de excepciones y validación de datos para todas las operaciones de lectura y escritura del carrito y productos.


## Componente Analizado: `HomeComponent`

### Descripción General

El componente `HomeComponent` maneja la vista principal de productos en la aplicación. Permite la visualización de productos, filtrados por categoría y la adición de productos a un carrito de compras.

### Identificación de Olores de Código

#### Olores de Código

1. **Funciones Grandes (+1):**
   - Los métodos `obtenerDatosVista`, `agregarProducto` y `cargarCarrito` contienen múltiples responsabilidades y lógica compleja, lo que dificulta la lectura y mantenimiento del código.

2. **Uso de Tipos `any` (+1):**
   - El uso de `any` en `productos` y otros lugares reduce la seguridad de tipos proporcionada por TypeScript, lo que puede llevar a errores difíciles de detectar.

3. **Acoplamiento Fuerte (+1):**
   - El componente depende fuertemente de los servicios `ProductoService` y `SharedService`, lo que dificulta el cambio de estos servicios o su prueba.

4. **Código Repetitivo (+1):**
   - La lógica para obtener productos por categoría se repite en múltiples lugares.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - El método `obtenerDatosVista` tiene múltiples responsabilidades: obtener productos por categoría y manejar la lógica de actualización de la vista, lo que debería estar separado en diferentes métodos.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - El componente depende directamente de la implementación de los servicios en lugar de abstracciones, lo que dificulta el cambio y la prueba de estas dependencias.

#### Patrones de Diseño no Utilizados

1. **Observer Pattern (+10):**
   - Implementar un patrón Observer para notificar cambios en el carrito podría mejorar la separación de preocupaciones y la mantenibilidad del código.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(4, 2, 1) = (1 + 1 + 1 + 1) + (10 + 10) + (10) = 34
\]

### Comentarios Adicionales

- **Manejo de Errores:**
  - Mejorar el manejo de errores para proporcionar retroalimentación más útil en caso de fallos en las solicitudes HTTP.

- **Validación de Datos:**
  - Asegurarse de que los datos se validen adecuadamente antes de realizar operaciones en el carrito y los productos para evitar inconsistencias.

### Recomendaciones de Refactorización

1. **División de Responsabilidades:**
   - Separar la lógica de obtención de datos, manejo de productos y actualización del carrito en diferentes métodos. Por ejemplo, crear métodos específicos para obtener productos y manejar la lógica del carrito.

2. **Uso de Tipos Fuertes:**
   - Utilizar tipos específicos en lugar de `any` para aprovechar las ventajas de TypeScript en la detección de errores y la documentación automática.

3. **Uso de Patrones de Diseño:**
   - Implementar el patrón Observer para manejar cambios en el carrito y notificar al componente de manera eficiente.

4. **Refactorización de Código Repetitivo:**
   - Consolidar la lógica repetitiva en métodos auxiliares para mejorar la mantenibilidad y reducir el código duplicado.




Este repositorio fue obtenido de: https://github.com/JavierEmi182/ProyectoLP-P2-G3
