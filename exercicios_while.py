import os
os.system('cls')
import time

''' Exercícios while '''


''' 5. O programa deve pedir letras ao usuário até que 
ele digite "0". Ao final, mostre quantas vogais 
(a, e, i, o, u) foram digitadas. '''

contagem = 0
letra = ''

while letra != '0':
    letra = input("Digite uma letra ou 0 para sair: ").lower()
    if letra in 'aeiou':
        contagem += 1

print(f"Fim do programa. Foram digitadas {contagem} vogais.")


'''4. O programa deve pedir a senha correta (definida no 
código). O usuário tem para acertar. Se errar todas, 
exiba "Acesso bloqueado".'''

senha = "louvre"
chances = 3 

while chances>0:
    tentativa = input("\nDigite a senha: ")
    chances -= 1
    if tentativa == senha:
        print("Senha correta.")
        break
    elif tentativa != senha and chances>0:
        print("Senha incorreta, tente novamente.")
    else:
        print("Acesso bloqueado")


''' 3. Peça ao usuário valores de produtos até que ele digite .
Ao final, exiba o total da compra. Se o usuário digitar um 
valor negativo, interrompa imediatamente o programa com break 
e mostre "Valor inválido, operação cancelada". '''

valor = 19.90
valorProduto = 0
totalCompra = 0

while valor != valorProduto:
    valorProduto = float(input("\nDigite o valor de um produto: "))
    totalCompra += valorProduto
    if valor == valorProduto:
        print(f"Fim da operação. O total da compra é: {totalCompra:.2f}")
        break
    elif valorProduto<0:
        print("Valor inválido, operação cancelada")
        break


''' 2. Peça ao usuário para adivinhar um número
secreto (fixo). O jogador terá . Se acertar antes,
mostre "Parabéns!" e encerre. Se não acertar, exiba
"Suas chances acabaram!". '''

numeroOculto = 44
chances = 3

while chances>0:
    palpite = int(input("\nAdivinhe o número secreto: "))
    chances -= 1
    if palpite == numeroOculto:
        print("Parabéns!")
        break
    elif palpite != numeroOculto and chances>0:
        print("Tente novamente!")
    else:
        print("Suas chances acabaram!")
    

''' 1. Crie um programa que peça ao usuário um
número inicial e faça uma contagem regressiva
até 0, exibindo cada número. Quando chegar em 0,
exiba "Lançar foguete!". '''

numero = int(input("\nDigite um número: "))
print(f"O número digitado é: {numero}")

while numero>0:
    print(f"Contagem regressiva: {numero}")
    time.sleep(0.5)
    numero -= 1
else:
    print(f"Lançar foguete!")