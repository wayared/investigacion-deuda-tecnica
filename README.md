# Análisis de la Deuda Técnica en Repositorios de Estudiantes de Computación

Este repositorio contiene el paquete de replicación para el estudio "Evolución de la Deuda Técnica en Estudiantes de Computación de la ESPOL".

## Descripción

La investigación analiza 60 repositorios de estudiantes de la ESPOL, divididos en dos grupos: repositorios trabajados durante el nivel de educación 100 II y aquellos trabajados durante el nivel de educación 300 II. El objetivo es entender la evolución de la deuda técnica y los factores que contribuyen a su acumulación.

## Preguntas de Investigación

1. **PI1.** ¿Cuáles fueron los factores principales que contribuyeron a la acumulación de deuda técnica entre los estudiantes de computación?
2. **PI2.** ¿Existe un cambio significativo en la cantidad de deuda técnica acumulada en los repositorios de los estudiantes entre los niveles 100 II y 300 II?
3. **PI3.** ¿Cuáles son las principales fallas de diseño que los estudiantes mantienen en el periodo desde el nivel 100 II y 300 II?

## Contenido del Paquete de Replicación

Este repositorio incluye:

- **Datos**: Acceso a los repositorios de código utilizados en el estudio.
- **Herramientas**: Lista de herramientas utilizadas para el análisis automático y manual de los repositorios.
- **Scripts de Análisis**: Scripts utilizados para la evaluación de la deuda técnica.
- **Documentación**: Guía detallada para la ejecución de los análisis.

## Datos

Los repositorios analizados están listados a continuación con sus correspondientes enlaces:

