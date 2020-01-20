dinheiro = float(input('quanto de dinheiro vc tem na carteira'))
dolar = dinheiro / 3.74
print('Com R${} você pode comprar U${:.2f}'.format(dinheiro, dolar))