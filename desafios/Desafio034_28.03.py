s=int(input('Qual é o seu salário? '))
if s >= 1250.00:
    a1=0.1*s
    vt1=a1+s
    print('Seu aumento será de R$ {}, totalizando R$ {}'.format(a1,vt1))
else:
    a2=0.15*s
    vt2=a2+s
    print('Seu aumento será de R$ {}, totalizando R$ {}'.format(a2,vt2))
