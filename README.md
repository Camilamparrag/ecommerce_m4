## Descripción breve de la app

La aplicación es un **Ecommerce por consola desarrollado en Python** utilizando Programación Orientada a Objetos (POO).  
Permite interactuar con dos tipos de usuarios:

- **ADMIN**:
  - Gestiona el catálogo de productos (crear, listar, eliminar y guardar en archivo).
  
- **CLIENTE**:
  - Visualiza productos, agrega al carrito y confirma compras.
  - Las compras se registran en un archivo de texto (`ordenes.txt`) con fecha, detalle y total.

El sistema utiliza:
- Clases y objetos (Producto, Catálogo, Carrito, Usuario).
- Herencia (Admin y Cliente).
- Manejo de excepciones.
- Lectura y escritura de archivos de texto.


## Cómo ejecutar el programa

1. Asegúrate de tener Python instalado en tu equipo.

2. Ubícate en la carpeta del proyecto desde la terminal:
   ```bash
   cd ecommerce_m4