#n1 = int(input("Digite um número: "))
#n2 = int(input("Digite o segundo número: "))
#if n1 > n2:
    #print("O número", n1, "é maior")
#else:
 #   if n1 == n2:
   #     print("Os números são iguais")
 #   else:
  #     print("O número", n2, "é maior")


#valor = float(input("Digite um valor: "))
#if valor > 0:
 #   print("O valor é positivo")
#else:
   # if valor == 0:
    #    print("Nem positivo nem negativo")
  #  else:
 #       print("O valor é negativo")


letra = str(input("Digite uma letra: "))
if letra == "m":
    print("\033[1;34;40mA letra é masculina\033[m")
else:
    if letra == "f":
        print("\033[1;35;40mA letra é feminina\033[m")
    else:
        print("Você não digitou m ou f")
