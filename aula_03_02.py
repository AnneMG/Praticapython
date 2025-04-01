#Programa pra calcular o peso ideal com estrutura de controle
nome = input('Digite o seu nome a seguir: ')
gen = input('Informe o sexo que deseja consultar (F/M)= ')
altura = float(input("Informe a altura da pessoa(use ponto para separar): "))

#Calculo do peso
if gen == 'M' or gen == 'm':
    M = (72.7*altura) - 58
    print (f"O peso ideal para o {nome} é: {M: ,.0f} kg.")

elif gen == 'F' or gen == 'f':
    F = (62.1*altura) - 44.7
    print (f"O peso ideal para a {nome} é: {F: ,.0f} kg.")
    
else:
    print("Verifique o sexo informado de acordo com o apresentado na pergunta.")