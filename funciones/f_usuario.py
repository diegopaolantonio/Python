from clases.usuario import Usuario


def ingresar_usuario(usuarios_db: list[Usuario]) -> Usuario | None:
    """ FUNCION PARA HACER LOGIN DE USUARIOS """

    print("*** INGRESAR CON USUARIO ****\n")
    if len(usuarios_db) > 0:
        salir = True
        while salir:
            email = input("Email('exit' para salir): ").lower()
            if email == 'exit':
                salir = False
            else:
                for usuario in usuarios_db:
                    if email == usuario.email:
                        intento = 0
                        while intento < 3:
                            password = input("Contraseña('exit' para salir): ")
                            if password == usuario.password:
                                return usuario
                            elif password == 'exit':
                                return None
                            else:
                                print("Contraseña invalida")
                                intento += 1
                        print("Exedio la cantidad de intentos")
                        input("Presione una tecla para continuar")
                print("Usuario no encontrado en la Base de Datos")
    else:
        print("No hay ningun usuario en la Base de Datos")
        salir = False
    return None


def logout_usuario() -> None:
    """ FUNCION PARA LOGOUT DE USUARIOS """

    return


def registrar_usuario(usuarios_db: list[Usuario]) -> list[Usuario]:
    """ FUNCION PARA REGISTRAR UN NUEVO USUARIO """

    print("*** REGISTRO DE USUARIO NUEVO ****\n")
    salir = True
    while salir:
        email_exists = False
        nombre = input("Nombre: ").lower()
        apellido = input("Apellido: ").lower()
        email = input("Email('exit' para salir): ").lower()
        if email == 'exit':
            salir = False
        elif email == '':
            print("el email no puede esta vacio")
        else:
            if len(usuarios_db) > 0:
                for usuario in usuarios_db:
                    if email == usuario.email:
                        email_exists = True
                if email_exists:
                    print("Ya existe el email en la Base de Datos")
                else:
                    usuarios_db = registrar_password(usuarios_db, nombre, apellido, email)
                    salir = False
                    input("Presione una tecla para continuar")
                    return usuarios_db
            else:
                usuarios_db = registrar_password(usuarios_db, nombre, apellido, email)
                salir = False
                input("Presione una tecla para continuar")
                return usuarios_db
    return usuarios_db


def registrar_password(usuarios_db: list[Usuario], nombre: str, apellido: str, email: str) -> list[Usuario]:
    """ FUNCION COMPLEMENTARIA PARA AGREGAR USUARIOS NUEVOS """

    while True:
        password = input("Contraseña('exit' para salir): ")
        if password == "":
            print("El password no puede estar vacio")
            continue
        elif password == 'exit':
            return usuarios_db
        else:
            print(f"\nusuario agregado 'nombre': {nombre}, 'apellido': {apellido}, 'email': {email} y 'password': {password}\n")
            usuarios_db.append(Usuario(nombre, apellido, email, password))
            return usuarios_db


def eliminar_usuario(usuarios_db: list[Usuario]) -> list[Usuario]:
    """ FUNCION PARA ELIMINAR UN USUARIO DE LA BASE DE DATOS POR SU EMAIL"""

    print("*** ELIMINAR USUARIO POR EMAIL ****\n")
    if len(usuarios_db) > 0:
        salir = True
        while salir:
            usuario_exists = False
            email = input("Email('exit' para salir): ").lower()
            if email.lower() == 'exit':
                salir = False
            if email.lower() == 'admin':
                print("No puede eliminar el usuario 'admin'")
            else:
                for usuario in usuarios_db:
                    if email == usuario.email:
                        eliminar_usuario = usuario
                        usuario_exists = True
                if usuario_exists:
                    usuarios_db.remove(eliminar_usuario)
                    print(f"El usuario {eliminar_usuario.email} fue eliminado")
                    input("Presione una tecla para continuar")
                    return usuarios_db
                else:
                    print("Usuario no encontrado en la Base de Datos")
    else:
        print("No hay ningun usuario en la Base de Datos")
        salir = False
    return usuarios_db


def ver_usuarios(usuarios_db: list[Usuario]) -> None:
    """ FUNCION PARA IMPRIMIR EN PANTALLA LA LISTA COMPLETA DE USUARIOS """

    print("\n**** VER TODOS LOS USUARIOS ****\n")
    for usuario in usuarios_db:
        print(f"usuario: {usuario}")
    input("\nPresione una tecla para continuar")
    return
