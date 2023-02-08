n=int(input('Digite um número: '))
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
bc=int(input('Qual será a base da conversão: '))
if bc == 1:
    print(str(bin(n)))
elif bc == 2:
    print(str(oct(n)))
elif bc == 3:
    print(str(hex(n)))
