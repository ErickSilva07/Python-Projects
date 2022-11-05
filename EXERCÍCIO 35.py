print("\033[030;40m<>\033[m"*20)
print("       ANALISADOR DE TRIÂNGULOS")
print("\033[030;40m<>\033[m"*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um TRIÂNGULO")
else:
    print("Os segmentos não podem formar um TRIÂNGULO")
