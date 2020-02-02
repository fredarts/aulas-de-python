num = int(input('qual numero você quer converter?'))

print('''Escolha uma das bases para conversão
[ 1 ] Converter para  Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opcao = int(input('Sua Opção'))

if opcao == 1:
    print('Seu numero {} em Binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('Seu numero {} em Octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('Seu numero {} em Hexadecial é {}'.format(num, hex(num)[2:]))

else:
    print('opção inválida, tente novamente')

