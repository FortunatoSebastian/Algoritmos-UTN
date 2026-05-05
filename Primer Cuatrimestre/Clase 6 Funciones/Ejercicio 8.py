# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def numero_maximo(num1, num2, num3):
    return max(num1, num2, num3)
num_mas_grande = numero_maximo(10, 150, 45)
print(f"El numero mas grande es: {num_mas_grande}")