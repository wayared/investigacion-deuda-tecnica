# Informe de Análisis de Deuda Técnica

## Malos olores de código, Patrones de Diseño no usados y Principios SOLID violados

### Clase Analizada: `Cliente`

#### Identificación de Olores de Código

**Acaparadores**

- Método Largo (+5):
  - `reservarHospedaje`
  - `reservarTransporte`
  - `reservarEntretenimiento`
- Clase Grande (+6): 
  - La clase `Cliente` maneja múltiples responsabilidades.
- Obsesión Primitiva (+3):
  - Uso de tipos primitivos para `fecha`, `fechaEntrada`, `fechaSalida`.
- Código duplicado (+7):
  - Lógica de validación de fechas repetida.

**Abusadores de Orientación a Objetos**

- Sentencias Switch (+5):
  - Uso de `switch` en `reservarHospedaje`.
- Intimidad inapropiada (+6):
  - La clase `Cliente` accede directamente a los archivos del sistema mediante la clase `Funcion`.

**Preventores de Cambio**

- Cambio divergente (+6):
  - La clase maneja varias responsabilidades, lo que dificulta los cambios sin afectar otras funcionalidades.

**Dispensables**

- Comentarios (+2):
  - Comentarios excesivos que describen el funcionamiento del código en lugar de su propósito.

**Acopladores**

- Envidia de características (+5):
  - Métodos que realizan demasiadas tareas.
- Cadenas de mensajes (+7):
  - Métodos que llaman a otros métodos en secuencia.

#### Violaciones de los Principios SOLID

- Principio de Responsabilidad Única (SRP) (+30)
- Principio Abierto/Cerrado (OCP) (+40)
- Principio de Inversión de Dependencias (DIP) (+45)

#### Patrones de diseño no utilizados

**Creacionales**
- Constructor (+25)
- Método de Fábrica (+20)

**Estructurales**
- Adaptador (+25)
- Compuesto (+30)

**De comportamiento**
- Estrategia (+20)
- Método Plantilla (+25)

---

### Clase Analizada: `Pago`

#### Identificación de Olores de Código

**Acaparadores**

- Obsesión Primitiva (+3):
  - Uso de tipos primitivos para `fechaDePago`, `fechaCaducidad`, `numeroMetodoPago`.
- Clase Grande (+6): 
  - La clase `Pago` tiene responsabilidades que podrían delegarse.

**Preventores de Cambio**

- Cambio divergente (+6):
  - La clase maneja la generación de identificadores y representación en texto.

**Acopladores**

- Intimidad inapropiada (+6):
  - Dependencia directa de la clase `Funcion` para la generación de identificadores.

#### Violaciones de los Principios SOLID

- Principio de Responsabilidad Única (SRP) (+30)
- Principio Abierto/Cerrado (OCP) (+40)
- Principio de Inversión de Dependencias (DIP) (+45)

#### Patrones de diseño no utilizados

**Creacionales**
- Método de Fábrica (+20)

**Estructurales**
- Adaptador (+25)

**De comportamiento**
- Estrategia (+20)

---

### Clase Analizada: `Reserva`

#### Identificación de Olores de Código

**Acaparadores**

- Clase Grande (+6):
  - La clase `Reserva` maneja la generación de números de reserva y representación en texto.
- Obsesión Primitiva (+3):
  - Uso de tipos primitivos para `fechaReserva`, `desde`, `hasta`.

**Preventores de Cambio**

- Cambio divergente (+6):
  - La clase maneja varias responsabilidades que podrían dividirse.

**Acopladores**

- Intimidad inapropiada (+6):
  - Dependencia directa de la clase `Funcion` para la generación de números de reserva.

#### Violaciones de los Principios SOLID

- Principio de Responsabilidad Única (SRP) (+30)
- Principio Abierto/Cerrado (OCP) (+40)
- Principio de Inversión de Dependencias (DIP) (+45)

#### Patrones de diseño no utilizados

**Creacionales**
- Método de Fábrica (+20)

**Estructurales**
- Adaptador (+25)

**De comportamiento**
- Estrategia (+20)

---

### Clase Analizada: `Hospedaje`

#### Identificación de Olores de Código

**Acaparadores**

- Clase Grande (+6):
  - La clase `Hospedaje` maneja tanto hoteles como departamentos.
- Obsesión Primitiva (+3):
  - Uso de tipos primitivos para `fechaEntrada`, `fechaSalida`, `precioH`.

**Dispensables**

- Código duplicado (+7):
  - Métodos `mostrarReserva` y `mostrarReservaDe` tienen código similar.

**Acopladores**

- Intimidad inapropiada (+6):
  - Dependencia directa de clases de bajo nivel.

#### Violaciones de los Principios SOLID

- Principio de Responsabilidad Única (SRP) (+30)
- Principio Abierto/Cerrado (OCP) (+40)

#### Patrones de diseño no utilizados

**Creacionales**
- Método de Fábrica (+20)

**Estructurales**
- Compuesto (+30)

**De comportamiento**
- Estrategia (+20)
- Método Plantilla (+25)
