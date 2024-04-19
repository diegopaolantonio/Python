class Cliente:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre


class Usuario(Cliente):
    def __init__(self, nombre: str, email: str, password: str) -> None:
        super().__init__(nombre)
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return f"{self.nombre} {self.email}"

    def __repr__(self) -> str:
        return f"{self.email}"

