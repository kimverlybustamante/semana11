# inventario.py
"""
Sistema de Gestión de Inventario - Local de Ropa y Maquillaje
Este programa gestiona un inventario de productos de una tienda de ropa y maquillaje.
Permite agregar, eliminar, actualizar, buscar y mostrar productos, guardando la
información en un archivo JSON para que no se pierda al cerrar el programa.
"""

import json
import os

# Clase Producto
class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"ID: {self.id} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"

# Clase Inventario
class Inventario:
    def _init_(self):
        self.productos = {}
        self.archivo = "inventario.json"
        self.cargar_inventario()

    def agregar(self, producto):
        self.productos[producto.id] = producto

    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("No existe ese ID.")

    def actualizar(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
        else:
            print("No existe ese ID.")

    def buscar(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        for p in self.productos.values():
            print(p)

    def guardar(self):
        lista = []
        for p in self.productos.values():
            lista.append({
                "id": p.id,
                "nombre": p.nombre,
                "cantidad": p.cantidad,
                "precio": p.precio
            })
        with open(self.archivo, "w") as f:
            json.dump(lista, f)

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                lista = json.load(f)
                for p in lista:
                    prod = Producto(p["id"], p["nombre"], p["cantidad"], p["precio"])
                    self.productos[prod.id] = prod
        else:
            # Inventario inicial
            inicial = [
                Producto(1, "Blusa", 10, 15),
                Producto(2, "Pantalón", 5, 25),
                Producto(3, "Vestido", 7, 40),
                Producto(4, "Labial", 15, 8),
                Producto(5, "Base de maquillaje", 8, 12),
                Producto(6, "Sombras de ojos", 12, 10)
            ]
            for p in inicial:
                self.productos[p.id] = p
            self.guardar()


# Menú interactivo
def menu():
    inv = Inventario()
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Mostrar todos los productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Guardar y salir")
        opcion = input("Elige opción: ")

        if opcion == "1":
            inv.mostrar_todos()
        elif opcion == "2":
            try:
                id = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inv.agregar(Producto(id, nombre, cantidad, precio))
                print("Producto agregado.")
            except:
                print("Error en los datos.")
        elif opcion == "3":
            try:
                id = int(input("ID a actualizar: "))
                cantidad = input("Nueva cantidad (enter si no cambia): ")
                precio = input("Nuevo precio (enter si no cambia): ")
                inv.actualizar(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
                print("Producto actualizado.")
            except:
                print("Error en los datos.")
        elif opcion == "4":
            try:
                id = int(input("ID a eliminar: "))
                inv.eliminar(id)
                print("Producto eliminado.")
            except:
                print("Error en los datos.")
        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            encontrados = inv.buscar(nombre)
            if encontrados:
                for p in encontrados:
                    print(p)
            else:
                print("No encontrado.")
        elif opcion == "6":
            inv.guardar()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()