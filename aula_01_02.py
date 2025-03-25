#Calculo do salario liquido de um funcionário

#Entrada
ht= float (input('Informe quantidade de horas trabalhadas: '))
vh = float (input('Informe o valor da hora trabalhada: '))
pd = float (input('Informe o percentual de desconto da hora trabalhada: '))
td = float (input('Informe o total de desconto: '))

#Processamento do salario bruto considerando horas e valor da hora trabalhada
sb = ht*vh
#Calculando o total de desconto considerando o percentual de desconto multiplicado pelo salario bruto
td= (pd/100)*sb
#Resultado do salario liquido = salario bruto - total de desconto
sl= sb - td 

#Saida
print (f'O valor do salario bruto calculado é de: R${sb: ,.2f}')
print (f'O valor total de desconto calculado é de: R${td: ,.2f}')
print (f'O valor do salario liquido calculado é de: R${sl: ,.2f}')