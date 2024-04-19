from clases.usuario import Usuario
from clases.producto import Producto
from clases.ventas import Ventas


def realizar_compra(ventas_db: list[Ventas], usuario_logeado: Usuario | None, productos_db: list[Producto]) -> list[Ventas]:
    
    return ventas_db