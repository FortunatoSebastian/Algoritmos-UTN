import os 
os.system("cls")

def Mostrar_Producto():
    print("-" * 50)
    print("-" * 15 + "|Valor de Productos|" + "-" * 15)
    print("-" * 50)
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = int(input("Ingrese el precio del producto: "))
    
    precio_con_iva = precio_producto * 1.21
    print("-" * 50)
    print(f"Producto sin IVA: {nombre_producto} - ${precio_producto}")
    print(f"Producto Con IVA: {nombre_producto} - ${precio_con_iva}")
    return

Mostrar_Producto()