'''Dinâmica - Quem somos em Python?

Cada grupo deverá criar um script simples em Python contendo variáveis para
representar os integrantes do grupo, com pelo menos as seguintes
informações sobre cada integrante:

Nome completo;

Idade;

Profissão ou curso atual;

Algo curioso ou um hobby pessoal;

Em seguida, realize uma apresentação curta e criativa do grupo usando essas
variáveis, através de print() formatado no Python.'''

import os 
os.system('cls')

nome = input("Digite o seu nome completo: ")
print("O seu nome é:",nome,"\n")

idade = int(input("Digite a sua idade: "))
print("A sua idade é:",idade,"\n")

profissao = input("Digite a sua profissão: ")
print("Sua profissão é:",profissao,"\n")

curiosidade = input("Conte algo curioso sobre você: ")
print("A curiosidade a seu respeito é:",curiosidade,"\n")

hobby = input("Digite um hobby seu: ")
print("Seu hobby é:",hobby,"\n")

print(" - Apresentação Pessoal - \n\nBom dia :)\n\nMeu nome completo é",nome,"e tenho",idade,"anos de idade. Minha ocupação é ser",profissao,".\nUm fato curioso sobre mim é que",curiosidade,"e um dos meus hobbies é",hobby,".")