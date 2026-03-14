import os
os.system('cls')

'''
<16         magreza grave
16 a <17    magreza  moderada
17 a 18,5   magreza leve
18,5 < 25   saudável
25 a <30    sobrepeso
30 a <35    obesidade grau I
35 a <40    obesidade grau II
>40         obesidade grau III
'''

def classificacao_imc(imc):
    """ Classificação do IMC """
    if imc < 16:
        return "Magreza grave"
    elif imc >=16 and imc < 17:
        return "Magreza moderada"
    elif imc >= 17 and imc < 18.5:
        return "Magreza leve"
    elif imc >= 18.5 and imc < 25:
        return "Saudável"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30 and imc < 35:
        return "Obesidade grau I"
    elif imc >= 35 and imc < 40:
        return "Obesidade grau II"
    elif imc >= 40:
        return "Obesidade grau III"
    else:
        return "Valor inválido"

# Teste da funcao
# teste = classificacao_imc(25)
# print(teste)