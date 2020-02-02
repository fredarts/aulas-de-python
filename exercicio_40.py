nota_1 = float(input('Digite a primeira nota'))
nota_2 = float(input('digite a segunda nota'))

média = (nota_1 + nota_2) / 2

if média < 5:
    print('Sua média foi {}, você está reprovado'.format(média))
elif média > 5 and média < 6.9:
    print('Você está de recuperação, sua nota foi {}'.format(média))
else:
    print('Você foi aprovado, sua média foi {}'.format(média))

