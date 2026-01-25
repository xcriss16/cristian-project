"""
PROYECTO CRISTIAN ALVAREZ, PRODUCTOS DE COMIDA
"""

import json
import logging

# ==========================
# configuracion del logging
# ==========================
# se guardan los eventos en un archivo llamado app.log
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Aplicación iniciada")

# array con todos los productos
productos = []


def insertar_elemento(datos):
    """
    pedir datos , los valida y los añade a la lista
    """
    print("\n--- Insertar producto ---")

    nombre = input("Nombre del producto: ").strip()
    # validacion basica
    if not nombre:
        print(" El nombre no puede estar vacío")
        logging.warning("Intento de insertar producto sin nombre")
        return

    # validamos el precio con el try catch
    try:
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("El precio debe ser un número")
        logging.error("Error al introducir el precio del producto")
        return

    # Crear producto
    producto = {"nombre": nombre, "precio": precio}

    datos.append(producto)
    guardarArchivo(datos)

    logging.info(f"Producto añadido: {nombre} - {precio}€")
    print("Producto añadido correctamente")


def buscar_elemento(datos):
    """
    buscar un producto por su nombre
    """
    print("\n--- Buscar producto ---")
    nombre = input("Nombre del producto a buscar: ").strip()

    for p in datos:
        if p["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {p}")
            logging.info(f"Producto encontrado: {nombre}")
            return p

    print("Producto no encontrado")
    logging.warning(f"Producto no encontrado al buscar: {nombre}")
    return None


def modificar_elemento(datos):
    """
    permite modificar el precio de un producto existente
    """
    print("\n--- Modificar producto ---")
    nombre = input("Nombre del producto a modificar: ").strip()

    # Buscar producto
    for p in datos:
        if p["nombre"].lower() == nombre.lower():
            print("Producto encontrado:", p)
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                p["precio"] = nuevo_precio
                guardarArchivo(datos)
                logging.info(f"Producto modificado: {nombre} nuevo precio {nuevo_precio}€")
                print("Producto modificado")
            except ValueError:
                print("Debes ingresar un número válido")
                logging.error("Error al introducir el nuevo precio")
            return

    print("Producto no encontrado")
    logging.warning(f"Intento de modificar un producto inexistente: {nombre}")


def eliminar_elemento(datos):
    """
    eliminar un producto si existe
    manejo de errores si no esta el producto en la lista
    """
    print("\n--- Eliminar producto ---")
    nombre = input("Nombre del producto a eliminar: ").strip()

    for i, p in enumerate(datos):
        if p["nombre"].lower() == nombre.lower():
            del datos[i]
            guardarArchivo(datos)
            logging.info(f"Producto eliminado: {nombre}")
            print("Producto eliminado correctamente")
            return

    print("No se encontró el producto")
    logging.warning(f"Intento de eliminar producto inexistente: {nombre}")


def mostrar_todos(datos):
    """
    Muestra todos los productos con formato.
    """
    print("\n--- Lista de productos ---")

    if not datos:
        print("No hay productos registrados")
        logging.info("Listado solicitado pero no hay productos")
        return

    for i, p in enumerate(datos, start=1):
        print(f"{i}. {p['nombre']} - €{p['precio']}")

    logging.info("Listado de productos mostrado correctamente")


# ==========================
# menu interactivo
# ==========================

def menu():
    """
    menu principal
    """
    while True:
        print(
            """
=========== TIENDA DE COMIDA ===========
1. Añadir producto
2. Buscar producto
3. Modificar producto
4. Eliminar producto
5. Mostrar todos
6. Salir
"""
        )

        opcion = input("Elige una opción: ")

        if opcion == "1":
            insertar_elemento(productos)
        elif opcion == "2":
            buscar_elemento(productos)
        elif opcion == "3":
            modificar_elemento(productos)
        elif opcion == "4":
            eliminar_elemento(productos)
        elif opcion == "5":
            mostrar_todos(productos)
        elif opcion == "6":
            print("Saliendo del programa...")
            logging.info("Aplicación cerrada por el usuario")
            break
        else:
            print("Opción inválida Intenta nuevamente.")
            logging.warning("Opción inválida introducida en el menú")


def abrirArchivo():
    # vamos a cargar nuestro json en modo lectura para cargarlo en si
    ficheroProductos = open("productos.json", "r")
    lista = json.load(ficheroProductos)
    ficheroProductos.close()
    logging.info("Archivo productos.json cargado correctamente")
    return lista


def guardarArchivo(productos):
    ficheroProductos = open("productos.json", "w")
    json.dump(productos, ficheroProductos)
    ficheroProductos.close()
    logging.info("Archivo productos.json guardado correctamente")


# solo se ejecuta si corres este archivo
if __name__ == "__main__":
    try:
        productos = abrirArchivo()
    except FileNotFoundError:
        productos = []
        logging.warning("No existe el archivo productos.json, se crea una lista vacía")

    menu()
