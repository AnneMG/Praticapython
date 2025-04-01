# programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue 
nome= input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))
peso= float(input('Informe o seu peso: '))
sono= int(input ('Informe quantas horas de sono teve durante a noite: '))

#processamento
if (idade ==16 and idade<=69) and peso > 50 and sono >=6:
    print (f'A doação de {nome} esta permitida pois os criterios foram atendidos conforme a seguir: Idade= {idade} anos encontrando-se com {peso} kg após ter dormido {sono} horas nas ultimas 24hs.')
elif idade < 16 or idade > 69:
    print ('A idade informada não é permitida para doação de sangue.')
elif peso < 50:
    print ('O peso informado não é permitido para doação de sangue.')
elif sono < 6:
    print ('A quantidade de sono informado não é permitida para doação de sangue.')
else:
    print (f'{nome} não tem permissão para realizar a doação no momento por não atender aos requisitos. Atualmente esta com {idade} anos, pesando {peso} kg e descansou {sono} horas de sono nas ultimas 24hs')

#outra forma de execução para a estrutura
#if idade >= 16 and idade <=69:
#   if peso >=50:
#      if sono >=6: 
#            print('voce esta apto')
#        else:
#            print('vc nao esta apto devido a ter dormido menos de 6hs')
#    else:
#        print('vc nao esta apto por ter menos que 50 kg')
#else:
#    print ('vc nao esta apt a dormir')

