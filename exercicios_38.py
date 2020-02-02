numero1 = int(input('Digite o primeiro valor'))
numero2 = int(input('Digite o segundo valor'))

if numero1 > numero2:
    print('O Primeiro número é maior, {} que o segundo numero {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('Segundo numero é maior, {} que o primeiro número {}'.format(numero2, numero1))
else:
    print('Os valores {} e {} são iguais'.format(numero1, numero2))