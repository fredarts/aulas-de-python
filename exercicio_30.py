numero = int(input('me diga um numero qualquer'))
resultado = numero % 2
if resultado == 1:
    print('o numero {} é impar'.format(resultado))
else:
    print('O numero {} é par'.format(resultado))