from clases.producto import Producto

class Catalogo:
    def __init__(self):
        self.productos = []

    def __str__(self):
        return f"{self.productos}"

    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def listar_catalogo(self):
        for producto in self.productos:
           print(producto) 

    def buscar_por_id(self, id):
        for p in self.productos: #[producto1, producto2 ,producto 3, ...]
            if p.id == id:
                return p


    def eliminar_producto(self, id):
        p = self.buscar_por_id(id)
        self.productos.remove(p)


    def guardar_catalogo(self, nombre_archivo = "catalogo.txt"):
        try:
            with open(nombre_archivo, "w") as f:
                for p in self.productos:
                    f.write(f"{p.id}, {p.nombre}, {p.categoria}, {p.precio}")

        except Exception as e:
            print(f"error en el archivo : {e}")

class ProductoNoEncontradoError(Exception):
    pass