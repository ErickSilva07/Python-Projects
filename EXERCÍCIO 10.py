real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 4.82
euro = real / 5.16
libra = real / 6.08
print(f'com R${real:.2f} você consegue comprar \n U${dolar:.2f} \n EUR${euro:.2f} \n LIB${libra:.2f}')
