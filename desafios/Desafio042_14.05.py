n1=int(input('O valor da primeira reta: '))
n2=int(input('O valor da segunda reta: '))
n3=int(input('O valor da terceira reta: '))
if (n1+n2) >= n3:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
if n1 == n2 == n3:
    print('\033[34mTriângulo equilátero\033[m')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('\033[34mTriângulo isórceles\033[m')
else:
    print('\033[34mTriângulo escaleno\033[m')
