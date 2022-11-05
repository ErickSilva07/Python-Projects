# Estruturas sequênciais e Condicionais
nome = str(input("Digite seu nome: "))
nota1 = float(input(f"Digite a sua primeira nota {nome}: "))
nota2 = float(input(f"Digite a sua segunda nota {nome}: "))
m = (nota1 + nota2) / 2
print(f"Sua média foi {m}")
if m >= 6.0:
    print(f"Parabéns {nome}, você foi aprovado")
else:
    print(f"Parabéns {nome}, Você é um jumento")