primeiro = int(input('Digite o primeiro numero'))
segundo = int(input('Digite o segundo numero'))
terceiro = int(input('Digite o terceiro numero'))

teste = [primeiro, segundo, terceiro]
teste.sort(reverse=True)
print('Numero maior', teste[0], 'numero menor', teste[2])

