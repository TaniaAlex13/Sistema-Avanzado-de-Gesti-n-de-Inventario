import json
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenamiento eficiente

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre.lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto.to_dict())

    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            datos = {id_: prod.to_dict() for id_, prod in self.productos.items()}
            json.dump(datos, f, indent=4)
        print("Inventario guardado.")

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                for id_, info in datos.items():
                    producto = Producto(
                        info["id"],
                        info["nombre"],
                        info["cantidad"],
                        info["precio"]
                    )
                    self.productos[id_] = producto
            print("Inventario cargado.")
        except FileNotFoundError:
            print("No existe archivo previo.")
    