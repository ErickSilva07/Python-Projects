num = int(input("Digite um número: "))
resultado = num % 2
if resultado == 1:
    print(f"O número {num} é \33[1;31;40mímpar!\033[m")
else:
    print(f"O número {num} é \33[1;34;40mpar!\33[m")
