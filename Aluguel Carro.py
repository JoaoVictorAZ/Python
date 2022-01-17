km=float(input("Informe quantos kilômetros foram percorridos:"))
dia=int(input("Quantos dias ele foi alugado?"))
preçokm= km*0.15
preçodia= dia*60
preçofinal= preçokm+preçodia
print(f"\nO preço a ser pago por {km} Kilômetros rodados e {dia} dias passados é de:\n)")
print("R${:.2f}".format(preçofinal))
