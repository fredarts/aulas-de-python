import math
co = float(input('digite o cateto oposto'))
ca = float(input('digite o cateto adjacente'))
hipotenusa = math.hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hipotenusa))
