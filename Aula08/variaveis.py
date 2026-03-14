import os
os.system('cls')

def soma(*args):
    total = 0
    for num in args:
        total += num
    return total

print(soma(2, 3, 4, 6))
print(soma(2, 3, 4, 6, 5, 5, 1, 2))
print(soma(2,3))

def calculate_sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

result = calculate_sum(5, 10, 15, 20)
print(result)

# Utilizando lista
def print_lista(lista):
    for i in lista:
        print(i)

print_lista([1, 2, 3, 4])

# Utilizando *args
def print_lista(*lista):
    for i in lista:
        print(i)

print(1)
# É usado para que não seja necessário criar uma
# lista


def pessoa (**kwargs):
    print(kwargs)
    for nome, idade, in kwargs.items():
        print(f"{nome} tem atualmente {idade} anos de idade.")

pessoa(Aline='39', Gabriel=33, Rafael='47')

def display_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
    
display_info(name="Alice", age=30, profession="Engineer")
