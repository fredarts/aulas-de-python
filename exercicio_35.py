r1 = float(input('Primeiro segmento'))
r2 = float(input('Segundo segmento'))
r3 = float(input('Terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('esses valores formam um triangulo')
else:
    print('esses valores nao formam um triangulo')

