# CarDensityAI: Detección y recuento de coches a partir de imágenes aéreas

Este repositorio tiene como objetivo la implementación de un método de detección automática de vehículos en imágenes aéreas de alta resolución. El proyecto se desarrolla en el marco de la asignatura __Aplicaciones Industriales y Comerciales__  incluída en el [Máster Universitario en Visión Artificial](https://mastervisionartificial.es) impartido en la Universidad Rey Juan Carlos.

En la pestaña principa del repositorio se encuentra:

- `Documentation`: una carpeta cuya intención es recoger los documentos preparados durante el desarrollo del sistema. Esta documentación será la presentada al cliente. Incluye ficheros como el documento de requisitos del sistema, el presupuesto o el documento de diseño.

- 'WebApplication`: un directorio intencionado para recoger todos los ficheros para el desarrollo de la Web planteada.

- 'development': directorio en el que se guarda el código fuente de la aplicación así como los tests unitarios contra los que se prueban.

Se encuentra, además, este fichero `README.md` en formato markdown así como un fichero de requerimientos (`requirements.txt`) en el que se recogen los requisitos de spftware necesarios para ejecutar el código desde un interprete. 


El proyecto será desarrollado por:

- [Blanca Rodríguez González](https://github.com/brodgon)
- [Francisco C. Vázquez Donaire](https://github.com/xFranv8)

Última Edición: 30/03/2023

> **Importante**: El proyecto no está finalizado. En esta versión, el repositorio incluye una versión de juguete de lo que será el sistema final. Este fichero README.md se irá actualizando conforme se vaya desarrollando y optimizando la tarea. El fichero recoge una estructura preliminar de lo que será su versión final. 

## Descripción del proyecto

Con el fin de estimar la densidad de tráfico en diferentes núcleos urbanos, se plantea la implementación de un sistema de visión artificial capaz de realizar un recuento (y detección) automático de coches a partir de imágenes aéreas. Con este propósito, se implementará una red YOLO que analizará las imágenes y devolverá las coordenadas del "bounding box" en el que se encuentra cada coche. Esto se recogerá en un modulo diseñado para integrarse en las estaciones de trabajo del cliente, lo que permitirá realizar estudios de forma más rápida.

## El sistema desarrollado

Se diseña un algoritmo capaz de detectar vehículos en una imagen áerea de grandes dimensiones bajo el paradigma de **Programación Orientada a Objetos (POO)**. Partiendo de esta idea, se diseñan diferentes clases recogiendo los pasos necesarios para completar nuestros objetivos. Precisamente, se implementan seis clases, presentadas a continuación en orden alfabético:

- `BoundingBox`: clase contenedora de la estructura de las bounding box que reogen las detecciones de los vehículos.
- `CarDensityAI`: clase principal del sistema. Esta clase se apoya en el resto de clases diseñadas durante el desarollo. Actúa a su vez como programa principal.
- `Detector`: Clase recogiendo el proceso de la detección completo. Tras un parcheado de las imágenes, se llama a una clase externa contenedora del mdoelo de red YOLO preentrenado. Con ella, se hace inferencia sobre cada uno de los parches generados y se estructuran las coordenadas detectadas al tipo BoundingBox. Se devolverá, por tanto, una lista de coordenadas de todos los behículos detectados.
- `ImagePatcher`: clase diseñada para la división de la imagen original en parches de menor tamaño.
- `Reader`: clase diseñada para la correcta carga de las imágenes a partir de una ruta de entrada.
- `ResultViewer`: clase contentedora de métodos para la correcta visualización de los resultados del análisis. Se diseñan diferentes métodos que devolverán la imagen original con las detecciones dibujadas, así como un csv con la información pertinente (número de coches y coordenadas de las detecciones).

Sobre cada uno de los métodos diseñados, se implementan una serie de tests unitarios contra los que se prueban los métodos.


## Puesta en marcha del Sistema

A fecha de la última edición del proyecto, el proyecto se podrá usar por terceros simplemente clonando el repositorio e instalando los requisitos del sistema.

## Instrucciones de Uso

A fecha de la última edición del proyecto, el sistema se ejecuta desde un interprete Python.



