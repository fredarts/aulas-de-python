tempo = int(input('Quantos anos tem seu carro?'))
if tempo >= 3:
    print('{} anos já é um carro velho'.format(tempo))
    if tempo == 100:
        print('eita porra, velho pra caralho {} anos'.format(tempo))
else:
    print('Seu carro ainda é novo, só tem apenas {} anos'.format(tempo))

