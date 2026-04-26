import os
os.system("cls")

productos = [
    ["Arroz", 500, 100],
    ["Tomate", 800, 3000],
    ["Papa", 700, 2000]
]
usuarios = []

def Menu_Main():
    while True:
        os.system("cls")
        print("╔══════════════════════╗")
        print("║    Menu Principal    ║")
        print("╠══════════════════════╣")
        print("║ 1. Empleado          ║")
        print("║ 2. Cliente           ║")
        print("║ 3. Salir             ║")
        print("╚══════════════════════╝")

        opciones = input("Ingrese la opcion que necesite: ")

        match opciones.lower():
            case "1":
                Menu_Gerente()
            case "2":
                Menu_cliente()
            case "3":
                print("Saliendo del programa")
                break

def Menu_Gerente():
    while True:
        os.system("cls")
        print("╔═════════════════════════╗")
        print("║      Menu Gerente       ║")
        print("╠═════════════════════════╣")
        print("║ 1. Agregar Producto     ║")
        print("║ 2. Clientes Registrados ║")
        print("║ 3. Salir                ║")
        print("╚═════════════════════════╝")

        opciones = input("Ingrese la opcion que necesite: ")

        match opciones.lower():
            case "1":
                Ingresar_productos()
            case "2":
                Mostrar_Usuarios_Registrados()
            case "3":
                print("Volviendo al Menu Principal")
                break

def Menu_cliente():
    while True:
        os.system("cls")
        print("╔══════════════════════╗")
        print("║    Menu Cliente      ║")
        print("╠══════════════════════╣")
        print("║ 1. Registrar usuario ║")
        print("║ 2. Iniciar Compra    ║")
        print("║ 3. Ver Catalogo      ║")
        print("║ 4. Salir             ║")
        print("╚══════════════════════╝")

        opciones = input("Ingrese la opcion que necesite: ")

        match opciones.lower():
            case "1":
                Registrar_usuarios()
            case "2":
                while True:
                    pregunta = input("Usted esta registrado? SI/NO: ").lower()

                    if pregunta == "no":
                        Realizar_compra(None)
                    else:
                        nombre = input("Ingrese su nombre: ").lower()
                        usuario = Buscar_usuario(nombre)

                        if usuario == None:
                            print("Usuario no encontrado, registrese primero")
                        else:
                            Realizar_compra(usuario)
            case "3":
                Mostrar_catalogo_Menu()
            case "4":
                print("Volviendo al Menu Principal")
                break

def Mostrar_Usuarios_Registrados():
    while True:
        os.system("cls")
        print("=" * 35)
        print("     👤 Clientes Registrados")
        print("=" * 35)
        for nombre, edad, tarjeta in usuarios:
            print(f"    Nombre: {nombre}")
            print(f"    Edad: {edad}")
            print(f"    Tiene tarjeta mayorista?: {tarjeta}")
            print("=" * 35)
        opcion = input("Quieres volver al menu anterior? SI/NO: ")
        match opcion.lower():
            case "si":
                print("Volviendo al Menu anterior")
                break
            case _:
                pass

def Mostrar_catalogo_Menu():
    while True:
        os.system("cls")
        print("=" * 30)
        print("   📦 CATÁLOGO DE PRODUCTOS")
        print("=" * 30)
        for numero, producto in enumerate(productos, 1):
            print(f"   {numero}. {producto[0]} - ${producto[1]}")
        print("=" * 30)
        opcion = input("Quieres volver al menu anterior? SI/NO: ")
        match opcion.lower():
            case "si":
                print("Volviendo al Menu anterior")
                break
            case _:
                pass

def Mostrar_catalogo_sin_Menu():
    print("=" * 30)
    print("   📦 CATÁLOGO DE PRODUCTOS")
    print("=" * 30)
    for numero, producto in enumerate(productos, 1):
        print(f"   {numero}. {producto[0]} - ${producto[1]}")
    print("=" * 30)

def Registrar_usuarios():
    os.system("cls")
    print("=" * 30)
    print("     👤Registrar Cliente")
    print("=" * 30)
    registro_Nombre = input("Ingrese su Nombre de Usuario: ")
    registro_edad = int(input("Ingrese su edad: "))
    tiene_tarjeta_mayorista = input("Usted tiene la tarjeta del Mayorista? si/no: ")

    usuarios.append([registro_Nombre, registro_edad, tiene_tarjeta_mayorista])
    return

def Buscar_usuario(buscar_nombre):
    os.system("cls")
    print("=" * 30)
    print("     👤Buscar Usuario")
    print("=" * 30)
    buscar_nombre = input("Ingresar nombre de cliente: ")
        
    for usuario in usuarios:
        if usuario[0].lower() == buscar_nombre:
            nombre, edad, tarjeta = usuario
            print("=" * 35)
            print(f"    Nombre: {nombre}")
            print(f"    Edad: {edad}")
            print(f"    Tiene tarjeta mayorista?: {tarjeta}")
            print("=" * 35)
            return usuario
    return None

def Ingresar_productos():
    os.system("cls")
    print("=" * 30)
    print("     📦 Ingresar Productos")
    print("=" * 30)
    nombre_producto = input("Ingresar el Nombre del producto a registrar: ")
    precio_producto = int(input("Ingrese el Precio del producto: "))
    stock_producto = int(input("Ingrese la cantidad en stock del porducto disponible: "))

    productos.append([nombre_producto, precio_producto, stock_producto])
    return

def Descuentos_por_cantidad(cantidad):

    if cantidad >= 100:
        return 15
    elif cantidad >= 50:
        return 10
    elif cantidad >= 10:
        return 5
    else:
        return 0

def calcular_descuentos(usuario, cantidad):
    total_descuento = 0

    total_descuento = Descuentos_por_cantidad(cantidad) + total_descuento
    if usuario[2] == "si":
        total_descuento = total_descuento + 5
    
    if int(usuario[1]) >= 60:
        total_descuento = total_descuento + 10
    
    return total_descuento

def Realizar_compra(usuario):
    if usuario == None:
        print("No estas logeado")
        return None
    Mostrar_catalogo_sin_Menu()
    elegir_producto = int(input("Elija el producto que quiera comprar: "))
    producto_elegido = productos[elegir_producto - 1]
    print("=" * 30)
    print(f"  Elegiste: {producto_elegido[0]}")
    print(f"  Precio: ${producto_elegido[1]}")
    print(f"  Stock: {producto_elegido[2]}")
    print("=" * 30)
    cantidad_producto = int(input("Ingrese la cantidad que quieres comprar: "))
    
    if cantidad_producto > producto_elegido[2]:
        print("No hay suficiente stock disponible")

    producto_elegido[2] = producto_elegido[2] - cantidad_producto

    precio_original = producto_elegido[1] * cantidad_producto
    descuento = calcular_descuentos(usuario, cantidad_producto)
    monto_descuento = precio_original * descuento / 100
    precio_final = precio_original - monto_descuento

    print("=" * 30)
    print("        🧾 FACTURA")
    print("=" * 30)
    print(f"   Producto : {producto_elegido[0]}")
    print(f"   Cantidad : {cantidad_producto}")
    print(f"   Precio   : ${precio_original}")
    print(f"   Descuento: {descuento}%  (-${monto_descuento})")
    print("=" * 30)
    print(f"   TOTAL    : ${precio_final}")
    print("=" * 30)



Menu_Main()
