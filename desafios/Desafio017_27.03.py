from math import sqrt,pow
co=int(input('Digite o valor do cateto oposto: '))
ca=int(input('Digite o valor do cateto adjeacente: '))
h=sqrt((pow(co,2))+(pow(ca,2)))
print('A hipotenusa do triângulo vale: {}'.format(h))
