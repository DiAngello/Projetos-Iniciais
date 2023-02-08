n1=int(input('Digite sua primeira nota: '))
n2=int(input('Digite sua segunda nota: '))
nt=(n1+n2)/2
if nt <= 5.0:
    print('\033[34mREPROVADO\033[m {}'.format(nt))
elif 5.0 <= nt <= 6.9:
    print('\033[34mRECULPERÇÃO\033[m {}'.format(nt))
elif nt >= 7.0:
    print('\033[34mAPROVADO\033[m {}'.format(nt))
