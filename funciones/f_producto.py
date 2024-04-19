from clases.producto import Producto


def registrar_producto(productos_db: list[Producto]) -> list[Producto]:
    """ FUNCION PARA REGISTRAR UN NUEVO PRODUCTO """

    print("*** REGISTRO DE PRODUCTO NUEVO ****\n")
    salir = True
    while salir:
        producto_exists = False
        nombre = input("Nombre('exit' para salir): ").lower()
        if nombre == 'exit':
            salir = False
        elif nombre == '':
            print("el nombre no puede esta vacio")
        else:
            if len(productos_db) > 0:
                for producto in productos_db:
                    if nombre == producto.nombre:
                        producto_exists = True
                if producto_exists:
                    print("Ya existe el producto en la Base de Datos")
                else:
                    productos_db = registrar_precio(productos_db, nombre)
                    salir = False
                    input("Presione una tecla para continuar")
                    return productos_db
            else:
                productos_db = registrar_precio(productos_db, nombre)
                salir = False
                input("Presione una tecla para continuar")
                return productos_db
    return productos_db


def registrar_precio(productos_db: list[Producto], nombre: str) -> list[Producto]:
    """ FUNCION COMPLEMENTARIA PARA PRECIO A PRODUCTOS NUEVOS """

    while True:
        precio = input("Precio('exit' para salir): ")
        if precio == "":
            print("El precio no puede estar vacio")
            continue
        elif precio == 'exit':
            return productos_db
        else:
            precio = float(precio)
            print(f"\nproducto agregado 'nombre': {nombre} y 'precio': {precio}\n")
            productos_db.append(Producto(nombre, precio))
            return productos_db


def eliminar_producto(productos_db: list[Producto]) -> list[Producto]:
    """ FUNCION PARA ELIMINAR UN PRODUCTO DE LA BASE DE DATOS POR SU NOMBRE"""

    print("*** ELIMINAR PRODUCTO POR NOMBRE ****\n")
    if len(productos_db) > 0:
        salir = True
        while salir:
            producto_exists = False
            nombre = input("Nombre('exit' para salir): ").lower()
            if nombre.lower() == 'exit':
                salir = False
            else:
                for producto in productos_db:
                    if nombre == producto.nombre:
                        eliminar_producto = producto
                        producto_exists = True
                if producto_exists:
                    productos_db.remove(eliminar_producto)
                    print(f"El producto {eliminar_producto.nombre} fue eliminado")
                    input("Presione una tecla para continuar")
                    return productos_db
                else:
                    print("Producto no encontrado en la Base de Datos")
    else:
        print("No hay ningun producto en la Base de Datos")
        salir = False
    return productos_db


def ver_productos(productos_db: list[Producto]) -> None:
    """ FUNCION PARA IMPRIMIR EN PANTALLA LA LISTA COMPLETA DE PRODUCTOS """

    print("\n**** VER TODOS LOS PRODUCTOS ****\n")
    for producto in productos_db:
        print(f"producto: {producto}")
    input("\nPresione una tecla para continuar")
    return
