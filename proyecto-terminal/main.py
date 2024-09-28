from logica_completa import Lista_reproduccion
from creacion_canciones import Cancion

def mostrar_menu():
    print("\n--- Menú del programa ---")
    print("1. Crear una lista de reproduccion")
    print("2. Ver lista de reproduccion")
    print("3. Buscar Canción por Nombre")
    print("4. Salir")

def main():
    listas = {}  # Diccionario para almacenar las listas de reproducción

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la lista de reproduccion: ")
            descripcion = input("Ingrese la descripcion de la lista de reproduccion: ")
            # Crear una nueva instancia de Lista_reproduccion
            nueva_lista = Lista_reproduccion(descripcion, nombre)
            # Llamar al método crear_lista en la instancia
            if nueva_lista.crear_lista(nombre, descripcion):
                listas[nombre] = nueva_lista  # Guardar la lista en el diccionario
                print("Lista creada exitosamente.")
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la lista de reproduccion a ver: ")
            if nombre in listas:
                listas[nombre].ver_lista_reproduccion()  # Llamar al método de la lista específica
            else:
                print("No se encontró la lista de reproducción con ese nombre.")
        
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la canción a buscar: ")
            Cancion.buscar_cancion(nombre)  # Este método debería estar implementado
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
