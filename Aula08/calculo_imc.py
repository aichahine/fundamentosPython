import os
os.system('cls')

def calculo_imc(peso, altura):
    """ Recebe o peso em kg e a altura em m e calcula o IMC """
    imc = peso / (altura * altura)
    return imc

# Teste da função
# imc_teste = calculo_imc(85.7, 1.71)
# print(f"O IMC calculado é: {imc_teste:.2f}.")