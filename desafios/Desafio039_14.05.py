id=int(input('Digite a sua idade: '))
if id == 18:
    print('Você precisa se alistar, já está na hora!')
elif id <= 18:
    print('Você ainda vai se alistar, faltam {} ano(s)'.format(18 - id))
elif id >= 18:
    print('Já passou o seu tempo de alistamento, passou {} ano(s)'.format(id - 18))
