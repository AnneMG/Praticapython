#Programa pra calcular o peso ideal
#nome
#Genero
altura= float(input("informe a altura da pessoa: "))

#Calculo do peso
#homens
h=(72.7*altura) - 58

#mulheres
m=(62.1*altura) - 44.7

#Saida dos dados
print (f"O peso ideal para homens é: {h: .0f} kg.")
print (f"O peso ideal para mulheres é: {m: .0f} kg.")