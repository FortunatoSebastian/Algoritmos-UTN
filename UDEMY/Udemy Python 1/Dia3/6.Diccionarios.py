#1 y 2
diccionario = {'c1':'valor1','c2':'valor2'}

resultado = diccionario['c1']
print(f"1. {diccionario}")
print(f"2. {resultado}")

#3 y 4 
cliente = {'nombre':'juan', 'apellido':'fuentes', 'peso':'88', 'talla':1.76}
consulta = (cliente['apellido'])
print(f"3. {cliente}")
print(f"4. {consulta}")

#5
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(f"5. {dic['c3']}")

#6
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(f"6. {dic['c2'][1]}".upper())

dic = {1: 'a', 2:'b'}
print(dic)

dic[3] = 'c'
print(f"7. {dic}")

dic[2] = 'B'
print(f"8. {dic}")

#Imprime las llaves de entrada
print(dic.keys())
#Imprime los valores de los diccionarios
print(dic.values())
#Imprime la llave con su valor
print(dic.items()) 