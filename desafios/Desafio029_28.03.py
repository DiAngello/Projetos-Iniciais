v=int(input('Qual a velocidade do seu carro, em Km/h? '))
if v > 80:
    print('Você foi multado!')
    m=(v-80)*7.0
    print('Sua multa vale: {}'.format(m))
else:
    print('Você está em uma boa velocidade!!!')