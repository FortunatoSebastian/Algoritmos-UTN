def prueba (num1, num2, *args,**kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"Kwargs {clave} = {valor}")

prueba(15,50,100,200,400,x=3, y=5, z=2)