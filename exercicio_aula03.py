import os
os.system('cls')

''' 3. Desenvolva um programa em Python que peça ao usuário para criar uma senha e,
em seguida, solicite que ele a digite novamente. Continue pedindo até que as duas
senhas correspondam. '''

senha1 = input("Digite sua senha: ")
senha2 = input("Digite sua senha novamente: ")

while senha1 != senha2:
  print("As senhas são diferentes.")
  senha1 = input("Digite sua senha: ")
  senha2 = input("Digite sua senha novamente: ")
else:
  print("As senhas são iguais.")

# Outra solução:

# senha1 = input("Digite sua senha: ")
# senha2 = input("Digite sua senha novamente: ")

# while senha1 != senha2:
#   senha2 = input("Digite sua senha novamente: ")
# else:
#   print("As senhas são iguais.")


''' 4. Crie um programa em Python que leia números inteiros do teclado até que o usuário
digite 0. Ao final, exiba a soma de todos os números digitados '''

# Atributo para somar os números recebidos
soma = 0

while True:
  numero = int(input("Digite um dos números do teclado ou zero para finalizar: "))
  soma += numero
  if numero == 0:
    print("\nPrograma encerrado.")
    break
  numero = int(input("Digite mais um número do teclado: "))
  soma += numero

print(f"Soma: {soma}")
