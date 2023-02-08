f=str(input('Digite uma frase: '))
print('A ocorrência da letra A na frase é: {}'.format(f.lower().count('a')))
print('A primeira aparição da letra A na frase é: {}'.format(f.lower().find('a')+1))
print('A última aparição da lentra A na frase é: {}'.format(f.lower().rfind('a')+1))
