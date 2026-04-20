
class Producto:
    def __init__(self, id, nombre, categoria, precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre}  - {self.categoria} - {self.precio}"


