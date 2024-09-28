 
Proyecto de aula
Entrega 1


Software Reproductor de Música


Alejandro Peña Restrepo




Algoritmos y programación orientada a objetos
Gabriel Jaime Thomas Uribe


Universidad de Medellín


03/09/2024

Tabla de contenidos
Descripción del problema	3
Análisis del problema	3
Requisitos funcionales	3
Modelo de la interfáz gráfica	4
Modelo del mundo del problema	5
Repositorio de GitHub	5














Descripción del problema
Se va a desarrollar un software en el cual se nos permita administrar múltiples canciones y de esta poder hacer playlists además de crear álbumes y escuchar música, por otra parte, podemos buscar canciones y agregarlas a las playlists.
Además, el enfoque esta para todo tipo de personas que quieran escuchar buena música con tan solo unos clics y la forma en como está constituido el software es de una manera ágil y versátil con el fin de que a los usuarios que la usen se les sea fácil y accesible a los múltiples contenidos. 

Análisis del problema
Para los requisitos funcionales se tendrá en cuenta la descripción del problema, abarcando múltiples aspectos para que el aplicativo quede completa y compacta al momento que un usuario la use. Además, se realizará la implementación de cada requerimiento funcional del reproductor de música los cuales se explicaran detalladamente a continuación.
Requisitos funcionales
[Replique las siguientes DOS tablas POR CADA REQUISITO FUNCIONAL]
Nombre	R1 Crear lista de Reproducción 
Resumen	El sistema debe permitir a los usuarios crear listas de reproducción
Entradas	•	Descripción
•	Nombre de la lista
Resultado	•	El sistema debe permitir crear listas de reproducción vacía con éxito

Pasos	Métodos	Responsabilidades
Crear lista de Reproducción	__init__(nombre, descripción)	Lista_reproduccion 
Almacenar lista de reproducción	Almacenar_lista()	Lista_reproduccion

Nombre	R2  Visualizar lista de reproducción  
Resumen	El sistema debe permitir al usuario visualizar las listas que tenga creadas 
Entradas	•	Lista de reproducción
Resultado	•	El sistema debe permitir visualizar con éxito las listas que se tengan disponibles o previamente creadas

Pasos	Métodos	Responsabilidades
Verificar que este creada la lista	Verificar_lista()->bool:	Lista_reproduccion 
Visualizar lista de reproducción	Ver_lista_reproduccion()	Lista_reproduccion 

Nombre	R3 Agregar canción a una lista de reproducción
Resumen	El sistema permite al usuario el ingreso de canciones a la playlist que se este haciendo
Entradas	•	Id canción 
•	Nombre
•	artista
Resultado	•	El sistema debe permitir el agregar canciones especificas a la lista de reproducción 

Pasos	Métodos	Responsabilidades
Verificar si la lista esta creada	Verificar_lista()->bool:	Lista_reproduccion 
Verificar que la canción no esta en la lista/ que no se repite	Verificar_cancion_lista()	Lista_reproduccion 
Agregar canción lista	Agregar_cancion(idCancion, nombre, artista)	Lista_reproduccion 

Nombre	R4 Eliminar canción de la lista
Resumen	El sistema debe permitir eliminar una canción de la lista de reproducción
Entradas	•	Id canción
•	Nombre
•	artista
Resultado	•	El sistema debe permitir eliminar canciones a la lista de reproducción 

Pasos	Métodos	Responsabilidades
Ver la lista creada	Ver_lista()	Lista
Verificar que la canción este en la lista o pertenezca a la lista 	Verificar_cancion_en_lista(idcancion)	Lista_reproduccion 
Eliminar canción de la lista	Delete_cancion_lista(idcancion)	Lista_reproduccion 

Nombre	R5 Agregar canción a cola 
Resumen	El sistema debe permitir agregar una canción a la cola de reproducción
Entradas	•	Id canción
•	Nombre
•	artista
Resultado	•	El sistema debe permitir el agregar canciones a la cola de reproducción 

Pasos	Métodos	Responsabilidades
Crear cola vacía 	Crear_cola()->list	Cola
Verificar que la canción no este en cola	Verificar_cancion_cola()->bool	Cola
Agregar canción a cola creada	Agregar_cancion_cola(idcancion,posicion)	Cola


