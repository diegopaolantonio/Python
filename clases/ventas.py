from .usuario import Usuario
from .producto import Producto

class Ventas:
    id_venta: int = 0
    list_ventas: list[dict] = []
    
    def __init__(self, usuario: Usuario, producto: Producto) -> None:
        self.usuario = usuario
        self.producto = producto
        self.compra()

    def compra(self):
        Ventas.id_venta += 1
        nueva_compra = {
            "id": Ventas.id_venta,
            "usuario": self.usuario,
            "producto": self.producto,
        }
