#Programa dado p 5 números inteiros calcule a soma deles identificando o maior deles e a pessoa mais velha/nova
#Entrada
soma=0
old=0
midade = 200
#Processamento
for i in range (3):
    nome= input ('Informe o nome do usuario: ')
    idade= int(input ('Informe a idade do usuario:'))
    
    if idade > old:
        old=idade
        ynome=nome  
    if idade < midade:
        midade=idade     
        mnome=nome
    soma = soma + idade
#Saida
print(f'A soma das idades: {soma}')
print(f'O valor da média das idades: {(soma/(i+1)):.2f}')
print (f'A maior idade digitada foi de {ynome} com {old} anos.')
print (f'A menor idade digitada foi de {mnome} com {midade} anos.')

