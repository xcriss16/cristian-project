def main():
    
    datos = []
    

    # asociamos cada eleccion con una funcion de las creadas
    
    while True:

        eleccion = menu()
        
        if eleccion == '1':
            insertar_elemento(datos)
        
        elif eleccion == '2':
           buscar_elemento(datos)
        elif eleccion == '3':
            modificar_elemento(datos)
        elif eleccion == '4':
            eliminar_datos(datos)
        elif eleccion == '5':
            mostrar_datos(datos)
        else :
            break;
        
        
        


        
        

            

    
    
def insertar_elementos(datos):

    while True:
        id_producto = int(input("Ingrese el ID del producto (o 'salir' para terminar): ")).strip()
        
        ## comprobamos si es salir para salir del bucle
        if id_producto.lower() == 'salir':
            break

        try: 
            id_producto = int(id_producto)
        
        except ValueError:
            print("Debe ingresar un numero válido o salir para salir")

        continue


        
        
        nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ").strip()
        if nombre.lower() == 'salir' :
                break

        




def menu():
    print("=== Menú Principal ===")
    print("1. Añadir elemento")
    print("2. Buscar elemento")
    print("3. Modificar elemento")
    print("4. Eliminar elemento")
    print("5. Mostrar todos")
    print("6. Salir")
    
    eleccion = input("Seleccione una opción: ")
    return eleccion


def mostrar_mensaje_salida():
    print("Gracias por usar el programa. ¡Hasta luego!")

            
def buscar_elemento(datos):
    print("Hola")


def modificar_elemento(datos):
    print("Hola")

def eliminar_elemento(datos):
    print("Hola")

def mostrar_todos(datos):
    print("Hola")
    
    


