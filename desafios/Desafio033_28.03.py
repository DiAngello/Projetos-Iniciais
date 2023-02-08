n1=int(input('Escolha o primeiro número: '))
n2=int(input('O segundo número: '))
n3=int(input('E o terceiro número: '))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor será: {}'.format(menor))
print('O maior valor será: {}'.format(maior))
