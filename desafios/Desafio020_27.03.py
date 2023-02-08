import random
a1=str(input('Nome do aluno:'))
a2=str(input('Nome do aluno:'))
a3=str(input('Nome do aluno:'))
a4=str(input('Nome do aluno:'))
list=[a1,a2,a3,a4]
random.shuffle(list)
print('A ordem de apresentação será: ')
print(list)
