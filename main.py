from clases.producto import Producto
from clases.catalogo import Catalogo, ProductoNoEncontradoError
from clases.carrito import Carrito, CantidadInvalidaError
from clases.usuario import Admin, Cliente
from datetime import datetime


def menu_admin(catalogo):
    while True:
        print("\n--- MENU ADMIN ---")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Guardar catálogo")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            catalogo.listar_catalogo()

        elif opcion == "2":
            try:
                id = int(input("ID: "))
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))

                producto = Producto(id, nombre, categoria, precio)
                catalogo.agregar_producto(producto)

            except ValueError:
                print("Error: datos inválidos")

        elif opcion == "3":
            try:
                id = int(input("ID a eliminar: "))
                catalogo.eliminar_producto(id)
            except Exception as e:
                print(e)

        elif opcion == "4":
            catalogo.guardar_catalogo()
            print("Catálogo guardado")

        elif opcion == "5":
            break

        else:
            print("Opción inválida")


def guardar_orden(carrito):
    try:
        with open("ordenes.txt", "a") as f:
            f.write("===== NUEVA ORDEN =====\n")
            f.write(f"Fecha: {datetime.now()}\n")

            total = 0
            for p, c in carrito.items.items():
                subtotal = p.precio * c
                total += subtotal
                f.write(f"Producto: {p.nombre} | Cantidad: {c} | Subtotal: {subtotal}\n")

            f.write(f"TOTAL: {total}\n")
            f.write("========================\n\n")

    except Exception as e:
        print(f"Error al guardar la orden: {e}")

def menu_cliente(catalogo, carrito):
    while True:
        print("\n--- MENU CLIENTE ---")
        print("1. Ver catálogo")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Confirmar compra")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            catalogo.listar_catalogo()

        elif opcion == "2":
            try:
                id = int(input("ID producto: "))
                cantidad = int(input("Cantidad: "))

                producto = catalogo.buscar_por_id(id)
                if not producto:
                    raise ProductoNoEncontradoError("Producto no existe")

                carrito.agregar(producto, cantidad)

            except (ValueError, CantidadInvalidaError) as e:
                print(f"Error: {e}")
            except ProductoNoEncontradoError as e:
                print(e)

        elif opcion == "3":
            carrito.ver_carrito()

        elif opcion == "4":
            if not carrito.items:
                print("Carrito vacío, no se puede comprar")
            else:
                guardar_orden(carrito)
                print("Compra realizada con éxito")
                carrito.vaciar()

        elif opcion == "5":
            break

        else:
            print("Opción inválida")


def main():
    catalogo = Catalogo()
    carrito = Carrito()

    # Productos iniciales
    catalogo.agregar_producto(Producto(1, "Reloj", "Accesorio", 25000))
    catalogo.agregar_producto(Producto(2, "Corbata", "Accesorio", 12000))
    catalogo.agregar_producto(Producto(3, "Camisa", "Ropa", 10000))
    catalogo.agregar_producto(Producto(4, "Pantalon", "Ropa", 12000))
    catalogo.agregar_producto(Producto(5, "Pulsera", "Accesorio", 10000))
    catalogo.agregar_producto(Producto(6, "Zapatillas", "Calzado", 35000))

    print("=== BIENVENIDO AL ECOMMERCE ===")
    print("1. Admin")
    print("2. Cliente")

    opcion = input("Seleccione rol: ")

    if opcion == "1":
        admin = Admin("admin")
        menu_admin(catalogo)

    elif opcion == "2":
        cliente = Cliente("cliente")
        menu_cliente(catalogo, carrito)

    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()