import random
n1=random.randint(0,5)
print("""Pensando em um número de 0 a 5...
      Pronto?""")
n2=int(input('Tente adivinhar o número que pensei: '))
if n2 == n1:
    print('PARABÉNS!!! Você acertou!!! ')
else:
    print('Que pena, você errou!')
    print('O número era: {}'.format(n1))