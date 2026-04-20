
class Carrito:
    def __init__(self):
        self.items = {}

    def agregar(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser mayor a 0")

        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def ver_carrito(self):
        total = 0

        if not self.items:
            print("Carrito vacío")
            return

        for p, c in self.items.items():
            subtotal = p.precio * c
            total += subtotal
            print(f"{p.nombre} - cantidad {c} - subtotal {subtotal}")

        print(f"Total de la compra: {total}")

    def total(self):
        return sum(p.precio * c for p, c in self.items.items())

    def vaciar(self):
        self.items.clear()

class CantidadInvalidaError(Exception):
    pass