| ID  | Dueño               | Nombre del Repositorio                                  | Enlace                                                                             |
|-----|---------------------|---------------------------------------------------------|------------------------------------------------------------------------------------|
| RP01| rochardp12          | proyecto                                                | [Enlace](https://github.com/rochardp12/proyecto)                                   |
| RP02| rochardp12          | ProyectoPOO-2Parcial                                    | [Enlace](https://github.com/rochardp12/ProyectoPOO-2Parcial)                       |
| RP03| anicela1030         | ProyectoPOO-2-G04                                       | [Enlace](https://github.com/anicela1030/ProyectoPOO-2-G04)                         |
| RP04| ChrisAcosta99       | ProyectoPOO2-PG-G04                                     | [Enlace](https://github.com/ChrisAcosta99/ProyectoPOO2-PG-G04)                     |
| RP05| CarlosAlvia         | ProyectoPoo2                                            | [Enlace](https://github.com/CarlosAlvia/ProyectoPoo2)                              |
| RP06| nicoletorres96      | POO-2-PG-02                                             | [Enlace](https://github.com/nicoletorres96/POO-2-PG-02)                            |
| RP07| WilmerVega          | Medical-appointment-system-for-special-children         | [Enlace](https://github.com/WilmerVega/Medical-appointment-system-for-special-children) |
| RP08| ByronB05            | ProyectoPOO2-G08                                        | [Enlace](https://github.com/ByronB05/ProyectoPOO2-G08)                             |
| RP09| JoseCandoA          | Proyecto_POO-G3                                         | [Enlace](https://github.com/JoseCandoA/Proyecto_POO_G3)                            |
| RP10| SebastianBravoo     | ProyectoSegundaParcial                                  | [Enlace](https://github.com/SebastianBravoo/ProyectoSegundaParcial)                |
| RP11| JhonatanRiveraF     | ProyectoPOO2_PG_04                                      | [Enlace](https://github.com/JhonatanRiveraF/ProyectoPOO2_PG_04)                    |
| RP12| JhonatanRiveraF     | Proyecto_POO-2-G2                                       | [Enlace](https://github.com/JhonatanRiveraF/Proyecto_POO-2-G2)                     |
| RP13| JhonatanRiveraF     | Proyecto_EDD_Grupo_9                                    | [Enlace](https://github.com/JhonatanRiveraF/Proyecto_EDD_Grupo_9)                  |
| RP14| ManuelBarrera10     | Analisador_de_Fotos_p1                                  | [Enlace](https://github.com/ManuelBarrera10/Analisador_de_Fotos_p1)                |
| RP15| JosueBarrosR        | Proyecto_EDD                                            | [Enlace](https://github.com/JosueBarrosR/Proyecto_EDD)                             |
| RP16| DerekSantander      | EDD-G3                                                  | [Enlace](https://github.com/DerekSantander/EDD-G3)                                 |
| RP17| DerekSantander      | Proyecto-2P_EDD-Grupo-3                                 | [Enlace](https://github.com/DerekSantander/Proyecto-2P_EDD-Grupo-3)                |
| RP18| RicardoVinuezaC     | Grupo_12                                                | [Enlace](https://github.com/RicardoVinuezaC/Grupo_12)                              |
| RP19| RicardoVinuezaC     | PROYECTOED2                                             | [Enlace](https://github.com/RicardoVinuezaC/PROYECTOED2)                           |
| RP20| DannyPuevo          | EDD1_PROY1P_LUNA_VIVAS_TENESAC                          | [Enlace](https://github.com/DannyPuevo/EDD1_PROY1P_LUNA_VIVAS_TENESAC)             |
| RP21| DannyPuevo          | ProyectoED2                                             | [Enlace](https://github.com/DannyPuevo/ProyectoED2)                                |
| RP22| DannyPuevo          | 2doParcialEstructuras2                                  | [Enlace](https://github.com/DannyPuevo/2doParcialEstructuras2)                     |
| RP23| DannyPuevo          | Proyecto_EDD_2P                                         | [Enlace](https://github.com/DannyPuevo/Proyecto_EDD_2P)                            |
| RP24| DannyPuevo          | Estructuras_de_datos_evaluacion_grupo_9                 | [Enlace](https://github.com/DannyPuevo/Estructuras_de_datos_evaluacion_grupo_9)    |
| RP25| DannyPuevo          | Grupo_09                                                | [Enlace](https://github.com/DannyPuevo/Grupo_09)                                   |
| RP26| lbarreto1           | lbarreto                                                | [Enlace](https://github.com/lbarreto1/lbarreto)                                    |
| RP27| lbarreto1           | Juego_reglas_BDT                                        | [Enlace](https://github.com/lbarreto1/Juego_reglas_BDT)                            |
| RP28| lbarreto1           | LI_Project--Backend                                     | [Enlace](https://github.com/lbarreto1/LI_Project--Backend)                         |
| RP29| lbarreto1           | LI-Project--Frontend                                    | [Enlace](https://github.com/lbarreto1/LI-Project--Frontend)                        |
| RP30| FaustoBinuesaF      | Analizador-proyecto                                     | [Enlace](https://github.com/FaustoBinuesaF/Analizador-proyecto)                    |
| RP31| FaustoBinuesaF      | Frontend2                                               | [Enlace](https://github.com/FaustoBinuesaF/Frontend2)                              |
| RP32| RicardoMolinoCoronel| doneFE2-Ecuador                                         | [Enlace](https://github.com/RicardoMolinoCoronel/doneFE2-Ecuador)                  |
| RP33| RicardoMolinoCoronel| FrontendL2P                                             | [Enlace](https://github.com/RicardoMolinoCoronel/FrontendL2P)                      |
| RP34| RicardoMolinoCoronel| LP2PARCIAL1                                             | [Enlace](https://github.com/RicardoMolinoCoronel/LP2PARCIAL1)                      |
| RP35| CarlosLoorB         | FrontendLP                                              | [Enlace](https://github.com/CarlosLoorB/FrontendLP)                                |
| RP36| lbarreto1           | life-angel                                              | [Enlace](https://github.com/lbarreto1/life-angel)                                  |
| RP37| lbarreto1           | comelec-ec                                              | [Enlace](https://github.com/lbarreto1/comelec-ec)                                  |
| RP38| JoseRivadeneira      | comelec-app-G3                                         | [Enlace](https://github.com/JoseRivadeneira/comelec-app-G3)                        |
| RP39| JoseRivadeneira     | SEGUNDOPROYECTO                                         | [Enlace](https://github.com/JoseRivadeneira/SEGUNDOPROYECTO)                       |
| RP40| edwardmartinez96    | DAWM_Project                                            | [Enlace](https://github.com/edwardmartinez96/DAWM_Project)                         |
| RP41| edwardmartinez96    | Dashboard-clima                                         | [Enlace](https://github.com/edwardmartinez96/Dashboard-clima)                      |
| RP42| RicardoMolinoCoronel| ProyectoDAWM                                            | [Enlace](https://github.com/RicardoMolinoCoronel/ProyectoDAWM)                     |
| RP43| RicardoMolinoCoronel| DMPA                                                    | [Enlace](https://github.com/RicardoMolinoCoronel/DMPA)                             |
| RP44| RicardoMolinoCoronel| backMPA                                                 | [Enlace](https://github.com/RicardoMolinoCoronel/backMPA)                          |
| RP45| RicardoMolinoCoronel| freshEcuador                                            | [Enlace](https://github.com/RicardoMolinoCoronel/freshEcuador)                     |
| RP46| edwardmartinez96    | Juan-Gallo_DAWM                                         | [Enlace](https://github.com/edwardmartinez96/Juan-Gallo_DAWM)                      |
| RP47| edwardmartinez96    | DAWM                                                    | [Enlace](https://github.com/edwardmartinez96/DAWM)                                 |
| RP48| edwardmartinez96    | Proyecto_DAWM-2022-1                                    | [Enlace](https://github.com/edwardmartinez96/Proyecto_DAWM-2022-1)                 |
| RP49| edwardmartinez96    | Proyecto-DAWM                                           | [Enlace](https://github.com/edwardmartinez96/Proyecto-DAWM)                        |
| RP50| edwardmartinez96    | frontE3                                                 | [Enlace](https://github.com/edwardmartinez96/frontE3)                              |
| RP51| carlosjroar17       | FrontendLP                                              | [Enlace](https://github.com/carlosjroar17/FrontendLP)                              |
| RP52| RicardoMolinoCoronel| ScrapingLuis                                            | [Enlace](https://github.com/RicardoMolinoCoronel/ScrapingLuis)                     |
| RP53| RicardoMolinoCoronel| frontP2                                                 | [Enlace](https://github.com/RicardoMolinoCoronel/frontP2)                          |
| RP54| MichaelJimenezC     | mpa                                                     | [Enlace](https://github.com/MichaelJimenezC/mpa)                                   |
| RP55| jcgallo1            | Juan-Gallo_DAWN                                         | [Enlace](https://github.com/jcgallo1/Juan-Gallo_DAWN)                              |
| RP56| dpaulsoria          | DAWM                                                    | [Enlace](https://github.com/dpaulsoria/DAWM)                                       |
| RP57| JairoAb             | Proyecto_DAWM-2022-1                                    | [Enlace](https://github.com/JairoAb/Proyecto_DAWM-2022-1)                          |
| RP58| codeswax            | Proyecto-DAWM                                           | [Enlace](https://github.com/codeswax/Proyecto-DAWM)                                |
| RP59| JEduardoRT          | P3                                                      | [Enlace](https://github.com/JEduardoRT/Portafolio/tree/main/P3)                    |
| RP60| carlosamr2          | frontFinal                                              | [Enlace](https://github.com/carlosamr2/frontFinal)                                 |
| RP61| luisenjs            | ScrapingLuis                                            | [Enlace](https://github.com/luisenjs/AnalisisDatos/tree/ScrapingLuis)              |

## Herramientas Utilizadas

- **Lint**: Herramienta de revisión de código para detectar patrones comunes de deuda técnica.
- **SonarQube**: Plataforma para análisis de calidad del código.

## Scripts de Análisis

Los scripts utilizados para el análisis están incluidos en la carpeta scripts y se pueden ejecutar siguiendo las instrucciones detalladas en la documentación.

## Documentación

Para replicar el estudio, sigue los pasos descritos en la documentación incluida en la carpeta docs. Esto incluye la configuración de las herramientas, ejecución de los scripts y análisis de los resultados.

