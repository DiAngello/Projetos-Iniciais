vc=int(input('Digite o valor da casa: '))
s=int(input('Digite seu sálario: '))
a=int(input('Digite em quantos anos você pagará: '))
vp=vc/a
if vp>(30/100)*s:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
