#Programa de calculo de atraso de prestação
prestacao = float (input('Informe o valor da prestação: R$'))
taxa = float(input('Informe a taxa a ser aplicada: '))
tempo = int(input('Informe o prazo que deseja calcular: '))

#Processamento
juros=prestacao*(taxa/100)*tempo
valorfinal=prestacao+juros

#Saida dos dados
print (f'O calculo dos juros da prestação é de: R${juros: ,.2f} \na ser pago em {tempo} parcelas')
print (f'O valor da prestação a ser paga com atraso é de: R${valorfinal:,.2f}')