distancia = int(input('qual a distancia da sua viagem'))
if distancia <= 200:
    print('Sua viagem custará {} reais'.format(distancia * 0.5))
else:
    print('sua viagem custará {} reais'.format(distancia * 0.45))