#Módulos - bibliotecas
#import
#from...import
#biblioteca math:
#ceil
#floor
#trunc
#pow
#sqrt
#fatorial
import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print('A raiz de {} vale {}: '.format(num,raiz))
print('Arredondando para cima vale: {}'.format(math.ceil(raiz)))
print('Arredondando para baixo vale: {}'.format(math.floor(raiz)))
