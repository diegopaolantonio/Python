from clases.usuario import Usuario
from clases.producto import Producto
from clases.ventas import Ventas
from .f_producto import ver_productos

def realizar_compra(usuario_logeado: Usuario | None, productos_db: list[Producto]) -> None:
    comprar_producto: Producto | None = None
    salir = True

    if usuario_logeado:
        while salir:
            nueva_compra = None
            comprar_producto = None
            ver_productos(productos_db)
            producto_nombre = input("Ingrese el nombre del producto a comprar('exit' para salir): ")
            if producto_nombre != 'exit':
                for producto in productos_db:
                    if producto_nombre == producto.nombre:
                        comprar_producto = producto
                if comprar_producto:
                    Ventas(usuario_logeado, comprar_producto)
                else:
                    print("Producto no encontrado")
            else:
                salir = False
        return
    else:
        print("No hay ningun usuario logueado para realizar la compra")
        return


def ver_compras():
    """ FUNCION PARA IMPRIMIR EN PANTALLA LA LISTA COMPLETA DE VENTAS """

    print("\n**** VER TODOS LAS VENTAS ****\n")
    for venta in Ventas.list_ventas:
        print(f"venta: {venta["id"]} - {venta["usuario"]} - {venta["producto"]}")
    input("\nPresione una tecla para continuar")
    return