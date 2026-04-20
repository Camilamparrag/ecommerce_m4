
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Admin(Usuario):
    def menu_admin(self):
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")

class Cliente(Usuario):
    def menu_cliente(self):
        print("1. Ver catálogo")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Comprar")