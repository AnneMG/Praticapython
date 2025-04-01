# Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes. E Utilizando a estrutura do programa 
#anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.
#Entrada de dados
n1= int(input('Informe o primeiro valor: '))
n2= int(input('Informe o segundo valor: '))

#Processamento
if n1== n2:
    val = n1+n2
    print (f'Eles são iguais! O valor da soma é {val}')
else:
    print (f'Eles são diferentes! O valor da multiplicação é {n1*n2}')

    