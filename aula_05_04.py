#programa que armazene em vetores o nome, a média e a situação de um
#grupo de 10 alunos. Ao final mostre o nome de cada aluno com sua respectiva situação.
aluno=[]
media=[]
sit=[]
for i in range(3):
    aluno.append(input('Informe o nome do aluno: '))
    media.append(float(input(f'Informe a média de: ')))
    if media[i] >= 70:
        sit.append("Aprovado")
    else:
        sit.append("Reprovado")
#Saida dos dados
for i in range(len(aluno)):
    print(f'O aluno {aluno[i]} obteve a média {media[i]} apresentando a situação {sit[i]}')
