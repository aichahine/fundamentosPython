import os
os.system('cls')

''' 1. Crie uma função contar_pares(*n) que conte e retorne quantos números pares
existem nos parametros passados. '''

def contar_pares(*n):
    cont_par = 0
    for i in n:
        if i % 2 == 0:
            cont_par += 1
            print(i)
    else:
        print(cont_par)


contar_pares(2, 4, 6, 9, 12, 15)

''' 2. Crie uma função cubica(*nums) que devolve uma lista com o cubo de cada número
recebido. Use for. '''

def cubica(*nums):
    for i in nums:
        nums == nums**3
        print(i)
    else:
        print("Else")

cubica(2, 4, 6, 9, 12, 15)