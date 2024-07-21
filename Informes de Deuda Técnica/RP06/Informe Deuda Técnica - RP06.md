# Informe de Análisis de Deuda Técnica
Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

## Clase Analizada: `Partido`

### Identificación de Olores de Código

#### Acaparadores
- **Método Largo (+5)**: `cargarPartido`
- **Obsesión Primitiva (+3)**: `goles1`, `goles2`, `fecha`, `fase`, `estadio`, `ciudad`
- **Código Duplicado (+7)**: Manejo de excepciones en `cargarPartido`

#### Preventores de Cambio
- **Cambio divergente (+6)**: Gestión de datos del partido y carga de datos desde archivos

#### Dispensables
- **Código duplicado (+7)**: Manejo de excepciones en `cargarPartido`

#### Acopladores
- **Intimidad inapropiada (+6)**: Dependencia directa de la lectura de archivos en `cargarPartido`

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30)**: Gestión de datos de partidos y lectura de archivos para cargar instancias
- **Principio Abierto/Cerrado (OCP) (+40)**: Dificultad para extender sin modificar la clase
- **Principio de Inversión de Dependencias (DIP) (+45)**: Dependencia directa de la lectura de archivos

### Patrones de diseño no utilizados
- **Fábrica Abstracta (+20)**
- **Método de Fábrica (+20)**
- **Fachada (+20)**

---

## Clase Analizada: `Mundial`

### Identificación de Olores de Código

#### Acaparadores
- **Método Largo (+5)**: `generarMundial`
- **Obsesión Primitiva (+3)**: `anio`, `golesAnotados`, `nEquipos`, `nPartidos`, `nAsistentes`
- **Código Duplicado (+7)**: Manejo de excepciones en `generarMundial`

#### Preventores de Cambio
- **Cambio divergente (+6)**: Gestión de datos del mundial y lectura de archivos para generar instancias

#### Dispensables
- **Código duplicado (+7)**: Manejo de excepciones en `generarMundial`

#### Acopladores
- **Intimidad inapropiada (+6)**: Dependencia directa de la lectura de archivos en `generarMundial`

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30)**: Gestión de datos del mundial y lectura de archivos para generar instancias
- **Principio Abierto/Cerrado (OCP) (+40)**: Dificultad para extender sin modificar la clase
- **Principio de Inversión de Dependencias (DIP) (+45)**: Dependencia directa de la lectura de archivos

### Patrones de diseño no utilizados
- **Fábrica Abstracta (+20)**
- **Método de Fábrica (+20)**
- **Fachada (+20)**

---

## Clase Analizada: `Jugador`

### Identificación de Olores de Código

#### Acaparadores
- **Obsesión Primitiva (+3)**: `nombre`, `nCamiseta`, `dt`

#### Dispensables
- **Código duplicado (+7)**: Lógica de comparación en el método `equals`

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30)**: Gestión de información del jugador y comparación/representación en formato de texto
- **Principio Abierto/Cerrado (OCP) (+40)**: Dificultad para extender sin modificar la clase

### Patrones de diseño no utilizados
- **Fábrica Abstracta (+20)**
- **Método de Fábrica (+20)**
- **Fachada (+20)**

---

## Clase Analizada: `Equipo`

### Identificación de Olores de Código

#### Acaparadores
- **Método Largo (+5)**: `sumarCopas`, `cargarJugadores`
- **Obsesión Primitiva (+3)**: `pais`, `iniciales`, `copasMundiales`, `imagenEquipo`
- **Código Duplicado (+7)**: Manejo de excepciones en `sumarCopas` y `cargarJugadores`

#### Preventores de Cambio
- **Cambio divergente (+6)**: Gestión de jugadores y lectura de archivos para sumar copas y cargar jugadores

#### Dispensables
- **Código duplicado (+7)**: Manejo de excepciones en `sumarCopas` y `cargarJugadores`

#### Acopladores
- **Intimidad inapropiada (+6)**: Dependencia directa de la lectura de archivos en `sumarCopas` y `cargarJugadores`

### Violaciones de los Principios SOLID
- **Principio de Responsabilidad Única (SRP) (+30)**: Gestión de jugadores, lectura de archivos, y manipulación de datos de copas mundiales
- **Principio Abierto/Cerrado (OCP) (+40)**: Dificultad para extender sin modificar la clase
- **Principio de Inversión de Dependencias (DIP) (+45)**: Dependencia directa de la lectura de archivos

### Patrones de diseño no utilizados
- **Fábrica Abstracta (+20)**
- **Método de Fábrica (+20)**
- **Fachada (+20)**
