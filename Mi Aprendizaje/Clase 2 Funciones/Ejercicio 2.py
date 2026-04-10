def calcular_total(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(calcular_total(3,5,1))