import math

ângulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo {ângulo} tem o seno de {seno:.2f}')
coseno = math.cos(math.radians(ângulo))
print(f'O angulo de {ângulo} tem o coseno de {coseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O angulo de {ângulo} tem a tangente de {tangente:.2f}')