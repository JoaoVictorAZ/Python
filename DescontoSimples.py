valor=float(input("Informe o valor total do produto:"))
desconto=float(input("Coloque aqui a porcentagem de desconto oferecido:"))
valordesc=valor*(desconto/100)
valorfinal=valor-valordesc
print(f"\nValor do desconto {valordesc}\nValor final {valorfinal}")
