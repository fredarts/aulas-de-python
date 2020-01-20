n1 = int(input('Digita um valor:'))
n2 = int(input('Digita outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}\no produto é {}\na divisão é {:.3f}'.format(s, m, d), end='')
print('A divisão inteira {} e a pontecia {}'.format(di, e))
