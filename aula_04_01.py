#n=0
#while n <= 5:
#    print (n)
#    n=n+1
#for i in range(5):
    #print(i) onde i é a posição da linha do vetor

#programa que dado 5 números inteiros calcule a soma deles e identifique o maior deles

#Entrada de dados
soma=0
n= int(input('Digite o valor inteiro que deseja calcular: '))
maior = n
#Processamento - Estrutura de repetição
for i in range (5):
    n= int(input('Digite o valor inteiro que deseja calcular: '))
    if n > maior:
        maior = n
    soma = soma+n
    
#saida
print (f'A soma dos valores digitados é igual a: {soma}')
print (f'O maior valor encontrado foi: {maior}')
