media=float(input("Informe qual a média necessária para passar:"))
n1=float(input("Digite sua primeira nota:"))
n2= float(input("Digite sua segunda nota:"))
m=(n1+n2)/2
if m <= media:
    print(f"Sua média foi: {m}")
    print("Você está abaixo da média, se esforce mais para recuperar sua nota!")
else:
    print(f"Sua média foi: {m}")
    print("Parabéns, você está acima da média necessária, continue assim!")
