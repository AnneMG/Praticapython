#Programa para calculo de idade
import datetime

#variaveis do programa
ano_nasc= int(input('Informe o ano de nascimento do individuo: '))
#atual= int(input('informe o ano que deseja considerar para calculo da idade: '))
data_atual = datetime.date.today()
atual= data_atual.year
#mes = int(input('Informe o mês de nascimento do individuo: '))

#Processamento
idade = atual - ano_nasc

#Saida dos dados
print (f'A idade do individuo corresponde a: {idade} anos.')