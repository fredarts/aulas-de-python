velocidade = int(input('Qual a velocidade do carro?'))

if velocidade >= 80:
    print('Você foi multado')
    print('O valor da sua multa foi de {} reais'.format((velocidade - 80) * 7))
