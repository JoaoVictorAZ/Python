n1=int(input("Informe o primeiro número:"))
n2=int(input("Infome agora o segundo número:"))
n3=int(input("Por fim informe o terceiro número:"))

if n1>n2 and n1>n3:
    print(f"O maior número é {n1}")
elif n2>n1 and n2>n3:
    print(f"O maior número é {n2}")
elif n3>n1 and n3>n2:
    print(f"O maior número é {n3}")
