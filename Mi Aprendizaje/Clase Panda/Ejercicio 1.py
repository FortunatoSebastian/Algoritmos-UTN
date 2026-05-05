import pandas as pd
import os
os.system("cls")
productos = pd.DataFrame({
    "nombre": ["Arroz", "Aceite", "Azucar", "Harina"],
    "stock": [50, 20, 5, 30],
    "precio": [300, 800, 400, 250]
})


productos["valor_total"] = productos["stock"] * productos["precio"]
# print(productos)
print("\n")
bajo_stock = productos[productos["stock"] < 25]
# print(bajo_stock)

productos_ordenados = productos.sort_values("valor_total", ascending=False)
print(productos_ordenados)

productos_ordenados.to_excel("reporte_almacen.xlsx", index=False)
print("Archivo Exportado...")