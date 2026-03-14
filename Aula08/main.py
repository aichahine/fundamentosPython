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
            print(f"A classificação do usuário é {classificacao_imc(imc_usuario)}.")
        else:
            print("É necessário calcular o IMC para obter a sua classificação.")