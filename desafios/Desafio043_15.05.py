p=int(input('Digite seu peso: '))
a=float(input('Digite sua altura: '))
imc=p/a**2
if 18.5 <= imc <= 25:
    print('Você está no peso ideal: {}'.format(imc))
elif imc <= 18.5:
    print('Você está abaixo do peso ideal: {}'.format(imc))
elif 25 <= imc <= 30:
    print('Você está no sobrepeso: {}'.format(imc))
elif 30 <= imc <= 40:
    print('Você está acima do peso ideal (obesidade): {}'.format(imc))
elif imc >= 40:
    print('Você está com obesidade mórbita: {}'.format(imc))
