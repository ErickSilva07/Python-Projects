
velocidade = int(input("Qual a velocidade atual do carro?: "))
if velocidade >80:
    print("\033[1;31;40mMULTADO, você ultrapassou o limite de velocidade que é 80km/h\033[m")
    multa = (velocidade - 80) * 7
    print(f"\033[1;31;40mVocê deverá pagar uma multa de {multa}R$\033[m")
else:
    print("Tudo certo :) Boa viagem!")
