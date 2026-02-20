def devolver_distintos(a, b, c):
    suma = a + b + c

    if suma > 15:
        return max(a,b,c)
    
    elif suma < 10:
        return min(a,b,c)
    
    else:
        lista = [a,b,c]
        lista.sort()
        return lista[1]
    

print(devolver_distintos(1,2,3))