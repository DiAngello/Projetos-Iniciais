from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''\033[34mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
p1 = int(input('\033[32mQual é a sua jogada?\033[m '))
print('\033[33mJO\033[m')
sleep(1)
print('\033[33mKEN\033[m')
sleep(1)
print('\033[33mPO!!!\033[m')
print('\033[36m-=\033[m' * 13)
print('\033[32mComputador jogou {}\033[m'.format(itens[pc]))
print('\033[32mJogador jogou {}\033[m'.format(itens[p1]))
print('\033[36m-=\033[m' * 13)
if pc == 0:
    if p1 == 0:
        print('\033[31mEMPATE!\033[m')
    elif p1 == 1:
        print('\033[31mJOGADOR VENCE!\033[m')
    elif p1 == 2:
        print('\033[31mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif pc == 1:
    if p1 == 0:
        print('\033[31mCOMPUTADOR VENCE!\033[m')
    elif p1 == 1:
        print('\033[31mEMPATE!\033[m')
    elif p1 == 2:
        print('\033[31mJOGADOR VENCE!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif pc == 2:
    if p1 == 0:
        print('\033[31mJOGADOR VENCE\033[m!')
    elif p1 == 1:
        print('\033[31mCOMPUTADOR VENCE!\033[m')
    elif p1 == 2:
        print('\033[31mEMPATE!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
