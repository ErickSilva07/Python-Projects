distancia = float(input("Qual a distância da viagem?: "))
print(f"Você está prestes a começar uma viagem de {distancia} km")
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
