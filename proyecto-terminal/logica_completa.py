from creacion_canciones import Cancion

class Lista_reproduccion(Cancion):
     descripcion:str
     nombre_lista:str
     def __init__(self,descripcion,nombre_lista):
          self.descripcion=descripcion
          self.nombre_lista=nombre_lista
          self.lista_reproduccion_canciones={}
        
     def crear_lista(self, nombre, descripcion):
          if nombre in self.lista_reproduccion_canciones:
               print(f"la lista '{nombre}' ya existe.")
               return False
          else:
           self.lista_reproduccion_canciones[nombre]=Lista_reproduccion(nombre,descripcion)
           print(f"Lista '{nombre}' creada exitosamente.")
           return True
     
     def _verificar_lista_creada(self):
          if not self.lista_canciones:
            print("no se tienen ninguna lista anteriormente")
            self.crear_lista()
            return False
          return True 
            
     def ver_lista_reproduccion(self):
         if len(self.lista_reproduccion_canciones) == 0:
            self._verificar_lista_creada()
            return False
         elif len(self.lista_reproduccion_canciones) == 1:
             print(f"la lista de reproduccion es {list(self.lista_reproduccion_canciones.items())[0]}")
         else:
             print(f"las listas de reproduccion que hay son {list(self.lista_reproduccion_canciones.items())}")
#verifica cancion repetida
     def _verificar_cancion_lista(self, nombre_lista, cancion):
       if  nombre_lista in self.lista_reproduccion_canciones:
           if 'canciones' in self.lista_reproduccion_canciones[nombre_lista]:
               for c in self.lista_reproduccion_canciones[nombre_lista]['canciones']:
                   if c.nombre_cancion == cancion.nombre_cancion and c.nombre_autor == cancion.nombre_autor:
                   
              
               
          
          
        