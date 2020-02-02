r1 = float(input('Primeiro segmento'))
r2 = float(input('Segundo segmento'))
r3 = float(input('Terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('esses valores formam um triangulo')
    if r1 == r2 == r3:
        print('seu triangulo é equilátero')
    elif r1 != r2 != r3:
        print('seu triangulo é Escaleno')
    else:
        print('eu triangulo é isósceles')

else:
    print('Seu segmentos não formam um triangulo')
