#Condições
###Métodos terminam com ()
####if : bloco True
####else: bloco False
tempo=int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
#Condição simplificada
print('Carro novo'if tempo<=3 else'Carro velho')
