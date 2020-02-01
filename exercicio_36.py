valorcasa = int(input('Qual o valor da casa?'))
salario = int(input('Qual o valor do seu salario?'))
prazo = int(input('Em quantos anos você quer pagar?'))

prestacao = valorcasa / prazo /12

if prestacao > salario * 0.3:
    print('Seu emprestimo foi negado')
else:
    print('seu emprestimo foi autorizado')
    print('Sua parcela ficou em {:.0f}'.format(prestacao))

