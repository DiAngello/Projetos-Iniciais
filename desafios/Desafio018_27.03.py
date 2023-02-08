from math import sin, cos, tan, radians
a=int(input('Digite o valor do ângulo em graus:'))
rad=radians(a)
print('O valor do seno do ângulo {} vale: {}'.format(a,sin(rad)))
print('O valor do cosseno do ângulo {} vale: {}'.format(a,cos(rad)))
print('O valor da tangente do ângulo {} vale: {}'.format(a,tan(rad)))
