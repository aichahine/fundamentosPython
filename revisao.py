import os
os.system('cls')
import time

''' Revisão '''

''' if elif else '''
nomePaciente = input("Digite o nome do paciente: ")
sintoma = input("Digite o sintoma: ").lower()

if sintoma == "dor no peito" or sintoma == "falta de ar":
    print("Vermelho")
elif sintoma == "pressão alta":
    print("Amarelo")
else:
    print("Verde") 


''' while '''
senha = input("\nDigite a senha: ")
confSenha = input("Digite a confirmação da senha: ")

while senha != confSenha:
    confSenha = input("Digite a senha novamente: \n")


nome = input("\nDigite o nome: ")

while nome != nome.upper():
    nome = input("Digite novamente: ")


''' while True '''
qtdeNotas = 0
somaNota = 0

while True:
    nota = float(input("Digite uma nota ou -1 para encerrar: "))
    somaNota += nota
    qtdeNotas += 1
    if nota == -1:
        print(f"Foram digitadas {qtdeNotas} notas e a soma das notas é {somaNota:.2f}.")
        break


''' for '''
for i in ["Gi", "Maicon", "Vini"]:
    print(f"{i}")
    time.sleep(0.5)


for i in range(0, 10, 1):
    print(f"{i}")
    time.sleep(0.5)


for i in range(10):
    print(f"{i}")
    time.sleep(0.5)


for i in range(10):
    if i % 2 != 0:
        print(i)
        time.sleep(0.5)