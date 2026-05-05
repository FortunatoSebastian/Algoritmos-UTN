import pandas as pd
import os
os.system("cls")

ventas = pd.DataFrame({
    "producto": ["Arroz", "Aceite", "Arroz", "Azucar","Aceite", "Harina"],
    "categoria": ["Secos", "Aceites", "Secos", "Secos", "Aceites", "Secos"],
    "cantidad": [3, 1, 2, 4, 2, 1],
    "precio_unitario": [300, 800, 300, 400, 800, 250]
})

ventas["subtotal"] = ventas["cantidad"] * ventas["precio_unitario"]
print(ventas)
print("\n")

por_categoria = ventas.groupby("categoria")["subtotal"].sum()
print(por_categoria)
print("\n")


por_categoria.to_excel("cierre_caja.xlsx")
print("Cierre de caja")