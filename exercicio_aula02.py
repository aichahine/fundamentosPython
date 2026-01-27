import os
os.system('cls')

''' Desafio - Desconto no posto de gasolina
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
. até 20 litros, desconto de 3% no preço total;
. acima de 20 litros, desconto de 5% no preço total.

Gasolina:
. até 20 litros, desconto de 4% no preço total;
. acima de 20 litros, desconto de 6% no preço total.

Escreva um algoritmo que leia o número de litros vendidos e o
tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e
imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da

gasolina é R$ 5,50 e o preço do litro do
álcool é R$ 3,89.'''

tipoCombustivel = input("Digite o tipo de combustível:\nA - álcool\nG - gasolina\n").upper()
volume = float(input("Digite o volume em litros de combustível que deseja abastecer: "))
gasolina = 5.50
alcool = 3.89

# Álcool
if tipoCombustivel == 'A' and volume<=20:
  print("Aplicado o desconto de 3%, o valor a ser pago é: R$",round(volume*alcool*0.97,2))
elif tipoCombustivel == 'A' and volume>20:
  print("Aplicado o desconto de 5%, o valor a pagar é: R$",round(volume*alcool*0.95,2))
# Gasolina
elif tipoCombustivel == 'G' and volume<=20:
  print("Aplicado o desconto de 4%, o valor a ser pago é: R$",round(volume*gasolina*0.96,2))
elif tipoCombustivel == 'G' and volume>20:
  print("Aplicado o desconto de 6%, o valor a ser pago é: R$",round(volume*gasolina*0.94,2))
else:
  print("Opção inválida.")