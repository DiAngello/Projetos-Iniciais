dv=int(input('Qual a distÂncia da viagem, em Km/h? '))
if dv <= 200:
    v1=dv*0.5
    print('O valor da viagem será: R$ {}'.format(v1))
else:
    v2=dv*0.45
    print('O valor da viagem será: R$ {}'.format(v2))
