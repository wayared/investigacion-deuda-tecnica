# Informe de Análisis de Código TypeScript (Angular)

## Archivo Analizado: `datos.component.ts`

### Descripción General

El archivo `datos.component.ts` pertenece a un componente Angular que se encarga de mostrar y filtrar una lista de juegos y categorías. Utiliza servicios para obtener los datos y ofrece funcionalidades de filtrado por nombre y plataforma.

### Identificación de Olores de Código

#### Olores de Código

1. **Funciones Grandes (+1):**
   - Las funciones `filtrarPorNombre` y `filtrarPlataformas` contienen múltiples responsabilidades y podrían ser divididas en funciones más pequeñas y manejables.

2. **Manejo Directo del DOM (+1):**
   - Se utilizan métodos como `document.getElementsByClassName` y `document.querySelector`, lo cual no es recomendado en Angular ya que se debe utilizar el enlace de datos y las directivas de Angular para manipular el DOM.

3. **Duplicación de Código (+1):**
   - La lógica de filtrado en `filtrarPorNombre` y `filtrarPlataformas` contiene estructuras repetitivas que podrían ser abstraídas en una función común.

4. **Nombres de Funciones y Variables no Descriptivos (+1):**
   - Los nombres de algunas variables y funciones, como `loadPlatform` y `loadNameSelector`, no describen claramente su propósito y podrían ser renombrados para mejorar la legibilidad.

5. **Uso Extensivo de `any` y Tipos Implícitos (+1):**
   - El uso del tipo `any` y la falta de tipado explícito en algunas variables y funciones reduce la robustez y la autocompletación proporcionada por TypeScript.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - Las funciones `ngOnInit`, `filtrarPorNombre` y `filtrarPlataformas` tienen múltiples responsabilidades, incluyendo la manipulación del DOM, la lógica de filtrado y la suscripción a servicios, lo cual debería estar separado en diferentes métodos.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La lógica de filtrado depende directamente de la estructura del DOM, lo que dificulta el testeo y la reutilización del código.

#### Patrones de Diseño no Utilizados

1. **Componente Presentacional y Contenedor (+10):**
   - Separar la lógica de presentación de la lógica de negocio podría mejorar la organización y la reutilización del código.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(5, 2, 1) = (1 + 1 + 1 + 1 + 1) + (10 + 10) + (10) = 35
\]

### Comentarios Adicionales

- **Uso de Enlace de Datos Angular:**
  - Utilizar el enlace de datos de Angular y las directivas para manejar el DOM en lugar de manipularlo directamente con `document`.

- **Separación de Funciones:**
  - Dividir las funciones grandes en funciones más pequeñas y manejables que tengan una única responsabilidad.

- **Mejorar Tipado:**
  - Aprovechar las capacidades de tipado de TypeScript para definir tipos específicos en lugar de utilizar `any`.

### Recomendaciones de Refactorización

1. **Uso de Directivas Angular:**
   - Utilizar directivas como `ngFor` y `ngIf` para manejar la lógica de filtrado en la plantilla HTML en lugar de manipular el DOM directamente.

2. **Funcionalidad de Filtrado:**
   - Extraer la lógica de filtrado a métodos de utilidad separados que puedan ser reutilizados y testeados de manera independiente.

3. **Refactorización del Ciclo de Vida:**
   - Simplificar el método `ngOnInit` para que sólo contenga la lógica necesaria para inicializar el componente y delegar otras responsabilidades a métodos auxiliares.

## Archivo Analizado: `custom.js`

### Descripción General

El archivo `custom.js` contiene una serie de scripts para manejar la interacción de la página web. Incluye animaciones, manejo de eventos, inicialización de componentes y otras funcionalidades para mejorar la experiencia del usuario.

### Identificación de Olores de Código

#### Olores de Código

1. **Funciones Grandes (+1):**
   - Las funciones anónimas y eventos contienen múltiples responsabilidades que podrían dividirse en funciones más pequeñas y manejables.

2. **Manipulación Directa del DOM (+1):**
   - El archivo contiene múltiples manipulaciones directas del DOM usando jQuery, lo cual puede dificultar el mantenimiento y prueba del código.

3. **Código Repetido (+1):**
   - Existen patrones repetidos en la manipulación de elementos del DOM y la configuración de eventos, lo cual puede ser abstraído para evitar redundancia.

4. **Nombres de Variables no Descriptivos (+1):**
   - Algunas variables y funciones no tienen nombres descriptivos, lo que dificulta la comprensión del código.

5. **Uso Extensivo de Literales Mágicos (+1):**
   - El uso de valores literales directamente en el código, como tiempos de animación y nombres de clases, dificulta la modificación y comprensión del código.

#### Principios SOLID Violados

1. **Principio de Responsabilidad Única (SRP) (+10):**
   - Las funciones contienen múltiples responsabilidades como la inicialización de componentes, el manejo de eventos y la manipulación del DOM.

