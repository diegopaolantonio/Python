class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f"{self.nombre}: ${self.precio}"
    
    def __repr__(self) -> str:
        return f"{self.nombre}: ${self.precio}"

