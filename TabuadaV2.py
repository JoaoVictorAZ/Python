numero=int(input("Digite o número para mostrar sua tabuada:"))
for x in range(10,-1,-1):
    tabuada=numero*x
    print(f"{numero} x {x} = {tabuada}")
