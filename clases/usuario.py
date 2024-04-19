class Cliente:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido


class Usuario(Cliente):
    def __init__(self, nombre: str, apellido: str, email: str, password: str) -> None:
        super().__init__(nombre, apellido)
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return f"{self.nombre} {self.email}"

    def __repr__(self) -> str:
        return f"{self.email}"

