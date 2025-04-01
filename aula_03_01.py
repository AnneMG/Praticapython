#Programa para liberar acesso a maiores de 19 anos
idade= int(input('Digite a sua idade a seguir:'))
print (f'A idade informada é:{idade}')
if idade < 18:
    print ('Você é menor de idade. Acesso negado!')
elif idade == 18:
    print ('Você tem 18 anos, acesso liberado!')
elif idade > 18 and idade >= 65 :
    print ('Acesso liberado')
else:
    print ('Você tem mais de 65 anos. O acesso foi liberado com cautela.')