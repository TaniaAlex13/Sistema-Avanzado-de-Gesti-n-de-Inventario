from inventario import Inventario
from producto import Producto

def main():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_ = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_ = input("ID a eliminar: ")
            inventario.eliminar_producto(id_)

        elif opcion == "3":
            id_ = input("ID a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for producto in resultados:
                print(producto.to_dict())

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
