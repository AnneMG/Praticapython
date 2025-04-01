#Programa que dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior
n1= int(input('Informe o primeiro numero: '))
n2= int(input('Informe o segundo numero: '))
n3= int(input('Informe o terceiro numero: '))

#Processamento
if n1 > n2 and n1 > n3:
    print(f'O maior é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior é {n3}')
else:
    print(f'Existem pelo menos 2 valores iguais.')