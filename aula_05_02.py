#programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são
#ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente.
lista=[]
pares=0
impares=0
lista_par=[]
lista_impar=[]
n=1

for i in range (10):
    lista.append(int(input(f'Digite o {n} valor a seguir:')))
    n+=1
    if lista [i] % 2 == 0:
        lista_par.append(lista[i])
        pares += 1
    else:
        lista_impar.append(lista[i])
        impares +=1

#Saida dos dados
print(f'A quantidade de numeros pares são:{pares}')
print(f'A quantidade de numeros impares são:{impares}')
print(f'Os pares são:{lista_par}')
print(f'Os impares são:{lista_impar}')

lista.reverse()
print(f'\nA lista reversa é:')
print(lista)

lista.sort()
print ('\nA lista em ordem crescente:')
print(lista)