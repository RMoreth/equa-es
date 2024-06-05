import math
"""
Crie um programa onde o usuário decide qual equação ele deseja calcular: equação do 1º grau ou equancao do 2º grau
"""
calcular_grau1 = lambda a, b: ((c-(b)) / a) 

def calcular_grau2(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        yield ("esta equação não possui solução real")
    elif delta == 0:
        resultado = -(b) / (2 * a)
        yield resultado
    else:
        resultado1 = (-(b) + math.sqrt(delta)) / (2 * a)
        yield resultado1
        resultado2 = (-(b) - math.sqrt(delta)) / (2 * a)
        yield resultado2


eq = int(
    input("Qual equação vc deseja usar? [1 para 1º grau e 2 prar 2º grau]"))
a = float(input("Informe o valor de A: "))
b = float(input("informe o valor de B: "))
c = float(input("infomr o valor de C: "))
if eq == 1:
    print(calcular_grau1(a, b))
elif eq == 2:
    resultado = calcular_grau2(a, b ,c)
    
    for item in resultado:
        print(f'resultado: {item}')


    
else:
    print("opção inexistente")

