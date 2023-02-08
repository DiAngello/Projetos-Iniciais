vp=int(input('Digite o valor do produto: '))
print('1 para \033[34mà vista dinheiro/cheque\033[m')
print('2 para \033[34mà vista no cartão\033[m')
print('3 para \033[34mem até 2x no cartão\033[m')
print('4 para \033[34m3x ou mais no cartão\033[m')
fp=int(input('Digite a forma de pagamento: '))
if fp == 1:
    print('O valor a ser pago será: {} reais'.format(vp-(vp*(10/100))))
elif fp == 2:
    print('O valor a ser pago será: {} reais'.format(vp-(vp*(5/100))))
elif fp == 3:
    print('O valor a ser pago será: {} reais'.format(vp))
elif fp == 4:
    print('O valor a ser pago será: {} reais'.format(vp+(vp*(20/100))))
