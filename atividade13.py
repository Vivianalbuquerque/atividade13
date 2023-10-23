# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
n1 = float(input("qual o primeiro numeros?"))
n2 = float(input("qual o segundo numero?"))
n3 = float(input("qual o terceiro numero?"))
maior = n1
if maior < n2:
    maior = n2
else: maior < n3
maior = n3
print(f"O numero maior é{maior}!")