2. **Principio de Inversión de Dependencias (DIP) (+10):**
   - La lógica de la aplicación depende directamente de la estructura del DOM, lo que dificulta la prueba y reutilización del código.

#### Patrones de Diseño no Utilizados

1. **Patrón de Módulo (+10):**
   - La utilización de un patrón de módulo podría encapsular las funcionalidades y mejorar la organización del código.

### Cálculo del Esfuerzo de Refactorización

\[
E(o, s, p) = E(5, 2, 1) = (1 + 1 + 1 + 1 + 1) + (10 + 10) + (10) = 35
\]

### Comentarios Adicionales

- **Modularización del Código:**
  - Dividir el código en módulos más pequeños y encapsulados puede mejorar la legibilidad y mantenibilidad del código.

- **Uso de Variables Constantes:**
  - Reemplazar literales mágicos con constantes bien nombradas puede hacer que el código sea más fácil de entender y mantener.

- **Refactorización de Eventos:**
  - Crear funciones separadas para manejar eventos específicos en lugar de manejar todos los eventos en una sola función.

### Recomendaciones de Refactorización

1. **División de Funciones:**
   - Separar la lógica de inicialización de componentes, manejo de eventos y manipulación del DOM en funciones independientes.

2. **Abstracción de Manipulaciones del DOM:**
   - Crear funciones auxiliares para manipular el DOM en lugar de hacerlo directamente dentro de los eventos.

3. **Utilización de Constantes:**
   - Definir constantes para valores usados repetidamente, como tiempos de animación, nombres de clases, y selectores.

4. **Adopción del Patrón de Módulo:**
   - Encapsular la lógica en módulos que puedan ser fácilmente importados y reutilizados en diferentes partes de la aplicación.

Informe de Análisis de Código JavaScript

## Archivo Analizado: owl.carousel.js

### Descripción General
El archivo owl.carousel.js es un script de jQuery que implementa la funcionalidad de un carrusel conocido como Owl Carousel. Este carrusel permite la creación de slides con varias características como navegación, reproducción automática, carga diferida de imágenes y soporte de videos.

### Identificación de Olores de Código
Olores de Código
Funciones Grandes (+1):

Las funciones contienen múltiples responsabilidades y tareas complejas que podrían dividirse en funciones más pequeñas y manejables. Ejemplo: Owl.prototype.initialize.
Manipulación Directa del DOM (+1):

El archivo contiene múltiples manipulaciones directas del DOM usando jQuery, lo cual puede dificultar el mantenimiento y prueba del código.
Código Repetido (+1):

Existen patrones repetidos en la manipulación de elementos del DOM y la configuración de eventos, lo cual puede ser abstraído para evitar redundancia.
Nombres de Variables no Descriptivos (+1):

Algunas variables y funciones no tienen nombres descriptivos, lo que dificulta la comprensión del código. Ejemplo: var i, j, k en Navigation.prototype.update.
Uso Extensivo de Literales Mágicos (+1):

El uso de valores literales directamente en el código, como tiempos de animación y nombres de clases, dificulta la modificación y comprensión del código.
Principios SOLID Violados
Principio de Responsabilidad Única (SRP) (+10):

Las funciones contienen múltiples responsabilidades como la inicialización de componentes, el manejo de eventos y la manipulación del DOM. Ejemplo: Owl.prototype.setup.
Principio de Inversión de Dependencias (DIP) (+10):

La lógica de la aplicación depende directamente de la estructura del DOM, lo que dificulta la prueba y reutilización del código.
Patrones de Diseño no Utilizados
Patrón de Módulo (+10):
La utilización de un patrón de módulo podría encapsular las funcionalidades y mejorar la organización del código.
Cálculo del Esfuerzo de Refactorización

E(o,s,p)=E(5,2,1)=(1+1+1+1+1)+(10+10)+(10)=35

### Comentarios Adicionales
Modularización del Código:

Dividir el código en módulos más pequeños y encapsulados puede mejorar la legibilidad y mantenibilidad del código.
Uso de Variables Constantes:

Reemplazar literales mágicos con constantes bien nombradas puede hacer que el código sea más fácil de entender y mantener.
Refactorización de Eventos:

Crear funciones separadas para manejar eventos específicos en lugar de manejar todos los eventos en una sola función.
Recomendaciones de Refactorización
División de Funciones:

Separar la lógica de inicialización de componentes, manejo de eventos y manipulación del DOM en funciones independientes.
Abstracción de Manipulaciones del DOM:

Crear funciones auxiliares para manipular el DOM en lugar de hacerlo directamente dentro de los eventos.
Utilización de Constantes:

Definir constantes para valores usados repetidamente, como tiempos de animación, nombres de clases, y selectores.
Adopción del Patrón de Módulo:

Encapsular la lógica en módulos que puedan ser fácilmente importados y reutilizados en diferentes partes de la aplicación.

Este repositorio fue obtenido de: https://github.com/AxcelVillagran/mpa
