dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos kilometros o carro percorreu? '))
valor = (dias * 60) + (km * 0.15)
print('Total a ser pago é R${:.2f}'.format(valor))
