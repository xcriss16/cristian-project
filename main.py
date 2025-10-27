## creamos la clase productos
class producto:

    ## vamos a definir los atributos de mis productos
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock  

        ## creamos una manzana que tenga de precio 1.5 y que hayan 10 en stock
        mi_producto1 =  ("Manzana",1.5,10)
        # vamos a mostrar algunas de las caracteristicas de mi producto creado
        print(mi_producto1.nombre)
        print(mi_producto1.precio)
        print(mi_producto1.stock)