s = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        s += n
print('O somatória dos valores pares é: {}'.format(s))
