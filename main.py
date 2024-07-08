nombres = {}
cantidades = {}
precios = {}
numRepuestos = 0


productos_predefinidos = [
    {"nombre": "Aceite", "cantidad": 10, "precio": 20.0},
    {"nombre": "Filtro de Aire", "cantidad": 15, "precio": 10.0},
    {"nombre": "Bujía", "cantidad": 30, "precio": 5.0},
    {"nombre": "Amortiguador", "cantidad": 5, "precio": 50.0},
    {"nombre": "Llantas", "cantidad": 20, "precio": 100.0}
]

# Función para guardar nombres en archivo
def guardar_nombres():
    with open("nombres.txt", "w") as file:
        for nombre in nombres.values():
            file.write(nombre + "\n")

# Función para guardar cantidades en archivo
def guardar_cantidades():
    with open("cantidades.txt", "w") as file:
        for nombre, cantidad in cantidades.items():
            file.write(f"{nombre}:{cantidad}\n")

# Función para guardar precios en archivo
def guardar_precios():
    with open("precios.txt", "w") as file:
        for nombre, precio in precios.items():
            file.write(f"{nombre}:{precio}\n")

# Función para cargar nombres desde archivo
def cargar_nombres():
    global numRepuestos
    try:
        with open("nombres.txt", "r") as file:
            for line in file:
                nombre = line.strip()
                nombres[nombre] = nombre
                numRepuestos += 1
    except FileNotFoundError:
        print("Archivo nombres.txt no encontrado. Iniciando con inventario vacío.")

# Función para cargar cantidades desde archivo
def cargar_cantidades():
    try:
        with open("cantidades.txt", "r") as file:
            for line in file:
                nombre, cantidad = line.strip().split(":")
                cantidades[nombre] = int(cantidad)
    except FileNotFoundError:
        print("Archivo cantidades.txt no encontrado. Iniciando con inventario vacío.")

# Función para cargar precios desde archivo
def cargar_precios():
    try:
        with open("precios.txt", "r") as file:
            for line in file:
                nombre, precio = line.strip().split(":")
                precios[nombre] = float(precio)
    except FileNotFoundError:
        print("Archivo precios.txt no encontrado. Iniciando con inventario vacío.")

# Función para inicializar los productos 
def inicializarProductos():
    global numRepuestos
    cargar_nombres()
    cargar_cantidades()
    cargar_precios()

    if not nombres:  # Si no se cargaron nombres, inicializar con productos predefinidos
        for producto in productos_predefinidos:
            nombre = producto["nombre"]
            cantidad = producto["cantidad"]
            precio = producto["precio"]
            nombres[nombre] = nombre
            cantidades[nombre] = cantidad
            precios[nombre] = precio
            numRepuestos += 1
        guardar_nombres()
        guardar_cantidades()
        guardar_precios()

# Función para imprimir el menú
def imprimirMenu():
    print("\n=== Menú ===")
    print("1. Ingresar nuevo repuesto")
    print("2. Editar repuesto")
    print("3. Eliminar repuesto")
    print("4. Listar repuestos")
    print("5. Calcular total de dinero")
    print("6. Salir")
    print("============")

# Función para ingresar un nuevo repuesto
def ingresarRepuesto():
    global numRepuestos
    if numRepuestos >= 20:
        print("Error: inventario lleno.")
        return

    nombre = input("Ingrese el nombre del repuesto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    # Verificar si el repuesto ya existe
    if nombre in nombres:
        cantidades[nombre] += cantidad
        print(f"Cantidad actualizada correctamente para '{nombre}'.")
    else:
        nombres[nombre] = nombre
        cantidades[nombre] = cantidad
        precios[nombre] = precio
        numRepuestos += 1
        print(f"Repuesto '{nombre}' ingresado correctamente.")

    guardar_nombres()
    guardar_cantidades()
    guardar_precios()

# Función para editar un repuesto
def editarRepuesto():
    global cantidades
    nombreEditar = input("Ingrese el nombre del repuesto a editar: ")

    if nombreEditar in nombres:
        nuevaCantidad = int(input("Ingrese la nueva cantidad: "))
        cantidades[nombreEditar] = nuevaCantidad
        print(f"Repuesto '{nombreEditar}' editado correctamente.")
        guardar_cantidades()
    else:
        print(f"Repuesto '{nombreEditar}' no encontrado.")

# Función para eliminar un repuesto
def eliminarRepuesto():
    global numRepuestos
    if numRepuestos == 0:
        print("No hay repuestos para eliminar.")
        return

    nombreEliminar = input("Ingrese el nombre del repuesto a eliminar: ")

    if nombreEliminar in nombres:
        cantidadEliminar = int(input(f"Ingrese la cantidad de '{nombreEliminar}' a eliminar: "))
        if cantidadEliminar > 0 and cantidadEliminar <= cantidades[nombreEliminar]:
            cantidades[nombreEliminar] -= cantidadEliminar
            if cantidades[nombreEliminar] == 0:
                del nombres[nombreEliminar]
                del cantidades[nombreEliminar]
                del precios[nombreEliminar]
                numRepuestos -= 1
                print(f"Repuesto '{nombreEliminar}' eliminado completamente del inventario.")
            else:
                print(f"{cantidadEliminar} unidades de '{nombreEliminar}' eliminadas correctamente.")

            guardar_nombres()
            guardar_cantidades()
            guardar_precios()
        else:
            print(f"Cantidad inválida o no hay suficientes unidades de '{nombreEliminar}' en el inventario.")
    else:
        print(f"Repuesto '{nombreEliminar}' no encontrado en el inventario.")

# Función para listar todos los repuestos
def listarRepuestos():
    print("\n=== Inventario de Repuestos ===")
    for nombre, cantidad in cantidades.items():
        print(f"Nombre: {nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: {precios[nombre]:.2f}")
        print(f"Total: {cantidad * precios[nombre]:.2f}")
        print("-----------------------------")
    print(f"Total de repuestos: {numRepuestos}")
    print("==============================")

# Función para calcular el total de dinero en el inventario
def calcularTotalDinero():
    total = 0
    for nombre, cantidad in cantidades.items():
        total += cantidad * precios[nombre]
    return total


def main():
    inicializarProductos()  
    opcion = 0
    while opcion != 6:
        imprimirMenu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ingresarRepuesto()
            elif opcion == 2:
                editarRepuesto()
            elif opcion == 3:
                eliminarRepuesto()
            elif opcion == 4:
                listarRepuestos()
            elif opcion == 5:
                print(f"El total de dinero en el inventario es: {calcularTotalDinero():.2f}")
            elif opcion == 6:
                print("Guardando datos y saliendo del programa...")
                guardar_nombres()
                guardar_cantidades()
                guardar_precios()
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
