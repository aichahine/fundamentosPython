import os
os.system('cls')

# Importando uma função criada em um módulo
from entrada_dados import recebe_peso_altura
from calculo_imc import calculo_imc

''' Oitava aula, 14 de março de 2026 '''
''' Projeto 01 '''

''' Modularização / Decomposição '''

# Menu CLI (Command Line)
while True:
    print(" --- SISTEMA DE CÁLCULO DO IMC --- ")
    print("Selecione uma das opções:\n1 - Calcular IMC\n2 - Sair\n")
    opcao = int(input())
    if opcao == 2:
        print("Saindo...")
        break
    if opcao == 1:
        peso_usuario, altura_usuario = recebe_peso_altura()
        imc_usuario = calculo_imc(peso_usuario, altura_usuario)
        print(f"O seu IMC é {round(imc_usuario, 4)}")
        