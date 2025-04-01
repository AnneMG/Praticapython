#Programa p calcular a media de cada aluno e mostrar a situação d cada um deles de acordo com parametros
#Entrada

#Processamento
for aluno in range (2):
    nome= input ('Informe o nome do aluno: ')
    nota1= float(input ('Informe a primeira nota recebida:'))
    nota2= float(input ('Informe a segunda nota recebida:'))
    media = (nota1 + nota2)/2    
#Saida mostrando as médias de cada aluno
    if media >= 70:
        print (f'A média alcançada por {nome} foi de {media} tendo o resultado alcançado.')
    elif media >= 30 and media < 70:
        print (f'A média alcançada por {nome} foi de {media} tendo o resultado parcialmente alcançado.')
    else:
        print (f'A média alcançada por {nome} foi de {media} não tendo o resultado alcançado.')
   
   
    
    