Nombre	R6 Canciones aleatorio
Resumen	El sistema debe permitir crear un modelo aleatorio de la cola de reproducción 
Entradas	•	Id canción
Resultado	•	El sistema debe permitir la creación del modelo y reproducción aleatorio de las canciones 

Pasos	Métodos	Responsabilidades
Verificar canciones en cola almacenada	Verificar_canciones_almacenadas_cola(idcancion,posicion)	Cola
Generar modelo aleatorio de reproducción	Generar_modelo_aleatorio()	Cola


Nombre	R7 visualizar canciones de una lista de reproducción 
Resumen	El sistema debe permitir visualizar las canciones que conforman la lista de reproducción creada 
Entradas	•	Id canción
•	Nombre
•	artista
Resultado	•	El sistema debe permitir visualizar las canciones de la lista reproducción

Pasos	Métodos	Responsabilidades
Verificar que este creada la lista	Verificar_lista()->bool:	Lista_reproduccion 
Mostrar la lista	Imprimir_lista()	Lista_reproduccion 
Mostrar componentes almacenados en lista	Mostrar_canciones_lista(idcancion)	Lista_reproduccion 


Nombre	R8 visualizar cola
Resumen	El sistema debe permitir ver la cola de reproducción de acuerdo a canciones que se tengan agregadas a dicha cola 
Entradas	•	Id canción
•	Nombre
•	Artista
•	Lista cola
Resultado	•	El sistema debe permitir ver la cola que se tenga en la lista

Pasos	Métodos	Responsabilidades
Verificar que se tenga una cola creada	Verificar_cola_creada()	Cola
Verificar canciones en cola almacenada	Verificar_canciones_en _cola(idcancion,posicion)	Cola
Imprimir lista de canciones en la cola 	Ver_lista_cola(idcancion)	Cola


Nombre	R9 Reproducir cola
Resumen	El sistema debe permitir reproducir la cola que se tenga creada en la lista de reproducción
Entradas	•	Id canción
•	Nombre
•	Artista
•	Lista cola
Resultado	•	El sistema debe permitir reproducir la canción de la cola

Pasos	Métodos	Responsabilidades
El sistema debe verificar que si se tengan canciones en cola	Verificar_canciones_en _cola(idcancion,posicion)	Cola
El sistema debe generar el modelo de reproducción	Generar_modelo_aleatorio()	Cola
El sistema se va a reproducir de acuerdo al orden que tenga en el modelo 	Reproducir_cancion(idcancion,posición)	Reproductor


Nombre	R10 Reproducir orden canción
Resumen	El sistema debe permitir reproducir ya sea la siguiente o anterior canción eso lo decide el usuario cual desea escuchar
Entradas	•	Id canción
•	Nombre
•	Artista
•	Lista canción
Resultado	•	El sistema debe permitir reproducir la siguiente/ anterior canción 

Pasos	Métodos	Responsabilidades
Determinar cual es la anterior y siguiente  	Determinar_orden()	Lista, Cola
Guardar orden lista	Guardar_orden()	Lista, Cola
Reproducir antes	Reproducir_antes()	Reproductor
Reproducir después	Reproducir_despues()	Reproductor


Nombre	R11 Buscar canción 
Resumen	El sistema debe permitir encontrar una canción en el catalogo de canciones de acuerdo a su nombre 
Entradas	•	Id canción
•	Nombre
•	artista
Resultado	•	El sistema debe permitir buscar una canción en el catalogo

Pasos	Métodos	Responsabilidades
Verificar que la canción esté disponible en el catálogo de canciones	Verificar_cancion()	Catalogo_canciones
Buscar canción del catalogo	Buscar_cancion(idcancion,nombre,artista)	Catalogo_canciones


Nombre	R12 volumen música
Resumen	El sistema debe permitir manipular el volumen ya sea subirlo o bajarlo de acuerdo con el manejo que le dé el usuario
Entradas	
Resultado	•	El sistema debe permitir subir y bajar volumen 

Pasos	Métodos	Responsabilidades
Subir volumen	Volumen(subir,bajar)	Reproductor
Bajar volumen	Volumen(subir,bajar)	Reproductor

Modelo de la interfáz gráfica 
 


Modelo del mundo del problema

 

Enlace: https://drive.google.com/file/d/1ga_NEC9Pp95bDsdyWLX_8kLZpaWDItPk/view?usp=sharing
Repositorio de GitHub
alejop0927/proyecto_poo_2024 (github.com)
