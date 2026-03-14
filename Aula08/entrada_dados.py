import os
os.system('cls')

def recebe_peso_altura():
    """ Recebe o peso em kg e a altura em m do usuário """
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em mm: "))

    return peso, altura

# Teste da função
# peso_teste, altura_teste = recebe_peso_altura()
# print(f"{peso_teste:.2f}")
# print(f"{altura_teste:.2f}")