#programa que calcule e mostre a tabuada de um número inteiro fornecido pelo usuário

num=int(input('Informe um numero para calcular a tabuada: '))

for i in range (1,11):
    tab=num*(i)

#Saída
    print(f'O resultado da tabuada é: {num}X{i}={tab}')
    