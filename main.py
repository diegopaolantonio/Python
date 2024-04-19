""" SEGUNDA PREENTREGA PYTHON - PAOLANTONIO DIEGO - SISTEMA PARA REGISTRO Y LOGIN DE USUARIOS, REGISTRAR PRODUCTOS """

from clases.usuario import Usuario
from clases.producto import Producto

import funciones.f_usuario as funciones_usuario
import funciones.f_producto as funciones_producto
import funciones.f_compra as funciones_compra


def main() -> None:
    """ FUNCION MAIN """

    # Lista de usuarios, productos y ventas, hay un usuario admin, que no se puede eliminar y es el unico que puede
    # crear, borrar y ver la lista de base de datos

    usuarios_db: list[Usuario] = [Usuario('admin', 'admin', 'admin', 'admin')]
    productos_db: list[Producto] = []

    usuario_logeado: Usuario | None = None;

    while True:
        print("\n**** SISTEMA DE LOGIN Y RESGITRO DE USUSARIOS: ****\n")
        if usuario_logeado != None:
            print(f"BIENVENIDO {usuario_logeado.email}\n")
        else:
            print("NINGUN USUARIO LOGEADO\n")
        if usuario_logeado == None:
            print("1 - Login")
        if usuario_logeado != None:
            print("2 - Logout")
            if usuario_logeado.email == 'admin':
                print("3 - Registrar nuevo usuario")
                print("4 - Borrar usuario")
                print("5 - Ver lista completa de usuarios")
                print("6 - Registrar nuevo producto")
                print("7 - Borrar producto")
                print("8 - Ver lista completa de productos")
            print("9 - Realizar compra")
            if usuario_logeado.email == 'admin':
                print("10 - Ver lista completa de ventas")
        print("11 - Salir de sistema")

        opcion = input("\nIngrese opcion: ")

        if opcion == "1":
            usuario_logeado = funciones_usuario.ingresar_usuario(usuarios_db)
        elif opcion == "2":
            usuario_logeado = funciones_usuario.logout_usuario()
        elif opcion == "3":
            usuarios_db = funciones_usuario.registrar_usuario(usuarios_db)
        elif opcion == "4":
            usuarios_db = funciones_usuario.eliminar_usuario(usuarios_db)
        elif opcion == "5":
            funciones_usuario.ver_usuarios(usuarios_db)
        elif opcion == "6":
            productos_db = funciones_producto.registrar_producto(productos_db)
        elif opcion == "7":
            productos_db = funciones_producto.eliminar_producto(productos_db)
        elif opcion == "8":
            funciones_producto.ver_productos(productos_db)
        elif opcion == "9":
             funciones_compra.realizar_compra(usuario_logeado, productos_db)
        elif opcion == "10":
            funciones_compra.ver_compras()
        elif opcion == "11":
            usuario_logeado = funciones_usuario.logout_usuario()
            break


main()

