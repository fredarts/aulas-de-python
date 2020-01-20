medida = float(input('uma medida em metros:'))
cm = medida * 100
mm = medida * 1000
print('A medida em {:.0f}m corresponde {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))