n = int(input('Digite um número: '))
d = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        d += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
    print('Ele foi dividido {} vezes'.format(d))
if d == 2:
    print('\033[31mÉ um número primo\033[m')
else:
    print('\033[31mNão é um número primo\033[m')
