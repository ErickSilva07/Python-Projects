medida = float(input('Medida em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
dc = medida / 10
hc = medida / 100
print(f' A medida de {medida} metros correspondem a \n {cm:.0f} centimetros \n {mm:.0f} mílimetros')
print(f' {km} kilometros \n {dc} decâmetros \n {hc} hectõmetros')
