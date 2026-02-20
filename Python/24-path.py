from pathlib import Path

# guia = Path(Path.home(),"C:\\Users\\Damia\\Desktop\\recetas")


# contador = 0
# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)
#     contador += 1

# print(f"Total de recetas encontradas: {contador}")

guia = Path("C:\\Users\\Damia\\Desktop\\recetas")

contador = 0
print("\n--  Recetas encontradas  --")
for txt in guia.glob("**/*.txt"):
    # print(f"Receta encontrada: {txt.stem}")
    print(f"{txt.stem}")
    contador += 1

print(f"\nTotal de recetas encontradas: {contador}")