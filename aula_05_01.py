nomes='Joao, Maria, Ana, Luiz'
nomes_lista= ["Joao", "Maria", "Ana", "Luiz"]
lista=[]
#Processamento
for i in range (5):
    lista.append(input('Digite um nome de alimento para incluir na lista:'))
    #lista.append(int((input('Digite um nome de alimento para incluir na lista:')))
    #media=(sum(num)/len(lista))
    
#Saida dos dados
print ('A lista de compras foi preenchida com os seguintes itens: ')
total= int(len(lista))
#for i in range(len(lista)):
while i < total:
    print ({lista[i]})
#pos=index.lista('Arroz')
print(f'O tamanho da lista é: {total}')
#print(f'A posiçao do elemento é {pos}')
print(nomes)
print(nomes_lista[2])
