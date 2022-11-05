salario = float(input("Digite seu sálario R$: "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f"Quem ganhava {salario} passa a ganhar {novo} agora ")
