salario = float(input('qual o salario do funcionario? R$'))
aumento = salario + (salario * 15 / 100)

print('o salario do funcionario é {:.0f}'.format(aumento))