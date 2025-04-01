#Calculo de velocidade media de um veiculo considerando DistanciaXTempo e o gasto de combustivel

#Entrada
dist = int (input('Informe a distância percorrida em km: '))
temp = float (input('Informe o tempo gasto para percorrer o trajeto em horas: '))
cm=12


#Processamento
vel = dist/temp
consumo = dist/cm

#Saida
print (f'A velocidade média para conclusão do percurso foi de: {vel: .2f} km/h e o consumo de combustivel utilizado foi: {consumo: ,.2f} L')
