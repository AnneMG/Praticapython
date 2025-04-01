#Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e
#se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor
#não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo
#segundo valor.

for i in range (2):
    val1= int (input('Informe o primeiro valor: '))
    val2= int (input('Informe o segundo valor: '))
    if val2 == 0:
        print('O valor digitado é zero e não válido.Informe a seguir um novo valor.')
        val2= int (input('Informe o segundo valor: '))
        
    
# poderia ser usado: while n2 == 0: n2 = int(input("Digite o segundo valor: "))
#Saída
    print(f'O resultado da divisão do primeiro valor {val1} pelo segundo  {val2} é: {(val1/val2):.2f}')