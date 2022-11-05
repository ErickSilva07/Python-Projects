"""co = float(input('O cateto oposto é: '))
ca = float(input('O cateto adjacente é: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'A hipotenusa é {hi:.2f}')"""

'''import math

co = float(input('O cateto oposto é: '))
ca = float(input('O cateto adjacente é: '))
hi = math.hypot(ca, co)
print(f'A hipotenusa é {hi:.2f}')'''

from math import hypot
co = float(input('O cateto oposto é: '))
ca = float(input('O cateto adjacente é: '))
hi = hypot(co, ca)
print(f'A hipotenusa é {hi:.2f}')