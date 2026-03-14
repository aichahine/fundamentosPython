import os
os.system('cls')

# Importando uma função criada em um módulo
from entrada_dados import recebe_peso_altura
from calculo_imc import calculo_imc
from classificacao_imc import classificacao_imc

# Menu CLI (Command Line)
while True:
    print(" --- SISTEMA DE CÁLCULO DO IMC --- ")
    print("Selecione uma das opções:\n1 - Calcular IMC\n2 - Calcular e classificar IMC\n3 - Sair")
    opcao = int(input())
    if opcao == 3:
        print("Saindo...")
        break
    elif opcao == 1:
        peso_usuario, altura_usuario = recebe_peso_altura()
        imc_usuario = calculo_imc(peso_usuario, altura_usuario)
        print(f"O seu IMC é {round(imc_usuario, 4)}")
    elif opcao == 2:
        if imc_usuario in locals():
            classificacao = classificacao_imc(imc_usuario)
            print(f"\nSeu IMC atual é {round(imc_usuario, 2)}")
            print(f"Sua classificação é: {classificacao}")
        else:
            print("É necessário calcular o IMC antes de classificar.")