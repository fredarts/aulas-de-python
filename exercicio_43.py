peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do peso, seu imc é {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal, seu imc é {:.0f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso, seu imc é {:.0f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade, seu imc é {:.0f}'.format(imc))
else:
    print('Obesidade Morbida, seu imc é {:.0f}'.format(imc))