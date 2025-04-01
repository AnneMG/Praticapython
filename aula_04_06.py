#programa que calcule o fatorial de um número inteiro fornecido pelo usuário

n=int(input('Digite um numero para calcular o seu fatorial:'))
fat=1

for i in range(1,n+1):
    fat = fat * i

print (f'O fatorial de {n} é: {fat}')