salario = int(input('Digite o salario a ser calculado'))

if salario > 1250:
    salario *= 1.1
    print('Seu salario é {:.2f}'.format(salario))
else:
    salario *= 1.15
    print('Seu salario é {:.2f}'.format(salario))